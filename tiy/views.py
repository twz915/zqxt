# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import (
                HttpResponse,
                HttpResponseNotFound,
                HttpResponseRedirect,
                Http404)

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.conf import settings
from django.http.request import validate_host
from django.db.models import F
from django.views.generic import View
from .models import Instance,DownloadStatistic

from urlparse import urlsplit
import datetime
from mobi.decorators import detect_mobile
import json
import os

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'src')


def download_statistic(request, requested_file):
    full_file_path = os.path.join(settings.MEDIA_ROOT, requested_file)
    if not requested_file or not os.path.exists(full_file_path):
        raise Http404

    # the usual case is that there is already at least one download of a
    # file, so only on creation we would trigger an additional query
    if not DownloadStatistic.objects.filter(download_url=requested_file
            ).update(count=F('count')+1):
        DownloadStatistic.objects.create(download_url=requested_file, count=1)

    return redirect('/media/'+requested_file)


def get_demo_url(name,type_, column=None):
    args = ['name={}'.format(name),
            'type={}'.format(type_)]
    if column is not None:
        args.append('column={}'.format(column))
    demo_url=reverse('demo')

    return demo_url + '?' + '&'.join(args)


def come_from_validate_host(request):
    coming_host = urlsplit(request.META.get('HTTP_REFERER','')).hostname
    if not (coming_host is not None and
            validate_host(coming_host, settings.ALLOWED_HOSTS)):
        return False
    return True


def demo(request):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        column = request.GET.get('column', None)
        type_ = request.GET.get('type', None)

        if name is None:
            return HttpResponseNotFound(format_html(u'''
                <h1>自强学堂</h1>
                <h3>警告，这个页面必须从调试页面发起，页面刷新后无效，请从在线测试页面提交代码</h3>
                <h2><a href="http://www.ziqiangxuetang.com">返回自强学堂首页</a><h2>'''))

        query_dict = {'name__iexact': name}
        if column is not None:
            query_dict['column__iexact'] = column

        if not come_from_validate_host(request):
            instance = Instance.objects.filter(**query_dict)[0]

            return HttpResponseNotFound(format_html(u'''
                    <h1>自强学堂</h1>
                    <h2>抱歉，不能直接访问该页面，请<a href="{0}">前往测试页面</a><h2>''',
                    instance.get_absolute_url()))

        try:
            instance = Instance.objects.filter(**query_dict)[0]
            if type_ == 'result':
                if '404 NOT FOUND!' in instance.code:
                    instance.result = 'NOT FOUND!'
                    instance.code='NOT FOUND!'
                    instance.save()
                return HttpResponse(instance.result)

            return HttpResponse(instance.code)
        except (Instance.DoesNotExist, IndexError):
            return HttpResponse('请在左侧输入源代码后，点击提交代码')

    # when users post code to server
    elif request.method == 'POST':
        code = request.POST.get('code', u'Error')
        saveit = request.POST.get('saveit', '')
        if request.user.is_superuser and saveit == 'yes':
            name = request.POST.get('name', None)
            if name is not None:
                i = Instance.objects.get_or_create(name=name)[0]
                i.code = code
                i.save()
        response = HttpResponse(code, content_type='text/html')
        response['X-XSS-Protection'] = '0'
        return response


@detect_mobile
def showit(request, name, column=None, show_result=False, tryit=False):
    kwargs = {'name': name}

    if show_result:
        template = 'showfile.html'
    elif tryit:
        template = 'tryit.html'
    else:
        template = 'showit.html'

    if column is not None:
        kwargs['column'] = column

    try:
        #print 'query tiy database'
        instance = Instance.objects.filter(**kwargs)[0]
        kwargs['code'] = instance.code
        if show_result:
            kwargs['result'] = instance.result

    except (Instance.DoesNotExist, IndexError):
        if tryit:
            kwargs['code'] = '请将代码复制到此输入框，然后点击上方的【提交代码】'
        else:
            raise Http404

    return render(request, template, kwargs)


def tiy(request, name):
    return showit(request, name, tryit=True)


def showfile(request, name):
    return showit(request, name, show_result=True)


def showphp(request, name):
    return showit(request, name, column='php')


def showasp(request, name):
    return showit(request, name, column='asp')


def ajax_database(request):
    keyword = request.GET.get('q', '')
    #用字典模拟一个数据库
    with open(os.path.join(SRC_DIR,'ajax_database.json')) as f:
        CompanyDict = json.load(f)

    info = CompanyDict.get(keyword, "Couldn't find!")
    return HttpResponse(info, content_type='text/html')


def try_color(request):
    colorName = request.GET.get('color', '')
    colorHex = request.GET.get('hex', '')
    color = colorName if colorName else '#%s' % colorHex

    return render(request, 'html_color.html', {'color': color})


def ajax_suggest(request):
    keyword = request.GET.get('q', '').capitalize()
    with open(os.path.join(SRC_DIR,'names.txt')) as f:
        hints = [name.strip() for name in f if keyword in name]

    hint = ', '.join(sorted(hints)) or "Couldn't find!"
    return HttpResponse(hint)


def demo_get(request):
    if request.method == 'GET':
        now = unicode(datetime.datetime.now())
        return HttpResponse('服务器当前时间: {}.'.format(now))
    else:
        return HttpResponseNotFound("您请求的方法不是GET方法！")


def demo_get2(request):
    if request.method == 'GET':
        info = u'%s %s, 今天过得怎么样？' % (
            request.GET.get('fname', 'Dear'),request.GET.get('lname', 'User'))
        return HttpResponse(info)
    else:
        return HttpResponseNotFound("您请求的方法不是GET方法！")


def jqeury_ajax_get(request):
    if request.method == 'GET':
        return HttpResponse('这是来自外部PHP文件的一些文本。')
    else:
        return HttpResponseNotFound("您请求的方法不是GET方法！")


@csrf_exempt
def jqeury_ajax_post(request):
    if request.method == 'POST':
        info = 'Dear %s Hope you live well in %s.' % (
            request.POST.get('name', 'User'),request.POST.get('city', 'China'))
        return HttpResponse(info)
    else:
        return HttpResponseNotFound("您请求的方法不是POST方法！")


@csrf_exempt
def jqeury_ajax_post2(request):
    if request.method == 'POST':
        info = u'%s %s, 很开心你能在自强学堂学到有用的知识！' % (
            request.POST.get('fname', 'Dear'),request.POST.get('lname', 'User'))
        return HttpResponse(info)
    else:
        return HttpResponseNotFound("您请求的方法不是POST方法！")
