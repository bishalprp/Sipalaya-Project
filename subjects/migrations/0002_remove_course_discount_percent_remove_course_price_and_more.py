# Generated by Django 5.1.4 on 2025-01-31 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Discount_percent',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Real_price',
        ),
        migrations.RemoveField(
            model_name='field',
            name='number',
        ),
        migrations.AddField(
            model_name='course',
            name='Location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
