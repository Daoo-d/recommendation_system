# Generated by Django 4.2.6 on 2024-04-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_remove_employee_user_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='User.skill'),
        ),
    ]
