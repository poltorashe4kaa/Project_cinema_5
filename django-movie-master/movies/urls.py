from django.urls import path, include
from . import views
from . import models


urlpatterns = [
    path('', views.index_page, name='home'),
    path('watching_a_movie <name>', views.player_page, name='watching_a_movie'),
    path('detailed_description <name>', views.about_page, name='подробнее'),
    path('films', views.films_page, name='films'),
    path('films_comedy', views.films_comedy_page, name='films_comedy'),
    path('films_drama', views.films_drama_page, name='films_drama'),
    path('films_horror', views.films_horror_page, name='films_horror'),
    path('films_romance', views.films_romance_page, name='films_romance'),
    path('series_comedy', views.series_comedy_page, name='series_comedy'),
    path('series_drama', views.series_drama_page, name='series_drama'),
    path('series_horror', views.series_horror_page, name='series_horror'),
    path('series_romance', views.series_romance_page, name='series_romance'),
    path('cartoons_mystery', views.cartoons_mystery_page, name='cartoons_mystery'),
    path('cartoons_anime', views.cartoons_anime_page, name='anime_drama'),
    path('cartoons_science_fiction', views.cartoons_science_fiction_page, name='cartoons_science_fiction'),
    path('series', views.series_page, name='series'),
    path('cartoons', views.cartoons_page, name='cartoons'),
    path('admin', views.admin, name='admin'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    # path("about_actor <name>", views.ActorView.as_view(), name="actor_detail"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    path("director/<str:slug>/", views.DirectorView.as_view(), name="director_detail"),
    path('detailed_description ', views.Search.as_view(), name='detailed_description '),

]
