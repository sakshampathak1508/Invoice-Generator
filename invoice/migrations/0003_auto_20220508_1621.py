# Generated by Django 3.2.13 on 2022-05-08 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_rename_order_itemlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='itemlist',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='invoice.order'),
            preserve_default=False,
        ),
    ]
