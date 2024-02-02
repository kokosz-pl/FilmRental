from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('registration/',registration, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/',logout_view, name='logout'),
    path('buy_film/',buy_view, name='buy_film'),
    path('order_confirmed/', confirmed_order, name='confirmed'),
    path('purchase_list/', purchase_view, name='purchase'),
]
