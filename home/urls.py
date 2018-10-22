from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name="home"),
    path('about-us/', views.aboutpage, name="about-us"),
    path('portal/', views.portal, name="portal"),
    path('contact-us/', views.contactpage, name="contact-us"),
    path('blog/', views.blog, name="blog"),
    ]
