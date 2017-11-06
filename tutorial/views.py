# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from django.views.decorators.cache import cache_page

from django.contrib.syndication.views import Feed

from .models import Tutorial, Column, ContentLink, ErrorTutorial
from pyquery import PyQuery as pq
from urlparse import urljoin, urlsplit


def index(request):
    prefix = ''.join([
        'm' if request.mobile else 'p',
    ])

    def wrap(request):
        latest_tutorials = Tutorial.objects.recently(40)

        return render(request, 'index.html', {
                'latest_tutorials': latest_tutorials,
            })

    if not request.user.is_superuser:
        wrap = cache_page(900, key_prefix=prefix)(wrap)
    return wrap(request)


def column_default_page(request, column_slug):
    try:
        tutorial = Tutorial.objects.published().filter(column__slug=column_slug)\
            .order_by("pub_date")[0]
    except IndexError:
        raise Http404

    return redirect(tutorial, permanent=True)

'''
content_links = ContentLink.objects.filter(published=True)\
        .exclude(keyword__icontains='(').exclude(keyword__icontains=')')\
        .exclude(keyword__icontains='\\').only('keyword','link')

def add_links(content):
    doc = pq(content)
    content = doc.outer_html()
    # protect the following labels
    protect_list = []
    protects = doc('a,pre,code,div.example_code,div.notranslate,img,script,meta,link')
    for index,protect_label in enumerate(protects):
        html = pq(protect_label).outer_html()
        label = 'PROTECT_LABEL_%s'%index
        content = content.replace(html, label)
        protect_list.insert(0, (label, html))
    
    # replace keywords to links
    replace_list = [] # prevent keyword in link to link
    for index,cl in enumerate(content_links):
        keyword = cl.keyword
        link = '<a href="{0}" title="{1}" class="content_link" target="_blank">{1}</a>'.format(cl.link, keyword)
        if keyword not in content:
            continue
        #print keyword
        label = 'REPLACE_LABEL_%s'%index
        content = content.replace(keyword, label)
        replace_list.insert(0, (label,link))
    
    for label,link in replace_list:
        content = content.replace(label, link)
    
    # replace back to html content
    for label, html in protect_list:
        content = content.replace(label, html)
    
    return content
'''

def tutorial_detail(request, column_slug, tutorial_slug):
    prefix = ''.join([
        'm' if request.mobile else 'p',
        column_slug,
        tutorial_slug,
    ])

    def wrap(request, column_slug, tutorial_slug):
        try:
            tutorial = Tutorial.objects.published().get(column__slug=column_slug,
                slug__iexact=tutorial_slug)
        except Tutorial.DoesNotExist:
            if tutorial_slug.lower() in ['default.html', 'index.html',
                    'index.htm']:
                return column_default_page(request, column_slug)

            tutorial = get_object_or_404(Tutorial, slug__iexact=tutorial_slug)
            return redirect(tutorial, permanent=True)

        # tutorial.content = add_links(tutorial.content)
        tutorial.content = tutorial.content.replace(
            'http://static.ziqiangxuetang.com/media/',
            'http://xxxx.oss-cn-xxxx.aliyuncs.com/media/'
        )
        return render(request, 'tutorial.html', {'tutorial': tutorial})

    if not request.user.is_superuser:
        wrap = cache_page(3600, key_prefix=prefix)(wrap)
    return wrap(request, column_slug, tutorial_slug)


def auto_to_template(request, page):
    template = "%s.html" % page
    try:
        get_template(template)
    except:
        raise Http404
    return render(request, template)


def error_tutorial(request):
    if request.method == 'POST':
        kw = {
            'url': request.POST.get('err_url'),
            'email': request.POST.get('err_email', ''),
            'desc': request.POST.get('err_desc', ''),
        }
        ErrorTutorial.objects.get_or_create(**kw)
        return HttpResponse('error submit, ok!')
    else:
        return HttpResponse('need post method!')


class LatestEntriesFeed(Feed):
    title = "自强学堂 在线教程"
    link = "/"
    description = "自强学堂在线教程提供了最全IT技术基础教程, 介绍了HTML教程、CSS教程、Javascript教程、Python基础教程，Django教程，PHP教程 , MySQL教程等各种建站基础。同时本站中也提供了大量的在线实例，通过实例，您可以更好的学习"

    def items(self):
        return Tutorial.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_description()

    def item_pubdate(self, item):
        return item.pub_date
