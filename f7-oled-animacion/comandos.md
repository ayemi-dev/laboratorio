# Una animación en una OLED con un ESP32 · paso a paso

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre dentro de la carpeta `f7-oled-animacion`.

## 1. Genera los cuadros

```text
python cuadros.py
```

Sale esto:

```text
8 cuadros de 128 x 64 puntos
1024 bytes por cuadro, 8192 en total
escrito: src/cuadros.h
```

Qué hace el script, en tres pasos:

1. **Dibuja** cada pose en una rejilla de 128 × 64 ceros y unos, con tres herramientas: `circulo`, `triangulo` y `linea`. La función `gatito(n)` arma la pose `n`: el cuerpo rebota, la cabeza se ladea, las patas de arriba se turnan, la cola se mece y en dos poses parpadea.
2. **Convierte** cada fila de 128 puntos en 16 bytes: junta los puntos de 8 en 8 y el primero de cada grupo va en el bit más alto. Por ejemplo, los puntos `00111100` son el byte `0x3C`. Es el orden que lee `drawBitmap()`.
3. **Escribe** `src/cuadros.h` con los 8 cuadros de 1024 bytes cada uno:

```cpp
const uint8_t NUM_CUADROS = 8;

const uint8_t cuadros[NUM_CUADROS][1024] PROGMEM = {
```

`PROGMEM` le dice al compilador que esos datos van en la memoria del programa (la flash), que es lo que pide la librería Adafruit GFX para `drawBitmap()`.

Para ver un cuadro en la terminal (`#` es un punto prendido):

```text
python cuadros.py --vista 0
```

Para guardar las 8 poses como imágenes PNG en la carpeta `vista` (necesita Pillow):

```text
pip install pillow
python cuadros.py --png vista
```

## 2. El programa del ESP32

[`src/main.cpp`](src/main.cpp), línea por línea:

| Línea | Qué hace |
|---|---|
| `Adafruit_SSD1306 oled(128, 64, &Wire, -1);` | La pantalla: 128 × 64, por I2C (`Wire`), sin pin de reinicio (`-1`) |
| `oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);` | La enciende en la dirección I2C 0x3C |
| `oled.clearDisplay();` | Borra el dibujo en la memoria del ESP32 |
| `oled.drawBitmap(0, 0, cuadros[n], 128, 64, SSD1306_WHITE);` | Dibuja el cuadro `n`: cada bit en 1 prende su punto |
| `oled.display();` | Manda el dibujo a la pantalla por I2C. Sin esta línea no cambia nada |
| `n = (n + 1) % NUM_CUADROS;` | Pasa al siguiente cuadro; después del último vuelve al primero |
| `delay(80);` | Espera 80 milisegundos antes de la siguiente vuelta |

En el ESP32, `Wire` usa por defecto SDA en el pin 21 y SCL en el pin 22: por eso el circuito va así.

## 3. Simula

**En el navegador (sin instalar nada):** sigue los pasos de «Ábrelo en Wokwi» del [`README.md`](README.md): `sketch.ino` con el código de `main.cpp`, una pestaña `cuadros.h`, el [`diagram.json`](diagram.json) y el [`libraries.txt`](libraries.txt). Botón verde y listo.

**En VS Code con PlatformIO:** compila en la terminal de PlatformIO:

```text
pio run
```

Debe terminar en `SUCCESS` y dejar `.pio/build/esp32dev/firmware.bin` y `.pio/build/esp32dev/firmware.elf`. Con la extensión Wokwi Simulator y su licencia: `F1` → **Wokwi: Start Simulator** ([`wokwi.toml`](wokwi.toml) ya apunta al firmware).

## 4. Tu propia animación

1. Cambia la función `gatito(n)` de `cuadros.py`, o cambia `NUM_CUADROS` para tener más o menos poses.
2. Vuelve a correr `python cuadros.py`.
3. Vuelve a compilar o pega el `cuadros.h` nuevo en Wokwi.

Cada cuadro ocupa 1024 bytes: 8 cuadros son 8192 bytes, y el ESP32 de la placa `esp32dev` tiene 4 MB de flash, así que caben muchos más.

Si prefieres dibujar a mano, Adafruit recomienda la herramienta web image2cpp (http://javl.github.io/image2cpp/) para convertir una imagen de 128 × 64 a bytes. Usa dibujos tuyos o con permiso.

---
Guía: CC BY-SA 4.0 · Código: MIT
