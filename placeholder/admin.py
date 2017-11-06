from django.contrib import admin
from .models import PlaceHolder


@admin.register(PlaceHolder)
class PlaceHolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'create_time', 'update_time']
