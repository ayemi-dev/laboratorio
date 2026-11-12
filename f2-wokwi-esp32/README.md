# Un ESP32 que consulta internet, simulado en el navegador (Wokwi)

El ESP32 simulado en [Wokwi](https://wokwi.com/) se conecta a su Wi-Fi virtual (`Wokwi-GUEST`), le pide a [Open-Meteo](https://open-meteo.com/) la temperatura actual de la Ciudad de México y la muestra en una pantalla OLED junto a la de un sensor DHT22.

## Usar

1. Abre un proyecto nuevo con ESP32: https://wokwi.com/projects/new/esp32
2. En `sketch.ino`, borra el ejemplo y pega [`sketch.ino`](sketch.ino).
3. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): ESP32, DHT22 en el GPIO 15 y OLED SSD1306 por I2C (SDA en el 21, SCL en el 22).
4. Agrega las librerías de [`libraries.txt`](libraries.txt) desde «Library Manager» (DHT sensor library, Adafruit SSD1306 y Adafruit GFX Library).
5. Pulsa el botón verde de iniciar simulación. En el monitor serie verás `Wi-Fi conectado` y luego `Aqui 24.0 C | CDMX …`; la pantalla muestra las dos temperaturas y se actualiza cada 10 s. Haz clic en el DHT22 para cambiar su temperatura.

## Para tomar en cuenta

- **Wi-Fi virtual:** `Wokwi-GUEST` es abierta, sin contraseña. El tráfico pasa por el gateway público de Wokwi, que lo monitorea: no mandes datos privados.
- **Fila de compilación:** en el plan gratuito, la compilación puede esperar unos segundos en fila.
- **Open-Meteo:** no pide clave; el uso gratuito es no comercial (hasta 10 000 llamadas al día) y los datos son CC BY 4.0, con atribución. Para un producto comercial revisa sus planes.
- **Para cambiar de ciudad,** edita `latitude` y `longitude` en `URL`.

Verificado el 12 de noviembre de 2026 en la documentación de Wokwi y en las páginas de Open-Meteo.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, nuevo proyecto con ESP32 | https://wokwi.com/projects/new/esp32 |
| Wi-Fi del ESP32 en Wokwi | https://docs.wokwi.com/guides/esp32-wifi |
| Planes de Wokwi | https://wokwi.com/pricing |
| Open-Meteo (API del clima) | https://open-meteo.com/ |
| Términos de Open-Meteo | https://open-meteo.com/en/terms |

Datos del clima: [Open-Meteo.com](https://open-meteo.com/) (CC BY 4.0). Ayemi no tiene relación con Wokwi ni con Open-Meteo.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
