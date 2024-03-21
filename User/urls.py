from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeTemplate.as_view())
]
