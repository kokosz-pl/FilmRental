from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Film


def login(request):
    return render(request, 'ClientPortal/login.html')


def films(request):
    # Pobierz wszystkie filmy z bazy danych
    film_list = Film.objects.all()

    # Utwórz obiekt Paginator z listą filmów i liczbą filmów na stronę (np. 10)
    paginator = Paginator(film_list, 20)

    # Pobierz numer aktualnej strony z parametru GET (jeśli nie podano, domyślnie 1)
    page = request.GET.get('page', 1)

    # Pobierz obiekt Page dla danej strony
    film_list_page = paginator.get_page(page)

    # Przekazuje film_list_page do szablonu
    return render(request, 'ClientPortal/film_list.html', {'film_list': film_list_page})