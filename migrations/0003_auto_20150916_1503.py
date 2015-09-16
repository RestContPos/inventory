# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_auto_20150914_0002'),
        ('products', '0001_initial'),
        ('inventory', '0002_auto_20150916_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_purshase_real',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_price', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('quantity', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('product', models.ForeignKey(default=1, to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase_real',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('provider', models.ForeignKey(default=1, to='providers.Provider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detail_purshase_real',
            name='purchase_real',
            field=models.ForeignKey(default=1, to='inventory.Purchase_real'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory_real',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
