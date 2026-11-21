# Una animación en una OLED de 0.96" con un ESP32

Video de la serie **Microcontroladores con herramientas modernas** del Laboratorio Ayemi. Un gatito baila en una pantalla OLED SSD1306 de 128 × 64 conectada a un ESP32, y aquí está cómo: la animación se vuelve cuadros de bits que el ESP32 dibuja uno tras otro.

- **Un punto es un bit:** la pantalla es monocromática, cada punto está prendido (1) o apagado (0).
- **Ocho puntos son un byte**, así que la pantalla entera, 128 × 64 puntos, cabe en **1024 bytes**. Eso es un cuadro.
- **El gatito es un dibujo original de Ayemi, hecho solo con código** en [`cuadros.py`](cuadros.py): círculos, triángulos y líneas en 8 poses. No usa imágenes, GIF ni personajes de nadie.
- El script guarda los 8 cuadros (8192 bytes) en [`src/cuadros.h`](src/cuadros.h) con `PROGMEM`, en la memoria del programa.
- En [`src/main.cpp`](src/main.cpp), cada vuelta del ciclo borra, dibuja un cuadro con `drawBitmap()`, lo manda a la pantalla por I2C con `display()` y pasa al siguiente.

## Ábrelo en Wokwi (en el navegador)

1. Entra a https://wokwi.com y abre un proyecto nuevo de **ESP32** (con Arduino).
2. Pega el contenido de [`src/main.cpp`](src/main.cpp) en `sketch.ino`.
3. Crea una pestaña nueva llamada `cuadros.h` y pega [`src/cuadros.h`](src/cuadros.h).
4. Reemplaza `diagram.json` por [`diagram.json`](diagram.json) (el ESP32 y la pantalla con sus cuatro cables).
5. Crea `libraries.txt` con el contenido de [`libraries.txt`](libraries.txt).
6. Pulsa el botón verde. En el plan gratuito la compilación puede esperar en fila un momento.

## Compílalo en VS Code con PlatformIO

Abre esta carpeta en VS Code con la extensión **PlatformIO IDE** y, en su terminal, compila:

```text
pio run
```

PlatformIO descarga la librería Adafruit SSD1306 (la pide [`platformio.ini`](platformio.ini)) y deja el programa en `.pio/build/esp32dev/firmware.bin`. Si tienes la extensión **Wokwi Simulator** con su licencia (se pide con tu cuenta de Wokwi; es gratis para proyectos de código abierto), [`wokwi.toml`](wokwi.toml) ya apunta a ese archivo: `F1` → **Wokwi: Start Simulator**. Más detalle en el video anterior, [`f6-wokwi-vscode`](../f6-wokwi-vscode/).

## Haz tu propia animación

Cambia el dibujo en la función `gatito()` de [`cuadros.py`](cuadros.py) y vuelve a generar el `.h`:

```text
python cuadros.py
```

Para ver un cuadro en la terminal o guardar las poses como imágenes:

```text
python cuadros.py --vista 0
python cuadros.py --png vista
```

`--png` necesita Pillow (`pip install pillow`). El resto del script solo usa Python.

La guía paso a paso, con qué hace cada línea, está en [`comandos.md`](comandos.md).

## Para tomar en cuenta

- **Velocidad:** en Wokwi el ESP32 corre por defecto a unos 8 MHz, así que la animación puede ir más lenta que en una placa real.
- **Dirección I2C:** Wokwi usa 0x3C, como muchos módulos. Si tu pantalla real no enciende, prueba con `0x3D` en `oled.begin(...)`.
- **Cables (placa real o simulada):** VCC al 3V3, GND a GND, SDA al pin 21 y SCL al pin 22, los pines I2C de Arduino en el ESP32.
- **Usa tus propios dibujos.** Si conviertes una imagen, que sea tuya o que tengas permiso.

Verificado el 20 de noviembre de 2026 en la documentación oficial de Wokwi, PlatformIO, Adafruit, Espressif y Solomon Systech.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| La pantalla SSD1306 en Wokwi | https://docs.wokwi.com/parts/board-ssd1306 |
| El ESP32 en Wokwi | https://docs.wokwi.com/guides/esp32 |
| Wokwi con PlatformIO | https://docs.wokwi.com/vscode/platformio |
| Licencia de Wokwi para VS Code | https://wokwi.com/license |
| `drawBitmap()` y PROGMEM (Adafruit GFX) | https://learn.adafruit.com/adafruit-gfx-graphics-library/graphics-primitives |
| Librería Adafruit SSD1306 | https://github.com/adafruit/Adafruit_SSD1306 |
| Placa `esp32dev` en PlatformIO | https://docs.platformio.org/en/latest/boards/espressif32/esp32dev.html |
| Pines I2C del ESP32 con Arduino | https://github.com/espressif/arduino-esp32/blob/master/variants/esp32/pins_arduino.h |
| Controlador SSD1306 | https://www.solomon-systech.com/product/SSD1306 |
| Video anterior: Wokwi y PlatformIO en VS Code | [`../f6-wokwi-vscode/`](../f6-wokwi-vscode/) |

Ayemi no tiene relación con Wokwi, PlatformIO, Adafruit, Espressif ni Solomon Systech.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
