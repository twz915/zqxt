from django.conf import settings
from django.http import HttpResponseRedirect
from mobi.useragents import search_strings, load_tablet_strings

MOBI_USER_AGENT_IGNORE_LIST = getattr(
    settings,'MOBI_USER_AGENT_IGNORE_LIST', list())

MOBI_DETECT_TABLET = getattr(settings, 'MOBI_DETECT_TABLET', False)


def ignore_user_agent(user_agent):
    """ compare the useragent from the broswer to the ignore list
        This is popular if you want a mobile device to not trigger
        as mobile. For example iPad."""
    if user_agent:
        for ua in MOBI_USER_AGENT_IGNORE_LIST:
            if ua and ua.lower() in user_agent.lower():
                return True
    return False


class MobileDetectionMiddleware(object):
    @staticmethod
    def process_request(request):
        """Adds a "mobile" attribute to the request which is True or False
           depending on whether the request should be considered to come from a
           small-screen device such as a phone or a PDA"""

        if "HTTP_X_OPERAMINI_FEATURES" in request.META:
            #Then it's running opera mini. 'Nuff said.
            #Reference from:
            # http://dev.opera.com/articles/view/opera-mini-request-headers/
            request.mobile = True
            return None

        if "HTTP_ACCEPT" in request.META:
            s = request.META["HTTP_ACCEPT"].lower()
            if 'application/vnd.wap.xhtml+xml' in s:
                # Then it's a wap browser
                request.mobile = True
                return None

        if "HTTP_USER_AGENT" in request.META:
            # This takes the most processing. Surprisingly enough, when I
            # Experimented on my own machine, this was the most efficient
            # algorithm. Certainly more so than regexes.
            # Also, Caching didn't help much, with real-world caches.
            s = request.META["HTTP_USER_AGENT"].lower()
            for ua in search_strings:
                if ua in s:
                    # check if we are ignoring this user agent: (IPad)

                    if not ignore_user_agent(s):
                        request.mobile = True
                        if MOBI_DETECT_TABLET:
                            request.tablet = _is_tablet(s)
                        return None

        #Otherwise it's not a mobile
        request.mobile = False
        return None


def _is_tablet(s):
    is_tablet = False
    tablet_strings = load_tablet_strings()
    for ta in tablet_strings:
        if ta == '__android__not_mobile__':
            if 'android' in s and not 'mobile' in s:
                is_tablet = True
                break

        if ta in s:
            is_tablet = True
            break

    return is_tablet


class MobileRedirectMiddleware(object):

    # Add MOBI_REDIRECT_URL to your settings.py file with a fully qualified
    # url that you want to redirect mobile clients too.
    # i.e. http://example.mobi
    MOBI_REDIRECT_URL = getattr(settings, 'MOBI_REDIRECT_URL', None)

    def process_request(self, request):
        do_redirect = False

        user_agent = request.META.get('HTTP_USER_AGENT', None)

        # mobile browsers are the only people who send this.
        x_wap = request.META.get('HTTP_X_WAP_PROFILE', None)
        http_profile = request.META.get('HTTP_PROFILE', None)

        if x_wap or http_profile:
            do_redirect = True

        #look at the user agent if they don't have x_wap and http_profile
        if user_agent and not do_redirect:
            user_agent = user_agent.lower()
            is_mobile = [w for w in search_strings if w in user_agent]
            if is_mobile:
                do_redirect = True

        if do_redirect and self.MOBI_REDIRECT_URL:
             # tell adaptation services (transcoders and proxies) to not
             # alter the content based on user agent as it's already being
             # managed by this script
             # http://mobiforge.com/developing/story/setting-http-headers-advise-transcoding-proxies
            response = HttpResponseRedirect(self.MOBI_REDIRECT_URL)
            response['Cache-Control'] = 'no-transform'
            response['Vary'] = 'User-Agent, Accept'
            return response
        else:
            return None
