# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cabecera', models.CharField(max_length=100, null=True)),
                ('compania', models.CharField(max_length=100, null=True)),
                ('texto', models.TextField(max_length=1000, null=True)),
                ('imagen', models.ImageField(upload_to=b'imagenes')),
                ('creador', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField(max_length=500, null=True)),
                ('Articulo', models.ForeignKey(to='control.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenadas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField(null=True)),
                ('y', models.IntegerField(null=True)),
                ('tienda', models.CharField(max_length=100, null=True)),
                ('pertenece', models.ManyToManyField(to='control.Articulo', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=100)),
                ('admin', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('edad', models.IntegerField(null=True)),
                ('imagen', models.ImageField(upload_to=b'imagenes')),
                ('amigos', models.ManyToManyField(related_name='amigos_rel_+', to='control.Persona', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(null=True)),
                ('Articulo', models.ForeignKey(to='control.Articulo')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='creador',
            field=models.ForeignKey(to='control.Persona'),
        ),
    ]
