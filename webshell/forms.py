from django import forms
from .models import Script


class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = '__all__'

    class Media:
        css = {
            'all': ('css/codemirror.css', 'css/pygments_style.css')
        }
        js = ('js/codemirror.js', 'js/python.js')
