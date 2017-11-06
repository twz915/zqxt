from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class PlaceHolder(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    code = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return 'PlaceHolder ({})'.format(self.name)
