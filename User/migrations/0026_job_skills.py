# Generated by Django 4.2.6 on 2024-04-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='User.skill'),
        ),
    ]
