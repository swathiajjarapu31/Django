# Generated by Django 3.2.10 on 2022-02-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0012_alter_ledger_business_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='company_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
