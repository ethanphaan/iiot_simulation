# data_visualization.py
# ITAI 3377 - Lab 04 | Ethan Phan
# Real-time Data Visualization - Subscribes to MQTT and plots sensor data live

import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json

data = []

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    try:
        sensor = json.loads(payload)
        data.append((datetime.now(), sensor["temperature"], sensor["humidity"]))
        if len(data) > 100:
            data.pop(0)

        df = pd.DataFrame(data, columns=["timestamp", "temperature", "humidity"])

        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(df["timestamp"], df["temperature"], label="Temperature (C)", color="red")
        plt.ylabel("Temperature (C)")
        plt.legend(loc="upper left")
        plt.title("IIoT Sensor Network - Real-Time Data (MQTT)")
        plt.xticks(rotation=45)

        plt.subplot(2, 1, 2)
        plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="blue")
        plt.ylabel("Humidity (%)")
        plt.xlabel("Timestamp")
        plt.legend(loc="upper left")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.draw()
        plt.pause(0.1)
    except Exception as e:
        print(f"Error parsing message: {e}")

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/data")
client.on_message = on_message

plt.ion()
plt.figure(figsize=(12, 6))
client.loop_start()

print("[Visualization] Listening for MQTT sensor data on topic: sensor/data")
print("[Visualization] Press Ctrl+C to stop.")

try:
    plt.show(block=True)
except KeyboardInterrupt:
    print("\n[Visualization] Stopped.")
    client.loop_stop()
