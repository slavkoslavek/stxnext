"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example.views import hello_world, hello_name, hello_world_template, MovieListView, GenreListView, MovieCreateView, \
    MovieUpdateView, MovieDeleteView, GenreCreateView, GenreDeleteView, MovieDetailsView


urlpatterns = [
    path('', MovieListView.as_view()),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path("hello/<str:name>/", hello_name),
    path("movies/", hello_world_template),
    path("movie_list/", MovieListView.as_view(), name= 'movie_list'),
    path("genre_list/", GenreListView.as_view(), name= 'genre_list'),
    path("movie_add/", MovieCreateView.as_view(), name='movie_add'),
    path('movie/update/<int:pk>', MovieUpdateView.as_view(), name="movie_edit"),
    path('movie/delete/<int:pk>', MovieDeleteView.as_view(), name="movie_delete"),
    path('<slug:slug>/', MovieDetailsView.as_view(), name='movie_details'),
    path("genre/add", GenreCreateView.as_view(), name = 'genre_add'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name="genre_delete")
]
