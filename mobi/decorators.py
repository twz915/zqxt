#coding:utf-8
from __future__ import unicode_literals

from mobi.middleware import MobileDetectionMiddleware
from functools import wraps


def detect_mobile(view):
    """View Decorator that adds a "mobile" attribute to the request which is
       True or False depending on whether the request should be considered
       to come from a small-screen device such as a phone or a PDA"""

    @wraps(view)
    def detected(request, *args, **kwargs):
        MobileDetectionMiddleware.process_request(request)
        return view(request, *args, **kwargs)
    detected.__doc__ = "%s\n[Wrapped by detect_mobile which detects if the " \
        "request is from a phone]" % view.__doc__
    return detected
