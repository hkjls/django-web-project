# Generated by Django 4.2.4 on 2023-09-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_delivery_customer_invoice_customer_order_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Ref', models.CharField(max_length=125)),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='invoice_supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Ref', models.CharField(max_length=125)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='order_supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Ref', models.CharField(max_length=125)),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='payment_supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=125)),
                ('code', models.CharField(max_length=125)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'supplier',
                'ordering': ['id'],
            },
        ),
    ]