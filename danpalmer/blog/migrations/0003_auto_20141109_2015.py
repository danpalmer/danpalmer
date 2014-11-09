# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141109_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]
