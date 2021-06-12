from django.urls import path

from . import views

urlpatterns = [
    path('about_us', views.about_page, name='about_page'),
    path('all_chess_games', views.all_chess_games, name='all_chess_games'),
]