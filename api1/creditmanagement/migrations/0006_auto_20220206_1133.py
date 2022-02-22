# Generated by Django 3.2.10 on 2022-02-06 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0005_distributor_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='business_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditmanagement.distributor'),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ledger', to='creditmanagement.store'),
        ),
        migrations.AlterUniqueTogether(
            name='ledger',
            unique_together=set(),
        ),
    ]