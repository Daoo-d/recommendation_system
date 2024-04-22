from django.contrib.auth.models import AbstractUser,Group,Permission
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField

special_char_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_\-!#$]*$',
    message='Only alphabets,digits and [ _, -,!,# ] characters are allowed.'
)

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50)
    city = models.CharField(max_length=100, null=False)
    dob = models.DateField(verbose_name='Date of Birth', null=False)
    country = CountryField(blank_label="(select country)", null=False)
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128,validators=[MinLengthValidator(8)])
    # username = models.CharField(max_length = 100,unique=True,validators=[special_char_validator])
    date_joined = models.DateTimeField(default=timezone.now)
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True)

    # Define related names for groups and user permissions
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate the slug from fullname and dateof_birth
            self.slug = slugify(f"{self.fullname} {self.dob}")
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.fullname}"


class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_title = models.CharField(max_length = 100,null=True)
    profile_description = models.TextField(max_length = 800,null=True)
    education = models.TextField(max_length =250,null = True)
    hourly_rate = models.IntegerField(null=True)
    profile_links = models.URLField(null=True)
    experience = models.TextField(max_length=250,null=True)
    languages = models.ManyToManyField('Language')
    skills = models.ManyToManyField('Skill')
    AVAILABILITY_CHOICES = [
        ('fulltime', 'Full-Time'),
        ('parttime', 'Part-Time'),
        ('both', 'Both'),
    ]
    availability = models.CharField(
        max_length=10,
        choices=AVAILABILITY_CHOICES,
        default='both',
    )

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return f"{self.name}"

class Skill(models.Model):
    name = models.CharField(max_length=100,unique = True)

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)   
    profile_title = models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True,null=True)
    website_url = models.URLField(blank=True,null=True)     
    industry = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return f"{self.profile_title}"

class Job(models.Model):
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE,related_name='job_postings')
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    skills = models.ManyToManyField('Skill') 
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    AVAILABILITY_CHOICES = [
        ('fulltime', 'Full-Time'),
        ('parttime', 'Part-Time'),
        ('both', 'Both'),
    ]
    availability = models.CharField(
        max_length=10,
        choices=AVAILABILITY_CHOICES,
        default='both',
    )

    def __str__(self) -> str:
        return f"{self.title}"