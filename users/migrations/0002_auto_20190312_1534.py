# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_more_info',
            name='u_header',
            field=models.ImageField(default='static/users/header/default.png', upload_to='static/users/header', verbose_name='用户头像'),
        ),
    ]
