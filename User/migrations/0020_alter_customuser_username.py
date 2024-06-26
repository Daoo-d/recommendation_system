# Generated by Django 4.2.6 on 2024-04-08 20:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Onlyalphabets,digits, _, -, @,!, and # characters are allowed.', regex='^[a-zA-Z0-9_\\-!@#$]*$')]),
        ),
    ]
