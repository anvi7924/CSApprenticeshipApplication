from django.conf.urls import url
from . import views
from . import forms
from django.contrib.auth import views as v

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^add_project/$', views.add_project, name='add_project'),
        url(r'^studentform/$', views.studentform, name='studentform'),
        url(r'^projectlist/$', views.projectlist, name='projectlist'),
        url(r'^projectlist/(\w+)/$', views.projectlist, name='project'),
        url(r'^staffpage/$', views.staffpage, name='staffpage'),
        url(r'^staffpage/(\w+)/$', views.staffpage, name='projmatrix'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^about/$', views.about, name='about'),
        ]
