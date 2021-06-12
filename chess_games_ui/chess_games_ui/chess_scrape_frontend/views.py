from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def about_page(request):
    return render(request, 'about_page/about_page.html')

def all_chess_games(request):
    return render(request, 'about_page/all_chess_games.html')

