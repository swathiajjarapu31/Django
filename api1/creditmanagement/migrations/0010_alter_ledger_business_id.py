# Generated by Django 3.2.10 on 2022-02-06 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0009_auto_20220206_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='business_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BID', to='creditmanagement.distributor'),
        ),
    ]