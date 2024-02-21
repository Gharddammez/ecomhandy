# Generated by Django 5.0.1 on 2024-02-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=105)),
                ('username', models.CharField(default='', max_length=100)),
                ('contact', models.IntegerField(default='')),
                ('subject', models.CharField(default='', max_length=200)),
                ('message', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
