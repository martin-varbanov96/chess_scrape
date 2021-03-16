# ChessGamesProducer.py
import json
from kafka import KafkaProducer


class ChessGamesProducer:
    def __init__(self, location='localhost:9092'):
        self.location = location
        self._kafka_producer = None

    def publish_message(self, topic_name, value):
        try:
            # TODO: Fix partitioning.
            # add key as an input argument
            # key_bytes = bytes(key.encode())#, encoding='utf-8')
            value_bytes = bytes(value.encode())#, encoding='utf-8')
            # value_bytes = bytes(value, encoding='utf-8')
            self._kafka_producer.send(topic_name, value=value_bytes)
            self._kafka_producer.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def publish_json_message(self, topic_name, value):
        try:
            # TODO: Fix partitioning.
            value_dumped = json.dumps(value)
            value_bytes = bytes(value_dumped.encode())#, encoding='utf-8')
            self._kafka_producer.send(topic_name, value=value_bytes)
            self._kafka_producer.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))
    def connect_kafka_producer(self):
        try:
            self._kafka_producer = KafkaProducer(bootstrap_servers=[self.location], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))

    def close(self):
        self._kafka_producer.close()

