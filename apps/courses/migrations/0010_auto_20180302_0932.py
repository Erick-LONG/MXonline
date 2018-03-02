# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='讲师忠告'),
        ),
        migrations.AddField(
            model_name='course',
            name='u_need_know',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]
