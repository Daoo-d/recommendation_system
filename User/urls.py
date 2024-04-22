from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeTemplate.as_view(),name="home_page"),
    path('register',views.SignUpView.as_view(),name="register_page"),
    path('login',views.SignIn.as_view(),name="login_page"),
    path('Dashboard/<slug>',views.UserView.as_view(),name="user_page"),
    path('Analytics/<slug>',views.UserAnalytics.as_view(),name="user_Analytics_page"),
    path('portfolio/<slug>',views.employee_portfolio.as_view(),name="user_portfolio"),
    path('logout/', views.custom_logout, name='logout_page'),
    path('client_data<slug>',views.employer_Profile.as_view(),name='employer_profile'),
    path('Job/<slug>',views.job_data.as_view(),name='job_post_data'),
]
