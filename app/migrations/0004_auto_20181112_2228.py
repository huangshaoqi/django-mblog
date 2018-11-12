# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181112_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('bauthor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('paddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.ManyToManyField(to='app.Publication'),
        ),
    ]