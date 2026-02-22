# IIoT Sensor Network Simulation
## ITAI 3377 - Lab 04 | Ethan Phan

## Project Overview
This project designs and simulates an Industrial Internet of Things (IIoT) sensor network. The simulation generates sensor data (temperature and humidity) using three industry-standard protocols: **MQTT**, **CoAP**, and **OPC UA**, and visualizes the data in real time.

## Project Structure
```
iiot_simulation/
├── README.md
├── mqtt_sensor_simulation.py
├── coap_sensor_simulation.py
├── opcua_sensor_simulation.py
├── data_visualization.py
├── generate_visualizations.py
├── visualizations/
│   ├── mqtt_visualization.png
│   ├── coap_visualization.png
│   ├── opcua_visualization.png
│   └── visualization_demo.mp4
└── comparison_report.md
```

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Mosquitto MQTT Broker

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/ethanphaan/iiot_simulation.git
cd iiot_simulation
```

### Step 2: Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Libraries
```bash
pip install pandas numpy paho-mqtt aiocoap asyncua matplotlib
```

### Step 4: Install Mosquitto MQTT Broker
Download from: https://mosquitto.org/download/
Follow installation instructions for your OS.

## Running the Simulations

### Start MQTT Broker (in a separate terminal)
```bash
mosquitto
```

### Run MQTT Simulation
```bash
python mqtt_sensor_simulation.py
```

### Run CoAP Simulation
```bash
python coap_sensor_simulation.py
```

### Run OPC UA Simulation
```bash
python opcua_sensor_simulation.py
```

### Run Data Visualization
```bash
python data_visualization.py
```

### Generate Static Visualizations (PNGs)
```bash
python generate_visualizations.py
```

## Protocol Descriptions

### MQTT (Message Queuing Telemetry Transport)
- Lightweight publish-subscribe messaging protocol
- Ideal for constrained devices and low-bandwidth networks
- Uses a broker-based architecture (Mosquitto)
- Port: 1883

### CoAP (Constrained Application Protocol)
- RESTful protocol designed for IoT/M2M environments
- Runs over UDP, making it ultra-lightweight
- Supports request/response model similar to HTTP
- Port: 5683

### OPC UA (Open Platform Communications Unified Architecture)
- Industrial standard for secure, reliable data exchange
- Platform-independent and service-oriented
- Supports complex data models and security
- Port: 4840

## Sensor Data
All simulations generate:
- **Temperature**: Random values between 20.0°C and 25.0°C
- **Humidity**: Random values between 30.0% and 50.0%
- **Interval**: Data generated every 1 second

## Author
- **Name:** Ethan Phan
- **Course:** ITAI 3377
- **Assignment:** Lab 04 - Conceptual Design of an IIoT Sensor Network & Protocol Experimentation
- **Institution:** Houston Community College

## File Naming Convention
L04_EthanPhan_ITAI_3377
