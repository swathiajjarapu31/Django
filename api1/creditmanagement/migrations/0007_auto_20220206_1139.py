# Generated by Django 3.2.10 on 2022-02-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0006_auto_20220206_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='business_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='customer_id',
            field=models.CharField(max_length=100),
        ),
    ]
