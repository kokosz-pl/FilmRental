from django.urls import path
from django.contrib.auth import views as auth_views
from .views import films
from .views import login

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('films/', films, name='films'),
    # Dodaj inne ścieżki...
]
