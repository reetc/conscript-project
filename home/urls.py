from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name="home"),
    path('about-us/', views.aboutpage, name="about-us"),
    ]
