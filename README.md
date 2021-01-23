# chess_scrape

### api information:
https://www.chess.com/news/view/published-data-api


## Setup

### Run Zookeeper:
/bin/zkServer.sh start && /bin/zkCli.sh

### Running Kafka:
/bin/kafka-server-start.sh /etc/kafka/server.properties 

### Running a consumer:
/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic TOPIC_NAME --from-beginning


