
from django.conf.urls import url
from company import views
from django.urls import path
# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^admin_dashboard/$',views.admin_dashboard,name='admin_dashboard'),
    url(r'^admin_dashboard/analysis$',views.analysis,name='analysis'),
    url(r'^interview_list/$',views.interview_list,name='interview_list'),
    url(r'^invite/$',views.invite,name='invite'),
    url(r'^domains/$',views.domains,name='domains'),
    url(r'^com_login/$', views.com_login, name="com_login"),
    url(r'^register/$',views.register_company,name='register_company'),
    url(r'^results/$',views.display_results,name='display_results'),
    url(r'applications_list/$', views.applications_list, name="applications_list"),
    url(r'application_result/(\S+)$', views.application_result, name="applicantion_result"),


]
