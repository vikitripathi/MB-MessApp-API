# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20150621_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['item', '-timestamp']},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(related_name=b'Transaction', to='stock.Item'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.OneToOneField(related_name=b'Unit', primary_key=True, serialize=False, to='stock.Item'),
        ),
    ]
