# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150222_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='slug',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
