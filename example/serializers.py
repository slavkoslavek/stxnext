from rest_framework import serializers

from example.models import Movie, Genre



class GenreSerializer(serializers.ModelSerializer):

    """Serializing all the Genre"""

    class Meta:
        model = Genre
        fields = {"id", "name", "viewed"}

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Movie
        Genre = GenreSerializer()
        fields = ("id", "name", "year", "released", "Genre")

class MovieMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "name", "viewed", "year")