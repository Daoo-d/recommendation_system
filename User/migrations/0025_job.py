# Generated by Django 4.2.6 on 2024-04-20 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0024_employer_description_employer_industry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.CharField(choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time'), ('both', 'Both')], default='both', max_length=10)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to='User.employer')),
            ],
        ),
    ]
