# Generated by Django 4.2.4 on 2023-09-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_rename_articles_article_rename_prices_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'customer',
                'ordering': ['id'],
            },
        ),
    ]
