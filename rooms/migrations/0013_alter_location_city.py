# Generated by Django 5.0.4 on 2024-04-18 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_alter_location_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='rooms.city'),
        ),
    ]