# Pico + DHT22 con MicroPython, simulada en Wokwi.
from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(22))   # GP22: datos

while True:
    time.sleep(2)             # una lectura cada 2 s
    sensor.measure()          # lectura nueva
    t = sensor.temperature()  # grados Celsius
    h = sensor.humidity()     # % de humedad relativa
    print("Temperatura:", t, "°C")
    print("Humedad:", h, "%")
