# Generated by Django 3.0 on 2020-11-04 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100, verbose_name='Street')),
                ('apartment_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apartment')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=14, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=14, null=True, verbose_name='Fax')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_set', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': "Address's",
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_address', to='address.Address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'ShippingAddress',
                'verbose_name_plural': "ShippingAddress's",
            },
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='address.Address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'BillingAddress',
                'verbose_name_plural': "BillingAddress's",
            },
        ),
    ]
