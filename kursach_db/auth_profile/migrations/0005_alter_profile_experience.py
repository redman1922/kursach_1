# Generated by Django 4.0.6 on 2023-05-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_profile', '0004_alter_profile_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.BooleanField(default=False),
        ),
    ]
