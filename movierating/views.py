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
    rater = Rater.objects.get(id=rater_id)
    MovieRating.objects.filter(rater__id=rater_id)
    movies = list(Movie.objects.filter(movierating__rater=rater_id))
    context = {
            "rater": (Rater.objects.get(id=rater_id)),
            "movies_rated": (MovieRating.objects.filter(rater=rater_id)),
            "movies_count": (MovieRating.objects.filter(rater=rater_id).count()),
            "movies": (Movie.objects.filter(movierating__rater=rater_id))
             }
    return render(request, "raterpage.html", context)


# def viewer_movies(request, rater_id):
#    # context = {
#            # "rater = Rater.objects.get(id=rater_id)",
#            # "movies": (MovieRating.objects.filter(rater=rater)),
#            #"movies": (Movie.objects.filter(movie=MovieRating.movie).filter(MovieRating.objects.filter(rater=rater))),
#            }
#    # return render(request, 'raterpage.html', context)


def view_movie(request, movie_id):
    from django.db.models import Avg
    movie = Movie.objects.get(id=movie_id)
    raters = list(Rater.objects.filter(movierating__movie=movie_id))
    context = {
            "movie": (Movie.objects.get(id=movie_id)),
            "ratings_list": (MovieRating.objects.filter(movie=movie_id)),
            "ratings_count": (MovieRating.objects.filter(movie=movie_id).count()),
            "ratings_avg": (MovieRating.objects.filter(movie=movie_id).aggregate(Avg("rating")))
            }
    return render(request, "movie.html", context)


def top_movies(request):
    from django.db.models import Avg
    movies = Movie
    context = {
            "movieratings": (MovieRating.objects.filter(movie=movies.id).aggregate(Avg('rating')))
            }
    return render(request, "topmovies.html", context)
