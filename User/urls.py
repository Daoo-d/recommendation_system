from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeTemplate.as_view(),name="home_page"),
    path('register',views.SignUpView.as_view(),name="register_page"),
    path('login',views.SignIn.as_view(),name="login_page"),
    path('Employee/<slug>',views.EmployeeView.as_view(),name="employee_page"),
    path('employee_analytics/<slug>',views.Employee_Analytics.as_view(),name="employee_Analytics_page"),
    path('portfolio/<slug>',views.employee_portfolio.as_view(),name="user_portfolio"),
   path('logout/', LogoutView.as_view(next_page='login_page'), name='logout_page')
]
