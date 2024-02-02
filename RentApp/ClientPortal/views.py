from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *


def get_film_list(request):
    user = User.objects.get(username=request.user)
    film_list = Film.objects.all()
    user_order = UserOrder.objects.all()
    film_ids = [data.film.film_id for data in user_order if data.customer.id == user.id]
    filtered_films = [film for film in film_list if film.film_id not in film_ids]
    paginator = Paginator(filtered_films, 20)
    page = request.GET.get('page', 1)
    return paginator.get_page(page)


def login(request):
    return render(request, 'ClientPortal/login.html')


def register(request):
    return render(request, 'ClientPortal/register.html')


def registration(request):
    email = request.POST['email']
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'ClientPortal/registration_error.html')

    return render(request, 'ClientPortal/registered.html')


def auth_view(request):

    if request.user.is_authenticated:
        return render(request, 'ClientPortal/film_list.html', {'film_list': get_film_list(request)})
    else:
        username = request.POST['username']
        password = request.POST['password']
        if username != "admin":
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request, 'ClientPortal/film_list.html', {'film_list': get_film_list(request)})
        
        return render(request, 'ClientPortal/login_failed.html')
    

def logout_view(request):
    auth.logout(request)
    return render(request, 'ClientPortal/login.html')


@login_required
def buy_view(request):
    id = request.POST['id']
    film = Film.objects.get(film_id = id)
    return render(request, 'ClientPortal/confirm.html', {'film_title': film.title, 'film_id': film.film_id})


@login_required
def confirmed_order(request):
    id = request.POST['id']
    film = Film.objects.get(film_id = id)
    user = User.objects.get(username=request.user)

    order = UserOrder(orders=film.title, customer=user, film=film)
    order.save()

    return render(request, 'ClientPortal/order_confirmed.html')


@login_required
def purchase_view(request):
    user_purchases = []
    user = User.objects.get(username=request.user)
    user_order = UserOrder.objects.all()
    for order in user_order:
        if order.customer.id == user.id:
            film = Film.objects.get(film_id=order.film.film_id)
            user_purchases.append((film.title, film.length))
        
    return render(request, 'ClientPortal/purchase_list.html', {'film_list': user_purchases})