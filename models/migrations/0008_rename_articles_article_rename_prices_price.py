# Generated by Django 4.2.4 on 2023-09-05 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_prices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='articles',
            new_name='article',
        ),
        migrations.RenameModel(
            old_name='prices',
            new_name='price',
        ),
    ]
