# coap_sensor_simulation.py
# ITAI 3377 - Lab 04 | Ethan Phan
# CoAP Sensor Simulation - Sends temperature and humidity data via CoAP POST

import asyncio
import random
from aiocoap import *

async def simulate_sensor_data():
    protocol = await Context.create_client_context()

    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)
        payload = f'{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}'.encode('utf-8')

        request = Message(code=POST, payload=payload)
        request.set_request_uri('coap://localhost/sensor/data')

        try:
            response = await protocol.request(request).response
            print(f'[CoAP] Result: {response.code} | Payload: {response.payload}')
        except Exception as e:
            print(f'[CoAP] Failed to send request: {e}')

        print(f"[CoAP] Sent -> Temperature: {temperature:.2f}C, Humidity: {humidity:.2f}%")
        await asyncio.sleep(1)

asyncio.run(simulate_sensor_data())
