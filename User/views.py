from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View
from django.http import HttpResponseRedirect
from .Form import SignUp,portfolio_data
from .models import Employee,Employer,CustomUser
from django.contrib.auth.views import LoginView

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
        form = SignUp(request.POST)
        if form.is_valid() and user_type:
            user = form.save(commit=False)
            if user_type=="isEmployee":
                user.is_employee = True
                user.save()
                profile = Employee.objects.create(user=user)
                return HttpResponseRedirect("login")
            elif user_type == "isEmployer":
                user.is_employer = True  
                user.save()
                profile = Employer.objects.create(user=user)
                return HttpResponseRedirect("login")
        return render(request,"User/Register.html",{
                "form":form
                })    

class SignIn(View):
    def get(self,request):
        return render(request,"User/login.html")
    def post(self,request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = CustomUser.objects.get(email=email, password=password)
                if user.is_employee:
                    return render(request, "User/employeeDashboard.html", {'user': user})
                elif user.is_employer:
                    return render(request, "User/home.html", {'user': user})
            except CustomUser.DoesNotExist:
                return render(request, "User/login.html")
        else:
            # Handle form validation errors (if any)
            return render(request, "User/login.html")    

class EmployeeView(TemplateView):
    template_name = "User/employeeDashboard.html" 
class Employee_Analytics(TemplateView):
    template_name = "User/employeeAnalytics.html"  
class employee_portfolio(View):
    def get(self,request):
        form = portfolio_data()
        return render(request,"User/potfolio_data.html",{
            'form':form
        })
