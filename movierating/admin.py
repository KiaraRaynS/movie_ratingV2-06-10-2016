from django.contrib import admin
from movierating.models import Rater
from movierating.models import Movie
from movierating.models import MovieRating

# Register your models here.

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(MovieRating)
