# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nif', models.CharField(unique=True, max_length=9, verbose_name='nif')),
                ('telefono', models.CharField(max_length=9, verbose_name='telefono')),
                ('imagen', models.ImageField(upload_to=b'profile_images', verbose_name='profile images', blank=True)),
                ('secretario', models.BooleanField(default=False, verbose_name='secretario general')),
                ('consejo', models.BooleanField(default=False, verbose_name='consejo ciudadano')),
                ('biografia', models.TextField(max_length=2000, verbose_name='biografia', blank=True)),
                ('motivacion', models.TextField(max_length=2000, verbose_name='motivacion', blank=True)),
                ('youtube', models.CharField(max_length=50, verbose_name='video youtube', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
