# Recibe por MQTT las lecturas del ESP32
# y las guarda en un CSV, una fila por lectura.
# Broker publico: solo para pruebas, nada real.
import csv
import json
import os
from datetime import datetime
import paho.mqtt.client as mqtt

ALEATORIO = "693e139e"   # el mismo de main.py
TEMA = "ayemi-lab/" + ALEATORIO + "/clima"
ARCHIVO = "lecturas.csv"
COLUMNAS = ["hora", "temperatura", "humedad"]
LIMITE = 12   # lecturas que guarda antes de salir

if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w", newline="") as f:
        csv.writer(f).writerow(COLUMNAS)

guardadas = 0


def al_conectar(cliente, extra, banderas, codigo, props):
    print("Escuchando", TEMA)
    cliente.subscribe(TEMA)


def al_recibir(cliente, extra, mensaje):
    global guardadas
    datos = json.loads(mensaje.payload)
    t, h = datos["t"], datos["h"]
    hora = datetime.now().strftime("%H:%M:%S")
    print(hora, "temperatura", t, "humedad", h)
    with open(ARCHIVO, "a", newline="") as f:
        csv.writer(f).writerow([hora, t, h])
    guardadas += 1
    if guardadas == LIMITE:
        print("Guardadas", guardadas, "lecturas")
        cliente.disconnect()


cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
cliente.on_connect = al_conectar
cliente.on_message = al_recibir
cliente.connect("test.mosquitto.org", 1883)
cliente.loop_forever()
