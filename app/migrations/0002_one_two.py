# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=20, null=True)),
                ('oage', models.CharField(max_length=20, null=True)),
                ('odate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Two',
            fields=[
                ('tsub', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.One')),
                ('tfond', models.CharField(max_length=20, null=True)),
                ('tdes', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
