from django.contrib import admin
from .models import Skill,Employee,CustomUser,Language,Employer,Job

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("username","dob",)}

admin.site.register(Skill)
admin.site.register(Employee)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Language)
admin.site.register(Employer)
admin.site.register(Job)
