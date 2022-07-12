from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
# Create your views here.

from django.views.generic.base import View
from .forms import RatingForm, Rating


from django.http import HttpResponse
from .models import Movie, MovieShots, Actor, Director, Category, Genre


def category(request):
    return {"category_list": Category.objects.all()}


def index_page(request):
    movies = Movie.objects.all().order_by('-year')
    # movie_stars = Rating.objects.all().order_by('ip')
    return render(request, 'movies/index.html', {'movies': movies})  # 'movie_stars' : movie_stars})


def player_page(request, name):
    movie = Movie.objects.get(name=name)
    magnet_link = movie.magnet_link
    return render(request, 'movies/torrent.html', {'magnet_link': magnet_link})


def about_page(request, name):
    try:
        movie = Movie.objects.get(name=name)
    except ObjectDoesNotExist:
        return HttpResponse("Фильм не найден")
    movie_shots = MovieShots.objects.filter(title=name)
    return render(request, 'movies/about.html', {'movie': movie, 'movie_shots': movie_shots})

class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 3  # выводим 3 фильма
    def get_queryset(self):
        return Movie.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_absolute_url(self):
        return reverse('sl', kwargs={"slug": self.name})
    """
    __icontains - для того чтобы не учитывался регистр
    self.request.GET.get("q") - значение которое ввел пользователь (имя фильма)
    """
    #def get_context_data(self, *args, **kwargs):
    #    context = super().get_context_data(*args, **kwargs)
    #    context["q"] = f'{self.request.GET.get("q")}&'   # добавляем в наш словарь
    #    return context


def films_page(request):
    movies = Movie.objects.filter(films=True).order_by('-year')
    return render(request, 'movies/films.html', {'movies': movies})



def films_comedy_page(request):
    movies = Movie.objects.filter(films_comedy=True).order_by('-year')
    return render(request, 'movies/films_comedy.html', {'movies': movies})


def films_drama_page(request):
    movies = Movie.objects.filter(films_drama=True).order_by('-year')
    return render(request, 'movies/films_drama.html', {'movies': movies})


def films_horror_page(request):
    movies = Movie.objects.filter(films_horror=True).order_by('year')
    return render(request, 'movies/films_horror.html', {'movies' : movies})


def films_romance_page(request):
    movies = Movie.objects.filter(films_romance=True)
    return render(request, 'movies/films_romance.html', {'movies' : movies})


def series_page(request):
    movies = Movie.objects.filter(series=True)
    genres = Genre.objects.all()
    return render(request, 'movies/series.html', {'movies': movies, 'genres': genres})


def series_comedy_page(request):
    movies = Movie.objects.filter(series_comedy=True).order_by('year')
    return render(request, 'movies/series_comedy.html', {'movies': movies})


def series_drama_page(request):
    movies = Movie.objects.filter(series_drama=True).order_by('year')
    return render(request, 'movies/series_drama.html', {'movies': movies})


def series_horror_page(request):
    movies = Movie.objects.filter(series_horror=True).order_by('year')
    return render(request, 'movies/series_horror.html', {'movies': movies})


def series_romance_page(request):
    movies = Movie.objects.filter(series_romance=True).order_by('year')
    return render(request, 'movies/series_romance.html', {'movies': movies})


def cartoons_page(request):
    movies = Movie.objects.filter(cartoons=True).order_by('year')
    genres = Genre.objects.all()
    return render(request, 'movies/cartoons.html', {'movies': movies, 'genres': genres})


def cartoons_science_fiction_page(request):
    movies = Movie.objects.filter(science_fiction=True).order_by('year')
    return render(request, 'movies/cartoons_science_fiction.html', {'movies': movies})


def cartoons_mystery_page(request):
    movies = Movie.objects.filter(mystery=True).order_by('year')
    return render(request, 'movies/cartoons_mystery.html', {'movies': movies})


def cartoons_anime_page(request):
    movies = Movie.objects.filter(anime=True).order_by('year')
    return render(request, 'movies/cartoons_anime.html', {'movies': movies})


def admin(request):
    return render(request, 'movies/admin.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ActorView(DetailView):
    """Вывод информации о актере"""
    model = Actor
    template_name = 'movies/about_actor.html'
    slug_field = "name"


class DirectorView(DetailView):
    model = Director
    template_name = 'movies/about_director.html'
    slug_field = "name"


class CategoryView(DetailView):
    model = Category
    template_name = 'movies/<str:slug>/.html'
    slug_field = "name"



"""    Измениния   """
"""
class AddReview(View):
Отзывы

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
"""

class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


