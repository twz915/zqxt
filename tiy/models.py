#coding:utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.db import models

from tutorial.fields import CompressedTextField

@python_2_unicode_compatible
class Instance(models.Model):
    name = models.CharField('名称', db_index=True, max_length=255)
    column = models.CharField('栏目', blank=True, null=True, max_length=100)

    code = CompressedTextField('代码', blank=True, null=True)
    result = CompressedTextField('结果', blank=True, null=True)

    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.column in ['asp','php']:
            viewname = 'show-{}'.format(self.column)
        elif self.result is not None and self.result.strip():
            viewname = 'show-file'
        else:
            viewname = 'tiy'
        return reverse(viewname, args=(self.name,))

    def url(self):
        return format_html('<a href="{}" target="_blank">{}</a>', 
                            self.get_absolute_url(), self.name)
    url.allow_tags = True

    class Meta:
        verbose_name = u'实例'
        verbose_name_plural = u'实例'


@python_2_unicode_compatible
class DownloadStatistic(models.Model):
    """
    Holds the information about how often a certain file was downloaded.

    :download_url: The URL from where the file was downloaded.
    :count: The amount of times this URL was clicked.

    """

    download_url = models.CharField('下载链接',max_length=512,db_index=True)
    count = models.PositiveIntegerField('下载次数')

    def __str__(self):
        return '{} ({})'.format(
            '...' + self.download_url[-50:] if len(self.download_url) > 50
            else self.download_url, self.count)

    class Meta:
        verbose_name = u'下载统计'
        verbose_name_plural = u'下载统计'

