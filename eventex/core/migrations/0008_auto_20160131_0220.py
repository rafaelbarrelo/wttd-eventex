# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='slot',
            new_name='slots',
        ),
    ]
