# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apellidos')),
                ('email', models.CharField(unique=True, max_length=50, verbose_name=b'Email')),
                ('nif', models.CharField(unique=True, max_length=9, verbose_name=b'NIF')),
                ('telefono', models.CharField(max_length=9, verbose_name=b'Tel\xc3\xa9fono')),
                ('imagen', models.ImageField(upload_to=b'profile_images', verbose_name=b'Imagen', blank=True)),
                ('secretario', models.BooleanField(default=False, verbose_name=b'Secretario General')),
                ('consejo', models.BooleanField(default=False, verbose_name=b'Consejo Ciudadano')),
                ('biografia', models.TextField(max_length=2000, verbose_name=b'Biograf\xc3\xada', blank=True)),
                ('motivacion', models.TextField(max_length=2000, verbose_name=b'Motivaci\xc3\xb3n', blank=True)),
                ('youtube', models.CharField(max_length=50, verbose_name=b'V\xc3\xaddeo youtube', blank=True)),
                ('activo', models.BooleanField(default=True, verbose_name=b'Activo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
