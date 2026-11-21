# Pico + DHT22 en Wokwi · el programa línea por línea

Guía del video. Todo se hace en el navegador, en el proyecto de Wokwi que armas con el [`README.md`](README.md).

## 1. El circuito, en `diagram.json`

Cada cable es una línea de la sección `connections`: el pin de un lado, el pin del otro, el color del cable y su
trazado.

| Línea | Qué conecta |
|---|---|
| `[ "sensor:VCC", "pico:3V3", "red", [ "v0" ] ],` | Corriente del sensor a los 3.3 V de la Pico |
| `[ "sensor:GND", "pico:GND.8", "black", [ "v0" ] ],` | Tierra del sensor a una tierra de la Pico |
| `[ "sensor:SDA", "pico:GP22", "green", [ "v0" ] ]` | Datos del sensor al pin GP22 |

El cuarto pin del DHT22, `NC`, no se conecta. En la sección `parts`, los atributos `temperature` y `humidity` son los
valores con los que arranca el sensor simulado (24 °C y 40 %).

## 2. El programa, en `main.py`

| Línea | Qué hace |
|---|---|
| `import dht` | Trae el módulo del sensor; ya viene en el MicroPython de la Pico |
| `sensor = dht.DHT22(Pin(22))` | Crea el sensor en su pin de datos, GP22 |
| `time.sleep(2)` | Espera 2 segundos: el DHT22 da su lectura más precisa si no se consulta más seguido |
| `sensor.measure()` | Pide una lectura nueva al sensor |
| `t = sensor.temperature()` | Temperatura de esa lectura, en grados Celsius |
| `h = sensor.humidity()` | Humedad de esa lectura, en porcentaje de humedad relativa |
| `print("Temperatura:", t, "°C")` | La muestra en la consola |

La espera va al principio de cada vuelta, así el sensor tiene sus 2 segundos también antes de la primera lectura.

## 3. Pruébalo a mano en el REPL

Con la simulación corriendo, haz clic en la consola y pulsa `Ctrl+C`: el programa se detiene y aparece el indicador
`>>>`. Escribe estas órdenes, una por línea:

```text
sensor.measure()
sensor.temperature()
sensor.humidity()
```

La primera pide una lectura y las otras dos devuelven los valores, por ejemplo `24.0` y `40.0`. Mueve un deslizador del
sensor y repite las tres órdenes.

## 4. Cambia el pin o el ritmo

- **Otro pin:** cambia `Pin(22)` en `main.py` y `pico:GP22` en `diagram.json`. En la Pico, de GP0 a GP22 son pines
  digitales.
- **Otro ritmo:** cambia el `2` de `time.sleep(2)` por más segundos. Menos de 2 no conviene con el DHT22.

Fuentes: documentación de Wokwi (`https://docs.wokwi.com/parts/wokwi-dht22`, `https://docs.wokwi.com/diagram-format`,
`https://docs.wokwi.com/guides/micropython`, `https://docs.wokwi.com/parts/wokwi-pi-pico`) y de MicroPython
(`https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html`, `https://docs.micropython.org/en/latest/library/time.html`),
y el manifiesto del puerto `rp2` de MicroPython (`https://github.com/micropython/micropython/blob/master/ports/rp2/boards/manifest.py`),
consultados el 21 de noviembre de 2026.

---
Guía: CC BY-SA 4.0 · Código: MIT
