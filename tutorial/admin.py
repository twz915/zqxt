# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages

from .models import Tutorial, Column, ContentLink, ErrorTutorial
from zqxt.push_to_search_engine import submit_link, submit_sitemap


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_per_page = 20
    raw_id_fields = ('column', 'prev', 'next',)
    list_display = ('title', 'url', 'id', 'pub_date', 'update_time', 'is_published',)
    search_fields = ('title', 'slug', 'content',)
    list_filter = ('column', 'published', 'author',)

    def save_model(self, request, obj, form, change):
        obj.save()
        # save order
        if obj.prev is not None:
            obj.prev.next = obj
            obj.prev.save(update_fields=['next'])
        if obj.next is not None:
            obj.next.prev = obj
            obj.next.save(update_fields=['prev'])

        if obj.published:
            url = 'http://www.ziqiangxuetang.com' + obj.get_absolute_url()
            try:
                ret = submit_link(url)
            except:
                ret = '投送失败'
            self.message_user(request, ret, messages.INFO)

            try:
                ret = submit_sitemap(obj.get_xml())
            except:
               ret = '提交sitemap失败'
            self.message_user(request, ret, messages.INFO)
        else:
            self.message_user(
                request, '成功添加一篇草稿，正式发布时会推送给百度', messages.WARNING)


class ColumnInline(admin.TabularInline):
    model = Column

    verbose_name = u'子栏目'
    verbose_name_plural = u'子栏目'


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id',)
    search_fields = ('name', 'slug',)


@admin.register(ContentLink)
class ContentLinkAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'link', 'published', 'pub_date', 'update_time',)
    search_fields = ('keyword', 'link',)


@admin.register(ErrorTutorial)
class ErrorTutorialAdmin(admin.ModelAdmin):
    list_display = ('url', 'email', 'desc', 'pub_date', 'update_time')
    search_fields = ('url', 'email', 'desc',)
