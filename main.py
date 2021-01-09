from fetch_data import DataFetcher
from kafka import KafkaProducer, KafkaConsumer
from ChessGamesProducer import ChessGamesProducer


# data_fetcher = DataFetcher("funvengeance", 12, 2020,)
# pgn_data = data_fetcher.fetch_month_games_pgn()

data = [i for i in range(0, 100)]
chess_games_producer = ChessGamesProducer("localhost:9092")
chess_games_producer.connect_kafka_producer()
for el in data:
    chess_games_producer.publish_message("python_topic", str(el))
chess_games_producer.close()