from django.urls import path
from basic_app import views
from django.urls import include, re_path

#for template tagging, set app name, to look here and find url that matches, this is what is called from html template
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$',views.relative,name='relative'),
    re_path(r'^other/$',views.other,name='other')
]
