from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}!")

# def hello_world_template(request):
#     movies = Movie.objects.all()
#     return render(request, "index.html", {'movies':movies})

def hello_world_template(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {'test':movies})

class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'
    context_object_name = "genres"

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    success_url = "../genre_list"
    template_name = "genre_add.html"

class GenreDeleteView(DeleteView):
    model = Genre
    success_url = "../../genre_list"
    template_name = "genre_add.html"

class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie_list"
    template_name = "movie_add.html"

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie_list"
    template_name = 'movie_add.html'

class MovieDeleteView(DeleteView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie_list"
    template_name = 'movie_add.html'

class MovieDetailsView(DetailView):
    model = Movie
    template_name = 'movie_details.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        a_obj = Movie.objects.get(name__icontains=slug)
        return a_obj



