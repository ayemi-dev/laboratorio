# Recibe los datos de tu ESP32 en Python y guárdalos en un CSV

Video de la serie **Microcontroladores con herramientas modernas** del Laboratorio Ayemi. Continúa
[`f10-esp32-wifi-mqtt`](../f10-esp32-wifi-mqtt/): el ESP32 simulado en [Wokwi](https://wokwi.com/) sigue publicando la
temperatura y la humedad del DHT22 por MQTT en `test.mosquitto.org`. Ahora, en vez de `mosquitto_sub`, un script de
Python las recibe, imprime cada lectura con su hora y la agrega a un archivo CSV. Otro script dibuja la gráfica.

- **`recibir.py`:** se suscribe al tema del ESP32 con [paho-mqtt](https://pypi.org/project/paho-mqtt/), el cliente MQTT
  de Eclipse Paho para Python; decodifica el JSON de cada mensaje y agrega una fila a `lecturas.csv`. Tras 12 lecturas
  se desconecta y termina solo.
- **`graficar.py`:** lee `lecturas.csv` y guarda en `grafica.png` la temperatura y la humedad con
  [matplotlib](https://matplotlib.org/).

> **Aviso:** `test.mosquitto.org` es un broker **público y solo para pruebas**. El puerto 1883 no cifra ni pide
> usuario: cualquiera que conozca tu tema puede leer lo que mandas, y el servidor puede reiniciarse. **Nunca mandes
> datos reales, personales ni contraseñas.** El Wi-Fi de Wokwi sale además por un servidor público que monitorea el
> tráfico.

## 1. El ESP32 publicando

Abre el proyecto de [`f10-esp32-wifi-mqtt`](../f10-esp32-wifi-mqtt/) en Wokwi (su README lo explica paso a paso, sin
iniciar sesión) y pulsa el botón verde. La consola imprime una línea `Enviado: {...}` cada 5 segundos.

El tema lleva un texto al azar, `693e139e`. Si en `main.py` pusiste el tuyo, ponlo también en `ALEATORIO` de
`recibir.py`: los dos deben ser iguales.

## 2. Instala las dos librerías

En la terminal de tu computadora, con Python 3.9 o más:

```bash
python -m pip install paho-mqtt matplotlib
```

En macOS y Linux puede llamarse `python3`. Si prefieres no mezclar paquetes, usa un entorno virtual (ver
[`comandos.md`](comandos.md)).

## 3. Recibe y guarda

En la carpeta donde están `recibir.py` y `graficar.py`:

```bash
python recibir.py
```

Con la simulación corriendo, haz clic en el sensor de Wokwi y mueve los deslizadores: la siguiente lectura llega con
los valores nuevos. La salida se ve así (la hora es la de tu computadora):

```text
Escuchando ayemi-lab/693e139e/clima
15:05:12 temperatura 24.0 humedad 40.0
15:05:17 temperatura 32.0 humedad 40.0
...
Guardadas 12 lecturas
```

Cada lectura queda en `lecturas.csv`, con una fila de encabezados:

```text
hora,temperatura,humedad
15:05:12,24.0,40.0
```

Si lo vuelves a correr, agrega filas al final (no borra las anteriores). Para guardar más lecturas, cambia `LIMITE`.

## 4. La gráfica

```bash
python graficar.py
```

Guarda `grafica.png` con dos paneles, temperatura arriba y humedad abajo, con la hora en el eje.

## Cómo funciona `recibir.py`

| Línea | Qué hace |
|---|---|
| `mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)` | Crea el cliente con la forma de funciones que recomienda paho-mqtt 2.x |
| `def al_conectar(cliente, extra, banderas, codigo, props):` | Se llama al conectarse; recibe cinco argumentos (los nombres son nuestros, el orden es el de paho-mqtt) |
| `cliente.subscribe(TEMA)` | Se suscribe al tema; al hacerlo dentro de `al_conectar`, la suscripción se renueva si se reconecta |
| `json.loads(mensaje.payload)` | Convierte el JSON del mensaje en un diccionario de Python |
| `datetime.now().strftime("%H:%M:%S")` | La hora local de tu computadora al recibir la lectura |
| `open(ARCHIVO, "a", newline="")` | Abre el CSV para agregar al final, como pide el módulo `csv` |
| `csv.writer(f).writerow([hora, t, h])` | Escribe una fila |
| `cliente.disconnect()` | Al llegar a `LIMITE`, se desconecta y `loop_forever()` termina |
| `cliente.connect("test.mosquitto.org", 1883)` | Se conecta al broker de pruebas, puerto 1883 |
| `cliente.loop_forever()` | Atiende la red y llama a las funciones mientras esté conectado |

Verificado el 25 de noviembre de 2026 en la documentación oficial de Eclipse Paho, PyPI, Python, matplotlib, Eclipse
Mosquitto y Wokwi.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| paho-mqtt en PyPI | https://pypi.org/project/paho-mqtt/ |
| Documentación de paho-mqtt (Eclipse Paho) | https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html |
| Eclipse Paho | https://eclipse.dev/paho/ |
| Módulo `csv` de Python | https://docs.python.org/3/library/csv.html |
| Módulo `json` de Python | https://docs.python.org/3/library/json.html |
| matplotlib, `pyplot.subplots` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html |
| El broker público de pruebas | https://test.mosquitto.org/ |
| Eclipse Mosquitto | https://mosquitto.org/ |
| El Wi-Fi del ESP32 en Wokwi | https://docs.wokwi.com/guides/esp32-wifi |

Ayemi no tiene relación con Eclipse, Wokwi, Python ni matplotlib.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
