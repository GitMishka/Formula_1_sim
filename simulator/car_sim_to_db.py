import psycopg2
import random
import time
import config

DB_HOST = config.pg_host
DB_NAME = config.pg_database
DB_USER = config.pg_user
DB_PASS = config.pg_password

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)
cur = conn.cursor()

class F1Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.speed = 0  # km/h
        self.position = 0  # meters
        self.lap = 1

    def update(self):
        self.speed = random.uniform(150, 350)  # Random speed between 150km/h and 350km/h
        self.position += self.speed * (1 / 3600)  # Position update in km
        if self.position >= 5:
            self.position = 0
            self.lap += 1

    def get_data(self):
        return (self.car_id, self.speed, self.position, self.lap)

def insert_data(data):
    sql = """INSERT INTO race_data(car_id, speed, position, lap) VALUES(%s, %s, %s, %s)"""
    cur.execute(sql, data)
    conn.commit()

def main():
    cars = [F1Car(i) for i in range(1, 21)]
    start_time = time.time()
    while time.time() - start_time < 600:  # Run for 10 minutes
        for car in cars:
            car.update()
            insert_data(car.get_data())
        time.sleep(1)  # Update every second

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
