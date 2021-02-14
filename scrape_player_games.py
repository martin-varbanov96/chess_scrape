from fetch_data import DataFetcher
from load_data import DataLoader

NAME = "funvengeance"
CHESS_GAMES = "chess_games"

# get games
data_fetcher = DataFetcher(NAME)
json_games_array = data_fetcher.get_array_chess_games("01", 2021)

# insert games
data_loader = DataLoader()
data_loader.mongo_many_insert_to_collection(CHESS_GAMES, json_games_array)