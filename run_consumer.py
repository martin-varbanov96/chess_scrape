from Config import *
from mysql import connector
from kafka import KafkaConsumer
from PersonalVariables import personal_variables

chess_db_connector = connector.connect(
    host=personal_variables.host_address,
    user=personal_variables.DB_USER,
    password=personal_variables.DB_PASS,
    database=personal_variables.chess_database,
)


# TODO: asert if connection to db fails
print(chess_db_connector) 
chess_db_cursor = chess_db_connector.cursor()

chess_db_cursor.execute("SHOW DATABASES")

for x in chess_db_cursor:
  print(x)
consumer = KafkaConsumer(TOPIC,
                         auto_offset_reset='earliest',
                         bootstrap_servers=[BROKER_ADDRESS],
                         api_version=(0, 10),
                         consumer_timeout_ms=1000,)
for msg in consumer:
    print(msg) 
consumer.close()