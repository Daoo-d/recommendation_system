from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from User.auth_backends import EmailBackend
from django.views.generic import TemplateView,View
from django.http import HttpResponseRedirect,HttpResponse
from .Form import SignUp,portfolio_data
from .models import Employee,Employer,CustomUser,Skill,Language
# from django.contrib.auth.views import LoginView

# Create your views here.
class HomeTemplate(TemplateView):
    template_name = "User/home.html"
class SignUpView(View):
    def get(self,request):
        form = SignUp()
        return render(request,"User/Register.html",{
            "form" : form
        })
    def post(self,request):
        user_type = self.request.POST.get('user_type')
        print(user_type)
        form = SignUp(request.POST)
        if form.is_valid() and user_type:
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            print(user.username )
            user.set_password(form.cleaned_data['password'])
            if user_type=="isEmployee":
                user.is_employee = True
                user.save()
                Employee.objects.create(user=user)
                return HttpResponse("Success")
            elif user_type == "isEmployer":
                user.is_employer = True  
                user.save()
                Employer.objects.create(user=user)
                return HttpResponse("Success")
        print(form.errors)    
        return render(request,"User/Register.html",{
                "form":form
                })    
        
class SignIn(View):
    def get(self,request):
        return render(request,"User/login.html")
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request,username=username, password=password)
        print(user.is_authenticated)
        if user is not None:
        # User is authenticated, log them in
            login(request, user)
            if user.is_employee:
                return redirect("employee_page", slug=user.slug)
            elif user.is_employer:
                return render(request, "User/home.html", {'user': user})
        else:
            return render(request, "User/login.html")    

class EmployeeView(View):
    def get(self,request,slug):
        user = CustomUser.objects.get(slug=slug)
        return render(request,"User/employeeDashboard.html", {'user': user})
  
class Employee_Analytics(View):
    def get(self,request,slug):
        user = CustomUser.objects.get(slug=slug)
        return render(request,"User/employeeAnalytics.html", {'user': user})
def save_skills(employee, skills):
        for skill_name in skills:
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            employee.skills.add(skill)

class employee_portfolio(View):
    
    def get(self,request,slug):
        form = portfolio_data()
        user = CustomUser.objects.get(slug=slug)
        return render(request,"User/portfolio_data.html",{
            'form':form,
            'user':user
        })
    def post(self,request,slug):
        form = portfolio_data(request.POST)
        user = CustomUser.objects.get(slug=slug)
        if form.is_valid():
            print("helloworld")
            employee = Employee.objects.get(user=user)
            employee.profile_title = form.cleaned_data['profile_title']
            
            employee.profile_description = form.cleaned_data['profile_description']
            employee.education = form.cleaned_data['education']
            employee.hourly_rate = form.cleaned_data['hourly_rate']
            employee.profile_links = form.cleaned_data['profile_links']
            employee.experience = form.cleaned_data['experience']
            employee.availability = form.cleaned_data['availability']
            employee.languages.set(form.cleaned_data['languages'])
            selected_skill = form.cleaned_data['user_s']
            selected_skill_list = selected_skill.split(',')
            save_skills(employee,selected_skill_list)
            
            employee.save()
            print(selected_skill_list)
            return HttpResponseRedirect("login")
        return render(request,"User/portfolio_data.html",{
            'form':form,
            'user':user
        })
            