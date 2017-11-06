from django.contrib import admin
from .forms import ScriptForm
from .models import Script, Shell


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    form = ScriptForm
    change_form_template = 'webshell/python.html'


@admin.register(Shell)
class ShellAdmin(admin.ModelAdmin):
    form = ScriptForm
    change_form_template = 'webshell/shell.html'
