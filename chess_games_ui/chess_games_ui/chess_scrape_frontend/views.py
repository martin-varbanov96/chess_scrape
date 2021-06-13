#system imports:
from math import ceil

# user imports:
from all_chess_games.models import ChessGame

# django imports:
from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render

def about_page(request):
    return render(request, 'about_page/about_page.html')

def all_chess_games(request, page_number):

    all_chess_games_html = 'all_games/all_chess_games.html'
    all_chess_games = ChessGame.objects.all()
    all_chess_games_size = len(all_chess_games)
    uri = str(request.path)
    #page_number = int(uri.split("/")[2])
    entries_per_page = 20
    final_page = ceil(all_chess_games_size / entries_per_page)
    first_entry_to_show = page_number*entries_per_page
    last_entry_to_show = page_number*entries_per_page + entries_per_page
    games_to_show = []

    # page out of limits
    if(first_entry_to_show > all_chess_games_size):
        return render(request, "chess_scrape_frontend/404_page.html")
    # TODO: test last page
    # list all of the page on the last page
    elif(first_entry_to_show > all_chess_games_size):
        games_to_show = all_chess_games[first_entry_to_show:]
    else:
        games_to_show = all_chess_games[first_entry_to_show:last_entry_to_show]
    context = {"games_to_show": games_to_show,
                "current_page": page_number,
                "final_page": final_page,
                }
    return render(request,
                    all_chess_games_html,
                    context)

