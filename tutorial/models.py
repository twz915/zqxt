# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.html import format_html
# from tutorial.fields import CompressedTextField

from DjangoUeditor.models import UEditorField


class Column(models.Model):
    # TODO: 保存历史记录，跳转到新的URL的实现
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='', help_text='栏目简介，栏目自定义导航等用途')

    def get_absolute_url(self):
        try:
            tutorial = Tutorial.objects.filter(column__slug=self.slug)\
                .order_by("pub_date")[0]
            return tutorial.get_absolute_url()
        except IndexError:
            return ''

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']


class TutorialManager(models.Manager):
    def recently(self, num=40):
        return self.published().exclude(column__slug='aboutus'
            ).order_by('-update_time')[0:num]

    def published(self):
        return self.get_queryset().filter(published=True,
            pub_date__lt=timezone.now())


class Tutorial(models.Model):
    column = models.ForeignKey(Column,null=True,blank=True,verbose_name='归属栏目')

    title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256, db_index=True)

    author = models.ForeignKey('auth.User',blank=True,null=True,editable=False,verbose_name='作者')
    keywords = models.CharField('关键词',max_length=256, null=True,blank=True, help_text='不写默认为标题')
    description = models.TextField('描述',null=True,blank=True, help_text='不写默认为内容前160字')
    #content = CompressedTextField('内容',default='教程正在编写中……')
    content = UEditorField('内容',height=300,width=1000,
        default='',imagePath="uploads/images/",
        toolbars='besttome',filePath='uploads/files/',blank=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)
    published = models.BooleanField('正式发布',default=True)

    prev = models.ForeignKey("self",null=True,blank=True,verbose_name='上一篇',related_name="prev+")
    next = models.ForeignKey("self",null=True,blank=True,verbose_name='下一篇',related_name="next+")
    # order

    objects = TutorialManager()

    def get_title(self):
        if ' ' in self.title:
            return format_html('''<h1>{} <span class="color_h1">{}</span></h1>''',
                        *self.title.split(' ', 1))
        else:
            return format_html('''<h1>{}</h1>''',self.title)

    def get_keywords(self):
        if self.keywords and self.keywords.strip():
            return self.keywords
        return self.title

    def get_description(self):
        if self.description and self.description.strip():
            return self.description

        if len(self.content) >= 160:
            return self.content[:160]
        else:
            return self.content

    def is_published(self):
        return self.published and self.pub_date < timezone.now()
    is_published.boolean = True
    is_published.short_description = '发布状态'

    def get_absolute_url(self):
        try:
            if self.column is not None:
                return reverse('tutorial-detail', args=(self.column.slug, self.slug,))
            else:
                return self.slug
        except:  # NoneType
            return ''

    def get_next(self):  # 先尝试有没有next,没有按照时间并保存
        next = self.next
        if next:
            return next

        next = self._default_manager.filter(
                column=self.column, pub_date__gt=self.pub_date)[:1]
        if next:
            next = next[0]
            self.next = next
            self.save(update_fields=['next'])
        else:
            next = None
        return next

    def get_prev(self):  # 先尝试有没有prev,没有按照时间找并保存
        prev = self.prev
        if prev:
            return prev
        prev = self._default_manager.filter(
            column=self.column,pub_date__lt=self.pub_date).latest('pub_date')
        self.prev = prev
        self.save(update_fields=('prev',))
        return prev

    def get_next_absolute_url(self):
        next = self.get_next()
        if next:
            return next.get_absolute_url()
        return ''

    def get_prev_absolute_url(self):
        prev = self.get_prev()
        if prev:
            return prev.get_absolute_url()
        return ''

    def url(self):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           self.get_absolute_url(), self.slug)
    url.allow_tags = True

    def get_xml(self):
        url = 'http://www.ziqiangxuetang.com'+self.get_absolute_url()
        title = self.title
        published_time = self.pub_date.strftime('%Y-%m-%d %H:%M')
        lastmod = self.update_time.strftime('%Y-%m-%dT%H:%M:%S')
        column_name = self.column.name

        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset>
    <url>
        <loc><![CDATA[{url}]]></loc>
        <lastmod>{lastmod}</lastmod>
        <priority>1.0</priority>
        <data>
            <display>
                <breadcrumb>所有教程>>{column_name}>>{title}</breadcrumb>
                <name>{title}</name>
                <url><![CDATA[{url}]]></url>
                <genre>{column_name}</genre>
                <provider>
                    <name>自强学堂</name>
                </provider>
                <datePublished>{published_time}</datePublished>
                <isOriginal>TRUE</isOriginal>
            </display>
        </data>
    </url>
</urlset>'''.format(**locals())
        return xml.encode('utf-8')

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
        get_latest_by = 'update_time'
        ordering = ['-update_time']

    def __unicode__(self):
        return self.title


class ContentLink(models.Model):
    keyword = models.CharField('关键词', max_length=100)
    link = models.URLField('链接')
    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('添加时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __unicode__(self):
        return '{0}({1})'.format(self.keyword, self.link)

    class Meta:
        verbose_name = '内链'
        verbose_name_plural = '内链'


class ErrorTutorial(models.Model):
    url = models.URLField('地址')
    email = models.EmailField('邮件', null=True)
    desc = models.TextField('错误详情')
    pub_date = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '错误'
        verbose_name_plural = '错误'
