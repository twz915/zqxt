from django.conf.urls import patterns, include, url
from django.views.generic.base import (TemplateView, RedirectView)

# sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.views.decorators.cache import cache_page
from . import sitemaps_views

from django.conf import settings

from tutorial.views import LatestEntriesFeed
from tutorial.models import Tutorial
from tiy.models import Instance
import os

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'tutorial.views.index', name='index'),
    url(r'^j/(?P<token>.+)/$', 'iclick.views.click_count', name='click-count'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain'), name='robots'),
    url(r'^error_tutorial\.py$', 'tutorial.views.error_tutorial', name='error-tutorial'),
)

# try it yourself
urlpatterns += patterns('tiy.views',
    url(r'^try/color\.py$', 'try_color', name='try-color'),
    url(r'^try/ajax/demo_get\.php$', 'demo_get', name='demo-get'),
    url(r'^try/ajax/demo_test2\.php$', 'demo_get2', name='demo-get2'),
    url(r'^try/ajax/demo_test\.php$', 'jqeury_ajax_get', name='jquery-ajax-get'),
    url(r'^try/ajax/demo_test_post\.php$', 'jqeury_ajax_post', name='jquery-ajax-post'),
    url(r'^try/ajax/demo_test_post2\.php$', 'jqeury_ajax_post2', name='jquery-ajax-post2'),
    url(r'^try/ajax_gethint\.asp$', 'ajax_suggest', name='ajax-suggest'),
    url(r'^try/ajax_database/$', 'ajax_database', name='ajax-database'),

    url(r'^try/([^/]+)/$', 'tiy', name='tiy'),
    url(r'^showasp/([^/]+)/$', 'showasp', name='show-asp'),
    url(r'^showphp/([^/]+)/$', 'showphp', name='show-php'),
    url(r'^showfile/([^/]+)/$', 'showfile', name='show-file'),
    # the following just used to handle history question
    url(r'^try/([^/]+)$', 'tiy', name='tiy2'),
    url(r'^showasp/([^/]+)$', 'showasp', name='show-asp2'),
    url(r'^showphp/([^/]+)$', 'showphp', name='show-php2'),
    url(r'^showfile/([^/]+)$', 'showfile', name='show-file2'),

    url(r'^demo/$', 'demo', name='demo'),
    url(r'^download/(?P<requested_file>.+)', 'download_statistic', name='download_view'),
)

urlpatterns += patterns('',
    url(r'^weixin/$', 'zqxt.wechat.index'),
    url(r'^webshell/', include('webshell.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^latest_feed/$', LatestEntriesFeed(), name='feed'),
)

# static/media/demo files
if settings.ON_LOCAL_HOST:
    from django.conf.urls.static import static

    urlpatterns += (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.DEMO_URL, document_root=settings.DEMO_ROOT) +
        static('/try/', document_root=os.path.join(settings.BASE_DIR, 'try'))
    )

urlpatterns += patterns('tutorial.views',
    url(r'^([^/]+)\.htm$', 'auto_to_template'),
    # 301 permanent redirect to first content page
    url(r'^(?P<column_slug>[^/]+)/$', 'column_default_page', name='column'),

    url(r'^(?P<column_slug>[^/]+)/(?P<tutorial_slug>[^/]+)$',
        'tutorial_detail', name='tutorial-detail'),
)


class LimitGenericSitemap(GenericSitemap):
    limit = 200


sitemaps = {
    'tutorials': LimitGenericSitemap(
            {'queryset': Tutorial.objects.all(), 'date_field': 'update_time'},
            priority=1.0),
    'tiy': LimitGenericSitemap(
            {'queryset': Instance.objects.all(), 'date_field': 'update_time'},
            priority=0.5),
}


urlpatterns += patterns('',
    url(r'^sitemap\.xml$',
        cache_page(86400)(sitemaps_views.index),
        {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    url(r'^sitemap-(?P<section>.+)-(?P<page>\d+)\.xml$',
        cache_page(86400)(sitemaps_views.sitemap),
        {'sitemaps': sitemaps}, name='sitemaps'),
)
