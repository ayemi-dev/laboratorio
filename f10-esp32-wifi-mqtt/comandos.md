# ESP32 + MQTT en Wokwi · el programa y los comandos

Guía del video. El ESP32 se simula en el navegador (ver [`README.md`](README.md)); los comandos van en la terminal de tu
computadora.

## 1. Instala `mosquitto_sub`

`mosquitto_sub` viene con Eclipse Mosquitto (https://mosquitto.org/download/).

- **Windows:** descarga el instalador `mosquitto-2.1.4-install-windows-x64.exe` de la página de descarga. Con las opciones
  del instalador sin cambiar, queda en `C:\Program Files\mosquitto\`. En Git Bash, para usarlo en esa terminal:

  ```bash
  export PATH="$PATH:/c/Program Files/mosquitto"
  ```

- **macOS:**

  ```bash
  brew install mosquitto
  ```

- **Linux (con Snap):**

  ```bash
  snap install mosquitto
  ```

## 2. Los comandos

| Comando | Qué hace |
|---|---|
| `python -c "import secrets; print(secrets.token_hex(4))"` | Imprime ocho caracteres hexadecimales al azar para tu tema único |
| `mosquitto_sub -h test.mosquitto.org -t ayemi-lab/693e139e/clima -v` | Se suscribe al tema en el broker de pruebas e imprime cada mensaje con su tema |

Las opciones de `mosquitto_sub`:

| Opción | Qué hace |
|---|---|
| `-h test.mosquitto.org` | El broker al que se conecta (si no la pones, usa tu propia computadora) |
| `-t ayemi-lab/693e139e/clima` | El tema al que se suscribe; cambia `693e139e` por tu texto |
| `-v` | Imprime cada mensaje como «tema datos» |
| `-C 5` (opcional) | Sale solo después de recibir 5 mensajes |

Sin `-p`, usa el puerto 1883: MQTT sin cifrar y sin usuario. Para salir, `Ctrl+C`.

## 3. El programa, en `main.py`

| Línea | Qué hace |
|---|---|
| `from umqtt.simple import MQTTClient` | Trae el cliente MQTT; ya viene en el MicroPython del ESP32 |
| `TEMA = "ayemi-lab/" + ALEATORIO + "/clima"` | Arma el tema; las diagonales separan sus niveles |
| `sensor = dht.DHT22(Pin(15))` | Crea el sensor en su pin de datos, el 15 |
| `wifi.connect("Wokwi-GUEST", "")` | Se conecta a la red virtual de Wokwi, que no lleva contraseña |
| `mqtt = MQTTClient("esp32-" + ALEATORIO, "test.mosquitto.org")` | Crea el cliente con un nombre único y el broker |
| `mqtt.connect()` | Se conecta al broker |
| `sensor.measure()` | Pide una lectura nueva al sensor |
| `datos = json.dumps({"t": t, "h": h})` | Arma el mensaje en JSON: temperatura en grados Celsius y humedad en porcentaje |
| `mqtt.publish(TEMA, datos)` | Publica el mensaje en el tema |
| `time.sleep(5)` | Espera 5 segundos antes de la siguiente lectura |

## 4. Por qué un broker de pruebas no sirve para datos reales

El puerto 1883 de `test.mosquitto.org` no cifra ni pide usuario, y cualquiera puede publicar o suscribirse a cualquier
tema. La propia página lo dice: no publiques nada sensible, porque cualquiera podría estar escuchando. Además, el Wi-Fi
de Wokwi sale por un servidor público que monitorea el tráfico. Úsalo para aprender; para un proyecto, tu propio broker.

Fuentes: documentación de Wokwi (`https://docs.wokwi.com/guides/esp32-wifi`, `https://docs.wokwi.com/guides/esp32`,
`https://docs.wokwi.com/parts/wokwi-dht22`), de MicroPython (`https://docs.micropython.org/en/latest/esp32/quickref.html`,
`https://docs.micropython.org/en/latest/library/json.html`), el manifiesto del puerto `esp32` de MicroPython
(`https://github.com/micropython/micropython/blob/master/ports/esp32/boards/manifest.py`), `umqtt.simple`
(`https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple`), Espressif
(`https://www.espressif.com/en/products/socs/esp32`), Eclipse Mosquitto (`https://mosquitto.org/download/`,
`https://mosquitto.org/man/mosquitto_sub-1.html`, `https://mosquitto.org/man/mqtt-7.html`, `https://test.mosquitto.org/`)
y Python (`https://docs.python.org/3/library/secrets.html`), consultadas el 24 de noviembre de 2026.

---
Guía: CC BY-SA 4.0 · Código: MIT
