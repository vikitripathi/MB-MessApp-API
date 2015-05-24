# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=30)),
                ('item_unit', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name=b'date recently modified')),
            ],
            options={
                'ordering': ['item_id', 'item_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_type', models.CharField(max_length=10, choices=[(b'Consumption', b'Consumption'), (b'Purchase', b'Purchase'), (b'Expired', b'Expired')])),
                ('quantity', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('inventory', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Date issued')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name=b'Transaction date')),
                ('consumption', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('name', models.OneToOneField(related_name=b'itemUnit', primary_key=True, serialize=False, to='stock.Item')),
                ('shorthand', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(related_name=b'itemTransaction', to='stock.Item'),
            preserve_default=True,
        ),
    ]
