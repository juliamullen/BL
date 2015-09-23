# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('isbn', models.IntegerField()),
                ('chapters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.IntegerField()),
                ('book', models.ForeignKey(to='booktalk.Book')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='segment',
            field=models.ForeignKey(to='booktalk.Segment'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
