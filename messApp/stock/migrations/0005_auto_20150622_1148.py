# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20150622_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(related_name=b'Transaction', to='stock.Item', to_field=b'item_name'),
        ),
    ]
