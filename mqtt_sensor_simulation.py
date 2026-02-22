# mqtt_sensor_simulation.py
# ITAI 3377 - Lab 04 | Ethan Phan
# MQTT Sensor Simulation - Publishes temperature and humidity data

import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)
        payload = f'{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}'
        client.publish(topic, payload)
        print(f"[MQTT] Published -> Temperature: {temperature:.2f}C, Humidity: {humidity:.2f}%")
        time.sleep(1)

client = mqtt.Client()
client.connect(broker, port)
simulate_sensor_data()
