from django.urls import path
from candidate import views
from django.conf.urls import url


urlpatterns = [

    path('', views.canhomepage, name="canhome"),
    url(r'sendComp/(\S+)$', views.sendComp, name="sendComp"),
    url(r'^login/$', views.login_blog),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout_blog),
    
    ]
