from all_chess_games.models import ChessGame
from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render

def about_page(request):
    return render(request, 'about_page/about_page.html')

def all_chess_games(request):
    all_chess_games_html = 'all_games/all_chess_games.html'
    all_chess_games = ChessGame.objects.all()
    all_chess_games_size = len(all_chess_games)
    uri = str(request.path)
    page_number = int(uri.split("/")[2])

    if(page_number*20 > all_chess_games_size):
        # TODO: give 404 page
        print("*"*300)
        return render(request, "chess_scrape_frontend/404_page.html")
    else:
        games_to_show = all_chess_games[page_number*20:page_number*20+20]
        
        context = {"games_to_show": games_to_show}

        return render(request,
                    all_chess_games_html,
                    context)

