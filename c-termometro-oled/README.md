# Un termómetro con ESP32, DHT22 y pantalla OLED, simulado en Wokwi

Carrusel de la saga **F · Microcontroladores** del Laboratorio Ayemi. Un ESP32 lee temperatura y humedad de un sensor DHT22 y las muestra en una pantalla OLED SSD1306 de 128 × 64 por I2C. Todo se simula gratis en el navegador con [Wokwi](https://wokwi.com), sin comprar nada.

## Qué se conecta con qué (7 cables)

| Pieza | Pin | Va al ESP32 |
|---|---|---|
| DHT22 | VCC | 3V3 |
| DHT22 | GND | GND |
| DHT22 | SDA (su cable de datos) | pin 15 |
| OLED SSD1306 | VCC | 3V3 |
| OLED SSD1306 | GND | GND |
| OLED SSD1306 | SDA (datos I2C) | pin 21 |
| OLED SSD1306 | SCL (reloj I2C) | pin 22 |

Ojo: el pin que Wokwi llama **SDA** en el DHT22 no es I2C. Es el único cable de datos del sensor, con su propio protocolo de un hilo. Por eso va a otro pin (15) y no comparte el 21 con la pantalla.

## Ábrelo en Wokwi (en el navegador)

1. Entra a https://wokwi.com y abre un proyecto nuevo de **ESP32** (con Arduino).
2. Pega el contenido de [`sketch.ino`](sketch.ino) en `sketch.ino`.
3. Reemplaza `diagram.json` por [`diagram.json`](diagram.json) (el ESP32, el sensor, la pantalla y sus siete cables).
4. Crea `libraries.txt` con el contenido de [`libraries.txt`](libraries.txt).
5. Pulsa el botón verde. En el plan gratuito la compilación puede esperar en fila un momento.
6. Haz clic en el DHT22: se abre una ventanita con dos deslizadores. Mueve la temperatura o la humedad y mira cómo cambian la pantalla y el monitor serie.

En el monitor serie verás algo así (los valores dependen de dónde pongas los deslizadores; el sensor arranca en 24 °C y 40 %):

```text
Termometro listo: DHT22 y OLED
Temperatura: 24.0 C, humedad: 40.0 %
```

## Qué hace el código

- `dht.setup(15, DHTesp::DHT22)` le dice a la librería en qué pin está el sensor y qué modelo es.
- `oled.begin(SSD1306_SWITCHCAPVCC, 0x3C)` enciende la pantalla en la dirección I2C 0x3C, la que usa Wokwi.
- En cada vuelta, `dht.getTempAndHumidity()` lee las dos cifras; si el sensor falla, el monitor serie dice por qué.
- La pantalla se borra, se escribe «Temperatura» y la cifra en grande, «Humedad» y su cifra, y `oled.display()` la manda por I2C.
- `delay(dht.getMinimumSamplingPeriod())` espera 2 segundos: el DHT22 no se debe leer más seguido.

## Para tomar en cuenta

- **Precisión (sensor real):** la hoja de datos del AM2302 (DHT22), manual v1.1 de Aosong, da ±0.5 °C típico (±1 °C máximo) en temperatura, ±2 %HR a 25 °C en humedad, un rango de −40 a 80 °C y una lectura cada 2 s como mínimo. En Wokwi el sensor da el valor que pones con el deslizador.
- **Librería del sensor:** Wokwi recomienda «DHT sensor library for ESPx» para el ESP32. Su repositorio está archivado (ya no se mantiene), pero funciona en la simulación.
- **Dirección I2C:** Wokwi usa 0x3C, como muchos módulos. Si tu pantalla real no enciende, prueba con `0x3D` en `oled.begin(...)`.
- **Velocidad:** en Wokwi el ESP32 corre por defecto a unos 8 MHz; no afecta a este proyecto.

Verificado el 27 de noviembre de 2026 en la documentación oficial de Wokwi, en la librería DHTesp, en Adafruit, en Espressif y en la hoja de datos del AM2302.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| El DHT22 en Wokwi | https://docs.wokwi.com/parts/wokwi-dht22 |
| La pantalla SSD1306 en Wokwi | https://docs.wokwi.com/parts/board-ssd1306 |
| El ESP32 en Wokwi | https://docs.wokwi.com/guides/esp32 |
| Librería DHT sensor library for ESPx (DHTesp) | https://github.com/beegee-tokyo/DHTesp |
| Librería Adafruit SSD1306 | https://github.com/adafruit/Adafruit_SSD1306 |
| Pines I2C del ESP32 con Arduino | https://github.com/espressif/arduino-esp32/blob/master/variants/esp32/pins_arduino.h |
| Hoja de datos del AM2302 (DHT22), manual v1.1 de Aosong | https://atta.szlcsc.com/upload/public/pdf/source/20161123/1479873083101.pdf |
| La OLED con un ESP32, paso a paso | [`../f7-oled-animacion/`](../f7-oled-animacion/) |
| El DHT22 con un ESP32 y MicroPython | [`../f10-esp32-wifi-mqtt/`](../f10-esp32-wifi-mqtt/) |

Ayemi no tiene relación con Wokwi, Aosong, Adafruit, Espressif ni con el autor de DHTesp.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
