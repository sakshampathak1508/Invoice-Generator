# Generated by Django 3.2.13 on 2022-05-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_remove_itemlist_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='invoice.order'),
            preserve_default=False,
        ),
    ]
