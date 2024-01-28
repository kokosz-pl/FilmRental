from django.urls import path,include, re_path
# from django.conf.urls import url
from .views import *
from AdminPortal import *
from ClientPortal import *

urlpatterns = [
    path('', home_page),
]
