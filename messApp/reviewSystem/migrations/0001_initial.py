# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('items_type', models.CharField(max_length=30, choices=[(b'BreakFast', b'BreakFast'), (b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=30)),
                ('item_id', models.CharField(max_length=10)),
                ('item_rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ratings', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(verbose_name=b'date rated')),
                ('item', models.ForeignKey(to='reviewSystem.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75)),
                ('tiemstamp', models.DateTimeField(verbose_name=b'date recently rated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(related_name=b'user_rating', to='reviewSystem.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='item',
            field=models.ForeignKey(related_name=b'category_type', to='reviewSystem.Item'),
            preserve_default=True,
        ),
    ]
