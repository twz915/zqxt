#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-27 16:11:03
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
from __future__ import unicode_literals

import sys
from django.conf import settings
from django import http
from django.http import HttpResponsePermanentRedirect as redirect_to
from django.http import Http404

from django.conf import settings
from django.contrib.redirects.models import Redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.debug import technical_500_response


class RedirectMiddleware(object):
    '''
    Custom middleware to realize complex redirects
    '''
    redirects_dict = {r.old_path: r.new_path
            for r in Redirect.objects.all().only('old_path', 'new_path')}

    def process_request(self, request):
        host = request.get_host()
        full_path = request.get_full_path()

        if '.duapp.com' in host:
            return redirect_to('http://www.ziqiangxuetang.com{}'.format(full_path))

        elif 'besttome.com' in host:
            if 'django' in full_path:
                if 'ajax' in full_path:
                    return redirect_to(
                        'http://www.ziqiangxuetang.com/django/django-ajax.html')
                return redirect_to(
                    'http://www.ziqiangxuetang.com/django/django-tutorial.html')
            elif 'datetime_strftime' in full_path:
                return redirect_to(
                    'http://www.ziqiangxuetang.com/python/datetime_strftime.html')
            elif 'python' in full_path:
                return redirect_to(
                    'http://www.ziqiangxuetang.com/python/python-tutorial.html')
            else:
                return redirect_to('http://www.ziqiangxuetang.com')

        elif full_path in self.redirects_dict:
            return redirect_to(
                self.redirects_dict[full_path])


class DoesNotExistsMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            raise Http404


class BlockedIpMiddleware(object):
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in getattr(settings, "BLOCKED_IPS", []):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')


class UserBasedExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if (request.user.is_superuser
                or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS):
            return technical_500_response(request, *sys.exc_info())
