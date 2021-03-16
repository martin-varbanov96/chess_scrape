from fetch_data import DataFetcher
from load_data import DataLoader
import datetime

NAME = "funvengeance"
CHESS_GAMES = "chess_games"

class PlayerGamesScraper():
    def scrape_last_month_games(self, player_name):
        # get data for last month
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        last_month_str = lastMonth.strftime("%m")
        las_month_year_int = int(lastMonth.strftime("%Y"))

        # get games
        data_fetcher = DataFetcher(player_name)
        json_games_array = data_fetcher.get_array_chess_games(last_month_str, las_month_year_int)

        # insert games
        data_loader = DataLoader()
        data_loader.mongo_many_insert_to_collection(CHESS_GAMES, json_games_array)