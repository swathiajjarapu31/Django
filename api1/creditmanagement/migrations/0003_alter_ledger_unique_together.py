# Generated by Django 3.2.5 on 2022-01-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0002_auto_20220118_1728'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ledger',
            unique_together={('company_id', 'business_id', 'customer_id')},
        ),
    ]