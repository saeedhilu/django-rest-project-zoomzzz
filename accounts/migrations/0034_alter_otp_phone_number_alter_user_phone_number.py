# Generated by Django 5.0.4 on 2024-04-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_alter_otp_phone_number_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]