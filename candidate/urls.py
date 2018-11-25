from django.urls import path
from candidate import views
from django.conf.urls import url


urlpatterns = [

    url(r'canhomepage/$', views.canhomepage, name="canhome"),
    url(r'sendComp/(\S+)$', views.sendComp, name="sendComp"),
    url(r'^login/$', views.login_blog, name="can_login"),
    url(r'^register/$', views.register, name="can_register"),
    url(r'^logout/$', views.logout_blog, name="can_logout"),
    url(r'^questions/$', views.questions, name="questions"),
#    url(r'^webcam/$', views.webcam, name="webcam"),
    
    ]
