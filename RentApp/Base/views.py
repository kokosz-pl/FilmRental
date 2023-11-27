from django.shortcuts import render
from .models import Film

# Create your views here.
def films(request):
    film_list = Film.objects.all()
    return render(request, 'Base/film_list.html', {'film_list': film_list})