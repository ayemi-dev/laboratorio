# ESP32 + DHT22 con MicroPython: manda temperatura y humedad por MQTT.
# El broker publico es solo para pruebas: nunca mandes datos reales.
import network
import time
import json
import dht
from machine import Pin
from umqtt.simple import MQTTClient

ALEATORIO = "693e139e"   # cambialo por el tuyo
TEMA = "ayemi-lab/" + ALEATORIO + "/clima"

sensor = dht.DHT22(Pin(15))   # datos en el pin 15

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Wokwi-GUEST", "")
while not wifi.isconnected():
    time.sleep(0.1)
print("Wi-Fi conectado")

mqtt = MQTTClient("esp32-" + ALEATORIO, "test.mosquitto.org")
mqtt.connect()
print("Conectado al broker")

while True:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    datos = json.dumps({"t": t, "h": h})
    mqtt.publish(TEMA, datos)
    print("Enviado:", datos)
    time.sleep(5)
