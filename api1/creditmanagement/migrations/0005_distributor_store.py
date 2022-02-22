# Generated by Django 3.2.10 on 2022-02-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanagement', '0004_alter_ledgertransactions_transaction_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_id', models.CharField(max_length=100, null=True)),
                ('tenant_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(max_length=100, null=True)),
                ('tenant_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('distributor_id', models.ManyToManyField(null=True, related_name='Store', to='creditmanagement.distributor')),
            ],
        ),
    ]
