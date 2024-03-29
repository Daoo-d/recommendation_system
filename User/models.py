from django.db import models
from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField


class CustomUser(models.Model):
    fullname = models.CharField(max_length=50)
    city = models.CharField(max_length = 100,null=False)
    dob = models.DateField(verbose_name='Date of Birth',null=False)
    country = CountryField(blank_label="(select country)",null=False)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100,validators=[MinLengthValidator(8,message="Password must be at least8 digits")])
    is_employee = models.BooleanField(default = False)
    is_employer = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f"{self.fullname}"

class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_title = models.CharField(max_length = 100,null=True)
    profile_description = models.TextField(max_length = 800,null=True)
    education = models.TextField(max_length =250,null = True)
    hourly_rate = models.IntegerField(null=True)
    profile_links = models.URLField(null=True)
    

class Employer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)        