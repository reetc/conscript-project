from django.urls import path
from candidate import views
from django.conf.urls import url


urlpatterns = [

    path('', views.canhomepage, name="canhome"),
    url(r'sendComp/(\S+)$', views.sendComp, name="sendComp"),

    ]
