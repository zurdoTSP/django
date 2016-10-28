# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenadas',
            name='x',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='coordenadas',
            name='y',
            field=models.FloatField(null=True),
        ),
    ]
