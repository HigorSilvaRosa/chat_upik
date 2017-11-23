# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modificação')),
            ],
            options={
                'verbose_name_plural': 'Mensagens do bate-papo',
                'verbose_name': 'Mensagem do bate-papo',
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modificação')),
            ],
            options={
                'verbose_name_plural': 'Salas do bate-papo',
                'verbose_name': 'Sala do bate-papo',
            },
        ),
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Usuários do bate-papo',
                'verbose_name': 'Usuário do bate-papo',
            },
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='chat_user',
            field=models.ForeignKey(to='core.ChatUser', verbose_name='Chat'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(to='core.ChatRoom', verbose_name='Sala'),
        ),
    ]
