# opcua_sensor_simulation.py
# ITAI 3377 - Lab 04 | Ethan Phan
# OPC UA Sensor Simulation - Writes temperature and humidity to OPC UA server

from asyncua import ua, Server
import asyncio
import random

async def main():
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    objects = server.nodes.objects
    myobj = await objects.add_object(idx, "MyObject")

    temperature = await myobj.add_variable(idx, "Temperature", 0.0)
    humidity = await myobj.add_variable(idx, "Humidity", 0.0)
    await temperature.set_writable()
    await humidity.set_writable()

    async with server:
        print("[OPC UA] Server started at opc.tcp://0.0.0.0:4840")
        while True:
            temp_value = random.uniform(20.0, 25.0)
            hum_value = random.uniform(30.0, 50.0)
            await temperature.write_value(temp_value)
            await humidity.write_value(hum_value)
            print(f"[OPC UA] Written -> Temperature: {temp_value:.2f}C, Humidity: {hum_value:.2f}%")
            await asyncio.sleep(1)

asyncio.run(main())
