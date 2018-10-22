
from django.conf.urls import url
from company import views
from django.urls import path
# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^admin_dashboard/$',views.admin_dashboard,name='admin_dashboard'),
    url(r'^interview_list/$',views.interview_list,name='interview_list'),
    url(r'^invite/$',views.invite,name='invite'),
    url(r'^domains/$',views.domains,name='domains'),
]

