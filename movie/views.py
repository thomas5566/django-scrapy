from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.
def home(request):
    movie = Movie.objects.all()
    return render(request, 'movies/home.html', {'movie': movie})
