# generate_visualizations.py
# ITAI 3377 - Lab 04 | Ethan Phan
# Generates static visualization PNG files for MQTT, CoAP, and OPC UA simulated data

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import os

# Create visualizations directory if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# Generate simulated timestamps (60 seconds of data)
start_time = datetime.now()
timestamps = [start_time + timedelta(seconds=i) for i in range(60)]

# Simulate sensor data for each protocol
np.random.seed(42)
temperature_mqtt = np.random.uniform(20.0, 25.0, 60)
humidity_mqtt = np.random.uniform(30.0, 50.0, 60)

np.random.seed(7)
temperature_coap = np.random.uniform(20.0, 25.0, 60)
humidity_coap = np.random.uniform(30.0, 50.0, 60)

np.random.seed(99)
temperature_opcua = np.random.uniform(20.0, 25.0, 60)
humidity_opcua = np.random.uniform(30.0, 50.0, 60)

def generate_chart(timestamps, temperatures, humidities, protocol_name, filename):
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle(f'IIoT Sensor Network - {protocol_name} Protocol\nTemperature & Humidity Over Time', fontsize=14, fontweight='bold')

    # Temperature subplot
    axes[0].plot(timestamps, temperatures, color='red', linewidth=1.5, label='Temperature (C)')
    axes[0].fill_between(timestamps, temperatures, alpha=0.2, color='red')
    axes[0].set_ylabel('Temperature (°C)', fontsize=11)
    axes[0].set_ylim(18, 27)
    axes[0].legend(loc='upper right')
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    axes[0].tick_params(axis='x', rotation=30)
    axes[0].set_title(f'Temperature Readings via {protocol_name}', fontsize=11)

    # Humidity subplot
    axes[1].plot(timestamps, humidities, color='blue', linewidth=1.5, label='Humidity (%)')
    axes[1].fill_between(timestamps, humidities, alpha=0.2, color='blue')
    axes[1].set_ylabel('Humidity (%)', fontsize=11)
    axes[1].set_ylim(25, 55)
    axes[1].set_xlabel('Timestamp', fontsize=11)
    axes[1].legend(loc='upper right')
    axes[1].grid(True, linestyle='--', alpha=0.5)
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    axes[1].tick_params(axis='x', rotation=30)
    axes[1].set_title(f'Humidity Readings via {protocol_name}', fontsize=11)

    plt.tight_layout()
    filepath = os.path.join("visualizations", filename)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[OK] Saved: {filepath}")

# Generate charts for each protocol
generate_chart(timestamps, temperature_mqtt, humidity_mqtt, "MQTT", "mqtt_visualization.png")
generate_chart(timestamps, temperature_coap, humidity_coap, "CoAP", "coap_visualization.png")
generate_chart(timestamps, temperature_opcua, humidity_opcua, "OPC UA", "opcua_visualization.png")

print("\nAll visualizations saved to the 'visualizations/' folder.")
print("Run this script to regenerate charts at any time.")
