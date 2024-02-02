from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', auth_view, name='auth'),
    path('logout/',logout_view, name='logout'),
    path('add_film_form/', add_film_view, name='add_film'),
    path('delete/', delete, name='delete'),
    path('add_film/', film_added_view, name='film_added'),
    ]
