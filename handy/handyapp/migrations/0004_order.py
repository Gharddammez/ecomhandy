# Generated by Django 5.0.1 on 2024-02-29 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handyapp', '0003_alter_contact_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=100)),
                ('customer', models.CharField(default='', max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=13)),
                ('cost', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
