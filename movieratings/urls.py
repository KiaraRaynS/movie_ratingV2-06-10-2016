"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# view list of class pages
from movierating.views import view_index, view_movies, view_raters
# view instance of class page
from movierating.views import view_rater, view_movie
from movierating.views import top_movies

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view_index, name='index'),
    url(r'movies/$', view_movies),
    url(r'^raters/$', view_raters),
    url(r'^toplist/$', top_movies),
    url(r'^raters/(?P<rater_id>\w+)/$', view_rater),
    url(r'^movies/(?P<movie_id>\w+)/$', view_movie),
]
