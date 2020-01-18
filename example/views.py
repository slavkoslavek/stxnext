from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from example.serializers import MovieSerializer, MovieMiniSerializer
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

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

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # filter_fields = ("name", "year", "viewed")
    authentication_classes = (TokenAuthentication,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ["name"]
    ordering_fields = ["year"]

    # def get_queryset(self):
    #     queryset = Movie.objects.filter(Genre__name='Horror')
    #     return queryset

    def get_queryset(self):
        # query_params = self.request.query_params
        queryset = self.queryset
        #
        # year = query_params.get("year")
        # viewed = query_params.get("viewed")
        #
        # if year:
        #     queryset = queryset.filter(year=year)
        #
        # if viewed:
        #     queryset = queryset.filter(viewed=viewed)

        return queryset

    # def list(self, request, *args, **kwargs):
    #     serializer = MovieMiniSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def viewed(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed = True
        instance.save()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)



