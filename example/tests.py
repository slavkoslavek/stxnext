from django.test import TestCase
from example.models import Movie, Genre
from example.forms import MovieForm

# Create your tests here.

class SimpleTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Horror')
        self.movie = Movie.objects.create(
            name='Dracula',
            year=1987,
            released='02-11-1987',
            Genre=self.genre
        )

    def tearDown(self):
        self.movie.delete()
        self.genre.delete()

    def test_max_length(self):
        form = MovieForm(data={'name': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_initial(self):
        form = MovieForm(instance=self.movie)
        self.assertEqual(form.initial['name'], self.movie.name)