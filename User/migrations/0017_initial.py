# Generated by Django 4.2.6 on 2024-04-07 20:10

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('User', '0016_remove_employee_languages_remove_employee_skills_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('groups', models.ManyToManyField(related_name='custom_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_users_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_title', models.CharField(max_length=100, null=True)),
                ('profile_description', models.TextField(max_length=800, null=True)),
                ('education', models.TextField(max_length=250, null=True)),
                ('hourly_rate', models.IntegerField(null=True)),
                ('profile_links', models.URLField(null=True)),
                ('experience', models.TextField(max_length=250, null=True)),
                ('availability', models.CharField(choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time'), ('both', 'Both')], default='both', max_length=10)),
                ('languages', models.ManyToManyField(to='User.language')),
                ('skills', models.ManyToManyField(to='User.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.customuser')),
            ],
        ),
    ]
