from django.db import models
from django.core.urlresolvers import reverse_lazy as reverse


class Link(models.Model):
    token = models.CharField(primary_key=True, max_length=20)
    to_url = models.CharField(max_length=256)
    count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('click-count', args=(self.token,))
