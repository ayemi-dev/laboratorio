# Tu ESP32 manda datos a internet por MQTT (Wokwi + MicroPython)

Video de la serie **Microcontroladores con herramientas modernas** del Laboratorio Ayemi. Continúa
[`f8-pico-sensor`](../f8-pico-sensor/): el mismo sensor DHT22, ahora en un ESP32 simulado en [Wokwi](https://wokwi.com/)
con MicroPython. En vez de quedarse en la consola, la temperatura y la humedad salen a internet por MQTT cada 5 segundos
y las recibes en tu computadora con `mosquitto_sub`.

- **Wi-Fi sin contraseña:** Wokwi le da al ESP32 una red virtual, `Wokwi-GUEST`, abierta y con salida a internet.
- **Sin instalar nada en el ESP32:** el MicroPython del ESP32 ya trae los módulos `dht` y `umqtt.simple`.
- **Publicar y suscribirse:** el ESP32 publica en un tema; el broker `test.mosquitto.org` lo entrega a quien esté
  suscrito a ese tema; tu computadora se suscribe con `mosquitto_sub`.
- **Un tema único y aleatorio:** el tema lleva un texto al azar para no cruzarse con los de otras personas.

> **Aviso:** `test.mosquitto.org` es un broker **público y solo para pruebas**. El puerto 1883 no cifra ni pide
> usuario: cualquiera que conozca tu tema puede leer lo que mandas, y el servidor puede reiniciarse o ir lento. **Nunca
> mandes datos reales, personales ni contraseñas.** El tráfico del Wi-Fi de Wokwi pasa además por un servidor público de
> Wokwi que lo monitorea.

## 1. Elige tu tema

En el código viene `ALEATORIO = "693e139e"`. Cámbialo por un texto tuyo, al azar, para que tu tema sea único. En la
terminal (con Python instalado):

```bash
python -c "import secrets; print(secrets.token_hex(4))"
```

Te imprime ocho caracteres al azar, por ejemplo `693e139e`. Usa los tuyos en `main.py` y en el comando de la sección 3.

## 2. Ábrelo en Wokwi (en el navegador, sin iniciar sesión)

1. Abre un proyecto nuevo de MicroPython con el ESP32:
   https://wokwi.com/projects/new/micropython-esp32
2. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): el ESP32 y el DHT22 con sus tres
   cables (`VCC` a `3V3`, `GND` a `GND.2` y `SDA`, los datos, al pin `15`).
3. En la pestaña `main.py`, borra el ejemplo y pega [`main.py`](main.py) con tu texto en `ALEATORIO`.
4. Pulsa el botón verde. La consola imprime:

```text
Wi-Fi conectado
Conectado al broker
Enviado: {"h": 40.0, "t": 24.0}
```

y una línea `Enviado:` nueva cada 5 segundos.

## 3. Recíbelo en tu computadora

Con `mosquitto_sub` instalado (ver [`comandos.md`](comandos.md)), suscríbete al mismo tema:

```bash
mosquitto_sub -h test.mosquitto.org -t ayemi-lab/693e139e/clima -v
```

Cada mensaje llega en una línea, con el tema y los datos:

```text
ayemi-lab/693e139e/clima {"t": 24.0, "h": 40.0}
```

Con la simulación corriendo, haz clic en el sensor y mueve el deslizador de temperatura: el siguiente mensaje llega con
el valor nuevo. Para salir de `mosquitto_sub`, `Ctrl+C`.

## En la placa real

- Cambia `"Wokwi-GUEST", ""` por el nombre y la contraseña de tu red. No subas ese archivo a ningún repositorio público.
- Para un proyecto de verdad usa tu propio broker o uno con usuario y cifrado, nunca el de pruebas.
- El DHT22 también se vende como AM2302; MicroPython recomienda una resistencia pull-up en el pin de datos (revisa la
  hoja de datos de tu módulo).

Verificado el 24 de noviembre de 2026 en la documentación oficial de Wokwi, Espressif, MicroPython y Eclipse Mosquitto.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, proyecto nuevo de MicroPython con el ESP32 | https://wokwi.com/projects/new/micropython-esp32 |
| El Wi-Fi del ESP32 en Wokwi (`Wokwi-GUEST`, MQTT y el servidor público) | https://docs.wokwi.com/guides/esp32-wifi |
| El DHT22 en Wokwi | https://docs.wokwi.com/parts/wokwi-dht22 |
| Referencia rápida de MicroPython para el ESP32 | https://docs.micropython.org/en/latest/esp32/quickref.html |
| `umqtt.simple` (cliente MQTT de MicroPython) | https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple |
| El ESP32 (Espressif) | https://www.espressif.com/en/products/socs/esp32 |
| Eclipse Mosquitto y su descarga | https://mosquitto.org/download/ |
| Manual de `mosquitto_sub` | https://mosquitto.org/man/mosquitto_sub-1.html |
| Qué es MQTT (temas y comodines) | https://mosquitto.org/man/mqtt-7.html |
| El broker público de pruebas | https://test.mosquitto.org/ |

Ayemi no tiene relación con Wokwi, Espressif, MicroPython ni Eclipse Mosquitto.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
