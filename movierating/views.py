from django.shortcuts import render
from movierating.models import Rater
from movierating.models import Movie
from movierating.models import MovieRating

# Create your views here.


def view_index(request):
    return render(request, "index.html")


def view_movies(request):
    context = {
            "movies_list": (Movie.objects.all())
            }
    return render(request, "movies.html", context)


def view_raters(request):
    context = {
            "raters_list": (Rater.objects.all())
            }
    return render(request, "raters.html", context)
