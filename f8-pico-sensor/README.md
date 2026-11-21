# Una Raspberry Pi Pico simulada lee temperatura y humedad con un DHT22 (Wokwi + MicroPython)

Video de la serie **Microcontroladores con herramientas modernas** del Laboratorio Ayemi. Continúa
[`f4-pico-micropython`](../f4-pico-micropython/): la misma Raspberry Pi Pico simulada en [Wokwi](https://wokwi.com/),
con MicroPython, ahora lee un sensor digital DHT22 cada 2 segundos y muestra la temperatura y la humedad en la consola.

- **Tres cables:** `VCC` a `3V3`, `GND` a una tierra de la Pico y `SDA` (datos) al pin `GP22`.
- **Sin instalar nada:** el MicroPython de la Pico ya trae el módulo `dht`.
- **Cuatro llamadas:** `dht.DHT22(Pin(22))` crea el sensor, `measure()` pide una lectura nueva, `temperature()` la da en
  grados Celsius y `humidity()` en porcentaje de humedad relativa.
- **Cada 2 segundos:** la documentación de MicroPython pide no consultar el DHT22 más de una vez cada dos segundos para
  tener la lectura más precisa.

## Ábrelo en Wokwi (en el navegador, sin iniciar sesión)

1. Abre un proyecto nuevo de MicroPython con la Raspberry Pi Pico:
   https://wokwi.com/projects/new/micropython-pi-pico
2. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): la Pico y el DHT22 con sus tres
   cables.
3. En la pestaña `main.py`, borra el ejemplo y pega [`main.py`](main.py). Wokwi carga y ejecuta `main.py` solo al
   iniciar la simulación.
4. Pulsa el botón verde. Cada 2 segundos la consola imprime dos líneas:

```text
Temperatura: 24.0 °C
Humedad: 40.0 %
```

5. Con la simulación corriendo, haz clic en el sensor: se abre una ventanita con dos deslizadores, temperatura y
   humedad. Muévelos y mira la siguiente lectura en la consola.

Las órdenes para probar el sensor a mano desde el REPL están en [`comandos.md`](comandos.md).

## En la placa real

- El DHT22 también se vende como **AM2302**; es el mismo sensor.
- MicroPython recomienda una **resistencia pull-up** en el pin de datos. Revisa la hoja de datos de tu módulo: el valor
  no lo da la documentación de MicroPython.
- Para instalar MicroPython en la Pico física, mira la guía de [`f4-pico-micropython`](../f4-pico-micropython/).

Verificado el 21 de noviembre de 2026 en la documentación oficial de Wokwi y MicroPython.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, proyecto nuevo de MicroPython con la Pico | https://wokwi.com/projects/new/micropython-pi-pico |
| El DHT22 en Wokwi (pines, atributos y deslizadores) | https://docs.wokwi.com/parts/wokwi-dht22 |
| La Pico en Wokwi | https://docs.wokwi.com/parts/wokwi-pi-pico |
| Guía de MicroPython de Wokwi | https://docs.wokwi.com/guides/micropython |
| El formato de `diagram.json` | https://docs.wokwi.com/diagram-format |
| Tutorial de MicroPython para sensores DHT | https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html |
| Referencia rápida de MicroPython para el RP2 | https://docs.micropython.org/en/latest/rp2/quickref.html |

Ayemi no tiene relación con Wokwi, Raspberry Pi ni MicroPython.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
