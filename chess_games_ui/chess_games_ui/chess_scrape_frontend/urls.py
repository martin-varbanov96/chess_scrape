from django.urls import path, re_path
from . import views

urlpatterns = [
    path('about_us', views.about_page, name='about_page'),
    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('all_chess_games/<int:page_number>', views.all_chess_games, name='all_chess_games'),
]