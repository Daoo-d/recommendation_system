# Generated by Django 4.2.6 on 2024-04-03 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_skill_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user_skills',
        ),
    ]
