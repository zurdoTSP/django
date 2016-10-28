# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='autor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='leido',
            field=models.IntegerField(null=True),
        ),
    ]
