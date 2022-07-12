from django.db import models
from django.urls import reverse


class Actor(models.Model):
    """Актеры"""
    name = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    career = models.CharField("Карьера", max_length=40)
    growth = models.IntegerField("Рост", default=0)
    birthday = models.IntegerField("День рождения", default=0)
    month = models.CharField("Месяц рождения",  max_length=10)
    year = models.IntegerField("Год рождения", default=0)
    place = models.CharField("Место рождения", max_length=20)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    genres = models.CharField("Жанры",  max_length=30)
    spouse = models.CharField("Супруг",  max_length=30)
    total_movies = models.CharField("Всего фильмов",  max_length=50)
    image = models.ImageField("Изображение", upload_to='actors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актера"
        verbose_name_plural = "Актеры"


class Director(models.Model):
    """режиссеры"""
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    career = models.TextField("Карьера", max_length=100)
    growth = models.IntegerField("Рост", default=0)
    birthday = models.IntegerField("День рождения", default=0)
    month = models.TextField("Месяц рождения")
    year = models.IntegerField("Год рождения", default=0)
    place = models.TextField("Место рождения", default=0)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    genres = models.TextField("Жанры")
    spouse = models.TextField("Супруг")
    total_movies = models.TextField("Всего фильмов")
    image = models.ImageField("Изображение", upload_to='actors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('director_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Режиссера"
        verbose_name_plural = "Режиссеры"


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    # description = models.TextField("Описание")
    # url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    name = models.CharField("Название жанра", max_length=100)

    def __str__(self):
        return f"{self.categories} - {self.name}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    name = models.CharField("Название фильма", max_length=100)
    country = models.CharField("Страна", max_length=100)
    description = models.TextField("Описание", max_length=5000)
    image = models.ImageField("Изображение", upload_to='movie')

    category = models.ManyToManyField(Actor, verbose_name="Категория фильма", related_name="category")
        # = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категории")

    films = models.BooleanField("Фильм", default=False, help_text="Выберите жанр фильма, который добавляете на сайт")
    films_comedy = models.BooleanField("Жанр - комедия", default=False)
    films_drama = models.BooleanField("Жанр - драма", default=False)
    films_horror = models.BooleanField("Жанр - ужасы", default=False)
    films_romance = models.BooleanField("Жанр - мелодрамма", default=False)

    series = models.BooleanField("Сериал", default=False, help_text="Выберите жанр сериала, который добавляете на сайт")
    series_comedy = models.BooleanField("Жанр - комедия", default=False)
    series_drama = models.BooleanField("Жанр - драма", default=False)
    series_horror = models.BooleanField("Жанр - ужасы", default=False)
    series_romance = models.BooleanField("Жанр - мелодрамма", default=False)
    cartoons = models.BooleanField("Мультфильм", default=False, help_text="Выберите жанр мультфильма,"
                                                                          " который добавляете на сайт")
    mystery = models.BooleanField("Жанр - мистика", default=False)
    science_fiction = models.BooleanField("Жанр - фантастика", default=False)
    anime = models.BooleanField("Жанр - аниме", default=False)
    magnet_link = models.TextField("Введите магнет ссылку", default=False)
    year = models.IntegerField("Введите год премьеры", null=False)
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    director = models.ManyToManyField(Director, verbose_name="режисеры", related_name="film_director")

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Название фильма", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots")
    # movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

"""
class MovieShots(models.Model):
    Кадры из фильма
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"
"""


"""
class Reviews(models.Model):
    Отзывы
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
"""


