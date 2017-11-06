from django.db import models


class Script(models.Model):
    name = models.CharField(max_length=100)
    source = models.TextField()

    def __unicode__(self):
        return self.name


class Shell(models.Model):
    name = models.CharField(max_length=100)
    source = models.TextField()

    def __unicode__(self):
        return self.name
