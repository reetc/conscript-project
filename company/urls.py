from django.urls import path
from . import views

urlpatterns = [

    path('', views.comhomepage, name="comhome"),
    ]
