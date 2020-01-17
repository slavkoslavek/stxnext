from django import forms
from example.models import Movie, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = {"created_on",}

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'