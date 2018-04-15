# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-15 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('review', models.CharField(blank=True, max_length=200, null=True)),
                ('className', models.CharField(max_length=30, null=True)),
                ('topSpeed', models.CharField(max_length=15, null=True)),
                ('releaseDate', models.DateField()),
                ('designer_name', models.CharField(blank=True, max_length=50)),
                ('nationality', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(blank=True, max_length=20)),
                ('p_country', models.CharField(blank=True, max_length=30)),
                ('website', models.URLField(blank=True)),
                ('bikeModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motorcycles.Bike')),
            ],
        ),
    ]
