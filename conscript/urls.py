
from django.contrib import admin
<<<<<<< HEAD
# from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from company import views

urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^admin/', admin.site.urls),
url(r'^company/',include('company.urls')),
url(r'^logout/$', views.user_logout, name='logout'),

]
=======
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


>>>>>>> ac98461a2ab4a74078ba9059834743969894db7b
