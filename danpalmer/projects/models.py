import datetime

from django.db import models


class Contribution(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="", blank=True)
    source_url = models.URLField(max_length=2000)

    created = models.DateTimeField(default=datetime.datetime.utcnow)
