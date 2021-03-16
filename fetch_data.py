# fetch_data.py
import json
import requests

class DataFetcher:
    def __init__(self, name, is_pgn=True):
        self.name = name
        self.is_pgn = is_pgn

    def fetch_month_games_pgn(self, month, year):
        url_to_pgn = f"https://api.chess.com/pub/player/{self.name}/games/{year}/{month}/pgn"
        r = requests.get(url_to_pgn)
        if(r.status_code == 200):
            return r.text
        else:
            print("could not obtain games from chess.com")

    def fetch_month_games_json(self, month, year):
        url_to_pgn = f"https://api.chess.com/pub/player/{self.name}/games/{year}/{month}"
        r = requests.get(url_to_pgn)
        if(r.status_code == 200):
            return r.text
        else:
            print(f"could not obtain games from chess.com. \n Status: {r.status_code}")

    
    def get_array_chess_games(self, month, year):
        raw_string = self.fetch_month_games_json(month, year)
        json_result = json.loads(raw_string)
        return json_result["games"]


