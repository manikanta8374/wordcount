from django.contrib import admin
from .views import home,count,about
from django.conf.urls import url
urlpatterns = [
    url('about/', about, name='about'),
    url('count/', count, name='count'),
    url('', home,name='home'),
    
]
