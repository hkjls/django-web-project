# Generated by Django 4.2.4 on 2023-09-05 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_order_list_customer_id_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_list_customer',
            name='id_order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='models.order_customer'),
        ),
    ]
