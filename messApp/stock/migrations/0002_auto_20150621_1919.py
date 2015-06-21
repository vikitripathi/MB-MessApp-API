# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=11, choices=[(b'Consumption', b'Consumption'), (b'Purchase', b'Purchase'), (b'Expired', b'Expired')]),
        ),
    ]
