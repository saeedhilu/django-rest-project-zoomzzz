# Generated by Django 5.0.4 on 2024-04-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_alter_location_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
