from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
#  from modeltranslation.admin import TranslationAdmin

# Register your models here.
from .models import Movie, Rating, RatingStar, MovieShots, Actor, Director, Category, Genre
# from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("categories", "name",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "movie", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
        list_display = ("name", "age", "get_image")
        readonly_fields = ("get_image",)

        def get_image(self, obj):
            return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

        get_image.short_description = "Изображение"
       # return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
        list_display = ("name", "age", "get_image")
        readonly_fields = ("get_image",)

        def get_image(self, obj):
            return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

        get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    pass
    # list_display = ("name")
    # list_display_links = ("name",)


"""
@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    Кадры из фильма
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

"""

admin.site.register(RatingStar)
