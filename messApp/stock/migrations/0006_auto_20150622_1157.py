# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20150622_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(related_name=b'Transaction', to='stock.Item'),
        ),
    ]
