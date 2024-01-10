import random
import time

class F1Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.speed = 0
        self.acceleration = 0
        self.position = 0

    def update_data(self):
        self.speed = random.uniform(100, 350) 
        self.acceleration = random.uniform(0, 10)  
        self.position += self.speed * 0.1  

    def get_data(self):
        return {
            "car_id": self.car_id,
            "speed": self.speed,
            "acceleration": self.acceleration,
            "position": self.position
        }


cars = [F1Car(car_id) for car_id in range(1, 6)]  # 5 cars

while True:
    for car in cars:
        car.update_data()
        print(car.get_data())
    time.sleep(1) 
