# Generated by Django 5.2 on 2025-04-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_emailotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_two_step_verified',
            field=models.BooleanField(default=False),
        ),
    ]
