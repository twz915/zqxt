# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import PlaceHolder as PlaceHolderModel
from django.utils.html import mark_safe, format_html
from django.template import Context, Template


class _PlaceHolder(object):
    def __init__(self, context_dict={}):
        assert isinstance(context_dict, dict)
        self.context_dict = context_dict

    def __getattr__(self, name):
        try:
            ph = PlaceHolderModel.objects.get(name=name)
        except PlaceHolderModel.DoesNotExist:
            return format_html(
                '<!-- add placeholder ({}) in admin -->', name)

        template = Template(ph.code)
        context = Context(self.context_dict)

        return mark_safe(template.render(context))


'''get placeholder lazy'''
placeholder_dict = {
    False: _PlaceHolder({'request.mobile': False}),
    True: _PlaceHolder({'request.mobile': True}),
}


def placeholders(request):
    return {'PlaceHolder': placeholder_dict[request.mobile]}
