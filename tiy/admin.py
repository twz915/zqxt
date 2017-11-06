from django.contrib import admin

from .models import Instance
from .models import DownloadStatistic


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'column', 'url', 'create_date', 'update_time',)
    search_fields = ('name', 'column', 'code', 'result',)
    list_filter = ('name', 'column', 'code', 'result',)
    readonly_fields = ('create_date', 'update_time',)


@admin.register(DownloadStatistic)
class DownloadStatisticAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('download_url', 'count')
    search_fields = ['download_url', ]
