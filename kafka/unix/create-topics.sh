#!/bin/bash

# Define your topic name
TOPIC_NAME="race_data"

# Create the topic with a single partition and only one replica (modify as needed)
echo "Creating Kafka topic: $TOPIC_NAME"
bin/kafka-topics.sh --create --topic $TOPIC_NAME --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

echo "Topic $TOPIC_NAME created successfully."
