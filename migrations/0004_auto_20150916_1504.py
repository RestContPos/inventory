# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('inventory', '0003_auto_20150916_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_purchase_real',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_price', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('quantity', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('product', models.ForeignKey(default=1, to='products.Product')),
                ('purchase_real', models.ForeignKey(default=1, to='inventory.Purchase_real')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='detail_purshase_real',
            name='product',
        ),
        migrations.RemoveField(
            model_name='detail_purshase_real',
            name='purchase_real',
        ),
        migrations.DeleteModel(
            name='Detail_purshase_real',
        ),
    ]
