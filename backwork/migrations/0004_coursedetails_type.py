# Generated by Django 5.1.4 on 2025-02-22 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backwork', '0003_coursedetails_address'),
        ('subjects', '0005_delete_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.type'),
        ),
    ]
