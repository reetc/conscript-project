
from django.conf.urls import url
from company import views
from django.urls import path
# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^candidate_list/$',views.candidate_list,name='candidate_list'),
    url(r'^interview_list/$',views.interview_list,name='interview_list'),
]
