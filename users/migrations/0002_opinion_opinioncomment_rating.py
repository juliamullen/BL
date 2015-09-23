# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktalk', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.TextField()),
                ('segment', models.ForeignKey(to='booktalk.Segment')),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OpinionComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=300)),
                ('opinion', models.ForeignKey(to='users.Opinion')),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('book', models.ForeignKey(to='booktalk.Book')),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
    ]
