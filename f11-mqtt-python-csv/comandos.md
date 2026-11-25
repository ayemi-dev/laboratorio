# ESP32 + MQTT + Python · los comandos

Guía del video. El ESP32 se simula en el navegador (ver [`../f10-esp32-wifi-mqtt/README.md`](../f10-esp32-wifi-mqtt/README.md));
estos comandos van en la terminal de tu computadora, en la carpeta de `recibir.py` y `graficar.py`.

## 1. Los comandos del video

| Comando | Qué hace |
|---|---|
| `python -m pip install paho-mqtt matplotlib` | Instala el cliente MQTT de Eclipse Paho y matplotlib |
| `python recibir.py` | Se suscribe al tema del ESP32, imprime cada lectura con su hora y la agrega a `lecturas.csv`; sale solo tras 12 |
| `head -n 5 lecturas.csv` | Muestra las primeras cinco líneas del CSV (en Git Bash, macOS o Linux) |
| `python graficar.py` | Lee `lecturas.csv` y guarda la gráfica en `grafica.png` |

En macOS y Linux, si `python` no existe, usa `python3`. En Windows la guía de pip usa `py -m pip`; en Git Bash, con
Python en el `PATH`, funciona `python`.

## 2. Opcional: un entorno virtual

Para instalar los paquetes aparte de los de tu sistema (módulo `venv` de Python). En Git Bash, en Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

En macOS y Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Después corre los comandos de la sección 1.

## 3. Lo que puedes cambiar

| En `recibir.py` | Para qué |
|---|---|
| `ALEATORIO = "693e139e"` | Ponle el mismo texto al azar que usaste en el `main.py` del ESP32 |
| `LIMITE = 12` | Cuántas lecturas guarda antes de salir |
| `ARCHIVO = "lecturas.csv"` | El nombre del CSV; si ya existe, agrega filas al final |

## 4. Por qué un broker de pruebas no sirve para datos reales

El puerto 1883 de `test.mosquitto.org` no cifra ni pide usuario, y cualquiera puede publicar o suscribirse a cualquier
tema. La propia página lo dice: no publiques nada sensible, porque cualquiera podría estar escuchando, y no dependas de
él para nada importante. Úsalo para aprender; para un proyecto, tu propio broker con usuario y cifrado.

Fuentes: paho-mqtt (`https://pypi.org/project/paho-mqtt/`,
`https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html`), Python (`https://docs.python.org/3/library/csv.html`,
`https://docs.python.org/3/library/json.html`, `https://docs.python.org/3/library/datetime.html`,
`https://docs.python.org/3/library/venv.html`), pip (`https://pip.pypa.io/en/stable/user_guide/`), matplotlib
(`https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html`), GNU Coreutils
(`https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html`) y Eclipse Mosquitto
(`https://test.mosquitto.org/`), consultadas el 25 de noviembre de 2026.

---
Guía: CC BY-SA 4.0 · Código: MIT
