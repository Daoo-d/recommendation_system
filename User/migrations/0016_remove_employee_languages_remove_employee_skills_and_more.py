# Generated by Django 4.2.6 on 2024-04-06 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_employee_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
