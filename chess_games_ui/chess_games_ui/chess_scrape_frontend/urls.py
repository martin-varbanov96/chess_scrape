from django.urls import path, re_path
from . import views

urlpatterns = [
    path('about_us', views.about_page, name='about_page'),
    re_path(r'^all_chess_games/[0-9]+$', views.all_chess_games, name='all_chess_games'),
]