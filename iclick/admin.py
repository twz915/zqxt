from django.contrib import admin
from iclick.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['token', 'to_url', 'count']
