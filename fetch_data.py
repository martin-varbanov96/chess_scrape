# fetch_data.py
import json
import requests

class DataFetcher:
    def __init__(self, name, month, year, is_pgn=True):
        self.name = name
        self.is_pgn = is_pgn
        self.month = month
        self.year = year

    def fetch_month_games_pgn(self):
        url_to_pgn = f"https://api.chess.com/pub/player/{self.name}/games/{self.year}/{self.month}/pgn"
        r = requests.get(url_to_pgn)
        if(r.status_code == 200):
            return r.text
        else:
            print("could not obtain games from chess.com")

