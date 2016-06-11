from django.shortcuts import render
from movierating.models import Rater
from movierating.models import Movie
from movierating.models import MovieRating

# Create your views here.


def view_index(request):
    return render(request, "index.html")

# View class lists


def view_movies(request):
    context = {
            "movies_list": (Movie.objects.all())
            }
    return render(request, "movies.html", context)


def view_raters(request):
    context = {
            "raters_list": (Rater.objects.all()),
            }
    return render(request, "raters.html", context)

# View singular class instances


def view_rater(request, rater_id):
    context = {
            "rater": (Rater.objects.filter(id=rater_id)),
            "movies_rated": (MovieRating.objects.filter(rater=rater_id)),
            "moviedata": (Movie.objects.filter(id=MovieRating.movie).filter(rater=rater_id))
            }
    return render(request, "raterpage.html", context)
