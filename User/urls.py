from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeTemplate.as_view(),name="home_page"),
    path('register',views.SignUpView.as_view(),name="register_page"),
    path('login',views.SignIn.as_view(),name="login_page"),
    path('Employee',views.EmployeeView.as_view(),name="employee_page"),
    path('employee_analatics',views.Employee_Analytics.as_view(),name="employee_Analytics_page")
]
