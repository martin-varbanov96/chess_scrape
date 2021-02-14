from fetch_data import DataFetcher
from kafka import KafkaProducer, KafkaConsumer
from ChessGamesProducer import ChessGamesProducer
from Config import *
import json
from mysql import connector
from PersonalVariables import personal_variables

data_fetcher = DataFetcher(personal_variables.ches_com_username)
json_games_array = data_fetcher.get_array_chess_games(12, 2020)


chess_games_producer = ChessGamesProducer(BROKER_ADDRESS)
chess_games_producer.connect_kafka_producer()
for json_game in json_games_array:
    chess_games_producer.publish_json_message(TOPIC, json_game)
chess_games_producer.close()


# chess_db_connector = connector.connect(
#     host=personal_variables.host_address,
#     user=personal_variables.DB_USER,
#     password=personal_variables.DB_PASS,
#     database=personal_variables.chess_database,
# )

# # TODO: asert if connection to db fails
# print(chess_db_connector)
# chess_db_cursor = chess_db_connector.cursor()

# chess_db_cursor.execute("SHOW DATABASES")

# for x in chess_db_cursor:
#   print(x)