from django.urls import path, re_path
from . import views

urlpatterns = [
    path('about_us', views.about_page, name='about_page'),
    path('all_chess_games/<int:page_number>', views.all_chess_games, name='all_chess_games'),
]