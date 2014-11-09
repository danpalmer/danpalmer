# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='post_images')),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('post', models.ForeignKey(to='blog.Post', related_name='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(editable=False, default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(null=True, upload_to='title_images', blank=True),
        ),
    ]
