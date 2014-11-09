# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141109_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', blank=True),
        ),
    ]
