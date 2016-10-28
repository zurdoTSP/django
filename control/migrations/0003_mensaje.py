# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20150516_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('texto', models.TextField(max_length=1000, null=True)),
                ('destinatario', models.ForeignKey(to='control.Persona')),
            ],
        ),
    ]
