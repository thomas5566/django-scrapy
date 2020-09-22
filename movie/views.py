from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
from .filters import MovieFilter

# Create your views here.


def home(request):
    all_rows = Movie.objects.all().order_by('date').reverse()
    movie = [all_rows.filter(title=item['title']).last(
    ) for item in Movie.objects.values('title').distinct().order_by('date').reverse()]

    # movieFilter = MovieFilter(request.GET, queryset=movie)

    # if request.method == "POST":
    #     movieFilter = MovieFilter(request.POST, queryset=movie)

    context = {
        'movie': movie
    }
    # movie = Movie.objects.all().order_by('date').reverse()
    return render(request, 'movies/home.html', context)
