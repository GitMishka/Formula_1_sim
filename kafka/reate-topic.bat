@echo off
echo Creating Kafka topic: race_data
.\bin\windows\kafka-topics.bat --create --topic race_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
echo Topic created successfully.
