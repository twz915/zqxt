#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-15 09:59:45
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'zqxt.settings'

from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication

application = WSGIApplication(get_wsgi_application())
