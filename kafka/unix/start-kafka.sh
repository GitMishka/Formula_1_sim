#!/bin/bash

# Start Zookeeper
echo "Starting Zookeeper..."
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Sleep for a few seconds to ensure Zookeeper starts up completely
sleep 5

# Start Kafka server
echo "Starting Kafka..."
bin/kafka-server-start.sh config/server.properties &
