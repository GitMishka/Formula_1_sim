import json
import random
import time
from kafka import KafkaProducer

# Kafka configuration
KAFKA_TOPIC = 'race_data'
KAFKA_BROKERS = 'localhost:9092' 

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

class F1Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.speed = 0  # km/h
        self.position = 0  # meters
        self.lap = 1

    def update(self):
        # Update car state for simulation
        self.speed = random.uniform(150, 350)  # Random speed between 150km/h and 350km/h
        self.position += self.speed * (1 / 3600)  # Position update in km
        # Check if a lap is completed (assuming 5km track length for simplicity)
        if self.position >= 5:
            self.position = 0
            self.lap += 1

    def get_data(self):
        # Return current state as a dictionary
        return {
            'car_id': self.car_id,
            'speed': self.speed,
            'position': self.position,
            'lap': self.lap,
            'timestamp': time.time()
        }

def main():
    # Create 20 F1 cars
    cars = [F1Car(i) for i in range(1, 21)]

    # Run the simulation for 10 minutes
    start_time = time.time()
    while time.time() - start_time < 600:
        for car in cars:
            car.update()
            # Send data to Kafka
            producer.send(KAFKA_TOPIC, car.get_data())
        time.sleep(1)  # Update every second

    producer.close()

if __name__ == "__main__":
    main()