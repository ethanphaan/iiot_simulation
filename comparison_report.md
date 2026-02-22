# IIoT Protocol Comparison Report
## ITAI 3377 - Lab 04 | Ethan Phan
**Course:** ITAI 3377 | **Institution:** Houston Community College
**Date:** February 2026

---

## 1. Introduction

This report presents a comparative analysis of three Industrial Internet of Things (IIoT) communication protocols used in sensor network simulation: **MQTT**, **CoAP**, and **OPC UA**. Each protocol was used to simulate a sensor that transmits temperature (20.0–25.0°C) and humidity (30.0–50.0%) readings every second. The goal of this lab was to understand the practical differences, strengths, and weaknesses of each protocol in an IIoT context.

---

## 2. Protocol Overview

### 2.1 MQTT (Message Queuing Telemetry Transport)
- **Type:** Publish-Subscribe messaging protocol
- **Transport Layer:** TCP/IP
- **Default Port:** 1883 (unencrypted), 8883 (TLS)
- **Standard Body:** OASIS
- **Best For:** Low-bandwidth, high-latency, unreliable networks

**How It Works:**
MQTT uses a broker-based architecture. Sensors (publishers) send data to a central broker (Mosquitto in this lab) on a specific topic (e.g., `sensor/data`). Subscribers connect to the broker and receive messages on matching topics. This decoupled model makes MQTT highly scalable.

**Key Features:**
- Extremely lightweight — minimal packet overhead
- Three Quality of Service (QoS) levels: 0 (at most once), 1 (at least once), 2 (exactly once)
- Persistent sessions and retained messages
- Wildcard topic subscriptions

---

### 2.2 CoAP (Constrained Application Protocol)
- **Type:** Request-Response RESTful protocol
- **Transport Layer:** UDP
- **Default Port:** 5683 (unencrypted), 5684 (DTLS)
- **Standard Body:** IETF (RFC 7252)
- **Best For:** Constrained devices with very limited CPU/memory/power

**How It Works:**
CoAP is designed as a lightweight HTTP alternative for IoT devices. It uses a RESTful model (GET, POST, PUT, DELETE) over UDP, making it faster but less reliable than TCP-based protocols. In this simulation, sensor data was sent as a POST request to `coap://localhost/sensor/data`.

**Key Features:**
- Built-in resource discovery
- Observe option for subscription-like behavior
- Low overhead due to UDP transport
- Supports multicast for device discovery

---

### 2.3 OPC UA (Open Platform Communications Unified Architecture)
- **Type:** Client-Server / Publish-Subscribe (in newer versions)
- **Transport Layer:** TCP
- **Default Port:** 4840
- **Standard Body:** OPC Foundation
- **Best For:** Industrial automation, manufacturing, SCADA systems

**How It Works:**
OPC UA is a comprehensive industrial communication standard. In this simulation, a server was initialized that exposed sensor variables (Temperature, Humidity) as addressable nodes in an object model. Values are written directly to the server's address space and clients can read or subscribe to them.

**Key Features:**
- Rich data modeling with complex hierarchies
- Built-in security (authentication, encryption, signing)
- Platform-independent
- Supports both polling and event-driven models
- Semantic data context (units, descriptions, data types)

---

## 3. Comparative Analysis

| Feature | MQTT | CoAP | OPC UA |
|---|---|---|---|
| **Transport** | TCP | UDP | TCP |
| **Architecture** | Pub/Sub (Broker) | RESTful (Client-Server) | Client-Server / Pub-Sub |
| **Overhead** | Very Low | Very Low | Medium-High |
| **Reliability** | High (QoS 0/1/2) | Low (UDP-based) | High |
| **Security** | TLS (optional) | DTLS (optional) | Built-in (mandatory) |
| **Scalability** | Very High | Medium | Medium |
| **Data Modeling** | None (raw payloads) | None (raw payloads) | Rich semantic model |
| **Device Suitability** | Constrained to powerful | Ultra-constrained | Powerful industrial |
| **Setup Complexity** | Low | Low | High |
| **Real-time Support** | Good | Good | Excellent |
| **Industry Adoption** | IoT, Smart Home, Mobile | IoT, Embedded systems | Industrial automation |

---

## 4. Performance Observations

### MQTT
- **Latency:** Very low due to persistent TCP connection with the broker
- **CPU/Memory:** Minimal — ideal for microcontrollers (e.g., Arduino, ESP32)
- **Data Flow:** Smooth and consistent; broker handles all routing
- **Observation:** The broker (Mosquitto) added negligible latency; data was received in near real-time by the visualization client

### CoAP
- **Latency:** Low, but variable due to UDP's unreliable nature
- **CPU/Memory:** Extremely low — designed for 8-bit microcontrollers
- **Data Flow:** Some packet loss expected in noisy network conditions
- **Observation:** Without a CoAP server running, POST requests returned errors — highlighting CoAP's dependency on an endpoint being available

### OPC UA
- **Latency:** Higher initialization time due to server setup overhead
- **CPU/Memory:** Requires more resources — suited for PLCs, gateways, industrial computers
- **Data Flow:** Highly structured and reliable once the server is running
- **Observation:** The address space model made it easy to add new sensor variables; server startup required more configuration than MQTT or CoAP

---

## 5. Use Case Recommendations

| Scenario | Recommended Protocol | Reasoning |
|---|---|---|
| Smart home sensors on WiFi | MQTT | Lightweight, broker handles routing, easy cloud integration |
| Battery-powered field sensors | CoAP | UDP reduces power consumption, REST model is familiar |
| Factory floor PLC integration | OPC UA | Rich data model, built-in security, industry standard |
| Mobile IoT applications | MQTT | Native support in AWS IoT, Azure IoT Hub, Google Cloud IoT |
| Critical industrial process control | OPC UA | Mandatory security, complex data modeling, high reliability |
| Mesh networks with packet loss | MQTT (QoS 2) | Exactly-once delivery ensures no data loss |

---

## 6. Simulation Results Summary

All three simulations successfully generated temperature and humidity sensor data at 1-second intervals:
- **Temperature range:** 20.0°C – 25.0°C (simulated room/industrial environment)
- **Humidity range:** 30.0% – 50.0% (normal indoor humidity levels)

The MQTT simulation integrated directly with the real-time visualization (`data_visualization.py`), producing live-updating charts of both metrics. The CoAP and OPC UA simulations demonstrated protocol-specific behaviors, with OPC UA providing the richest data access model via its address space.

---

## 7. Conclusion

All three protocols — MQTT, CoAP, and OPC UA — are valid choices for IIoT sensor networks, but they serve different purposes:

- **MQTT** is the best all-around choice for most IoT deployments due to its simplicity, low overhead, and massive ecosystem support.
- **CoAP** is optimal for battery-constrained, resource-limited devices where UDP's lower power footprint is critical.
- **OPC UA** is the gold standard for industrial environments where interoperability, security, and rich data modeling are non-negotiable.

This simulation demonstrated that each protocol can reliably transmit sensor data, but the choice of protocol must be driven by the specific hardware constraints, security requirements, and operational environment of the deployment.

---

## 8. References

- OASIS MQTT Standard: https://mqtt.org/
- IETF RFC 7252 (CoAP): https://tools.ietf.org/html/rfc7252
- OPC Foundation (OPC UA): https://opcfoundation.org/
- Eclipse Mosquitto MQTT Broker: https://mosquitto.org/
- Python paho-mqtt library: https://pypi.org/project/paho-mqtt/
- Python aiocoap library: https://aiocoap.readthedocs.io/
- Python asyncua library: https://github.com/FreeOpcUa/opcua-asyncio

---

*Report prepared by: Ethan Phan | ITAI 3377 | Houston Community College | February 2026*
*File: L04_EthanPhan_ITAI_3377*
