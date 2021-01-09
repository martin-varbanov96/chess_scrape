from fetch_data import DataFetcher
from kafka import KafkaProducer, KafkaConsumer
from ChessGamesProducer import ChessGamesProducer
from Config import *

# data_fetcher = DataFetcher("funvengeance", 12, 2020,)
# pgn_data = data_fetcher.fetch_month_games_pgn()


data = [i for i in range(0, 100)]
chess_games_producer = ChessGamesProducer(BROKER_ADDRESS)
chess_games_producer.connect_kafka_producer()
for el in data:
    chess_games_producer.publish_message(TOPIC, str(el))
chess_games_producer.close()

consumer = KafkaConsumer(TOPIC,
                         auto_offset_reset='earliest',
                         bootstrap_servers=[BROKER_ADDRESS],
                         api_version=(0, 10),
                         consumer_timeout_ms=1000,)
for msg in consumer:
    print(msg.value.decode())
consumer.close()