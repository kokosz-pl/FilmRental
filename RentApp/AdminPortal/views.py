from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Film


def get_film_list(request):
    film_list = Film.objects.all()
    paginator = Paginator(film_list, 20)
    page = request.GET.get('page', 1)
    return paginator.get_page(page)


def login(request):
    return render(request, 'AdminPortal/login.html')


def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'AdminPortal/film_list.html', {'film_list': get_film_list(request)})
    else:
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin" and password == "admin":
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request, 'AdminPortal/film_list.html', {'film_list': get_film_list(request)})
        else: 
            return render(request, 'AdminPortal/login_failed.html')
    

def logout_view(request):
    auth.logout(request)
    return render(request, 'AdminPortal/login.html')


def add_film_view(request):
    return render(request, 'AdminPortal/add_film.html')


@login_required
def film_added_view(request):
    title = request.POST['title']
    description = request.POST['description']
    release_year = request.POST['release_year']
    rental_rate = request.POST['rental_rate']
    length = request.POST['length']
    rating = request.POST['rating']

    try:
        film = Film(title = title, description=description, release_year=release_year, rental_rate=rental_rate, length=length, rating=rating)
        film.save()
    except:
        return render(request, 'AdminPortal/wrong_data.html')

    return render(request, 'AdminPortal/film_added.html')

@login_required
def delete(request):
    film_id = request.POST['id']
    film = Film.objects.get(film_id = film_id)
    film.delete()
    return render(request, 'AdminPortal/deleted.html')


