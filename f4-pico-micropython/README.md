# Una Raspberry Pi Pico simulada en el navegador, con MicroPython (Wokwi)

Una Raspberry Pi Pico (RP2040, doble núcleo Arm Cortex-M0+ de hasta 133 MHz) simulada en [Wokwi](https://wokwi.com/) lee un potenciómetro en GP26 con `read_u16()` (de 0 a 65535), ajusta el brillo de un LED en GP15 con PWM (`duty_u16()`) e imprime el valor y el voltaje en la consola. Al interrumpir con Ctrl+C se entra al REPL de MicroPython para darle órdenes en vivo.

## Usar

1. Abre un proyecto nuevo de MicroPython con la Raspberry Pi Pico: https://wokwi.com/projects/new/micropython-pi-pico (sin iniciar sesión).
2. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): Pico, potenciómetro en GP26, resistencia de 220 Ω y LED cian en GP15.
3. En la pestaña `main.py`, borra el ejemplo y pega [`main.py`](main.py). Wokwi carga y ejecuta `main.py` automáticamente al iniciar la simulación.
4. Pulsa el botón verde de iniciar simulación. Haz clic en la perilla y muévela con el ratón o con el teclado: `Izquierda` / `Derecha` (ajuste fino), `Re Pág` / `Av Pág` (ajuste grueso) e `Inicio` / `Fin` (`Home` / `End`) para llevarla a los extremos (0 y 65535).
5. Con la simulación corriendo, haz clic en la consola y pulsa `Ctrl+C` para detener `main.py` y entrar al indicador `>>>` del REPL. Escribe estas órdenes, una por línea:

```text
led.duty_u16(0)
led.duty_u16(65535)
```

La primera apaga el LED y la segunda lo prende al máximo (el objeto `led` queda disponible en el REPL tras interrumpir `main.py`).

## Para tomar en cuenta

- **Un solo núcleo simulado:** Wokwi simula solo uno de los dos núcleos Arm Cortex-M0+ del RP2040.
- **Convertidor de 12 bits y rango de 16 bits:** el ADC del RP2040 es de 12 bits, pero `read_u16()` en MicroPython entrega un entero de 0 a 65535, el mismo rango que acepta `duty_u16()`.
- **Especificaciones de la placa:** 264 kB de SRAM, 2 MB de memoria flash en placa, 26 pines GPIO multifunción y LED integrado en GP25. Si el proyecto necesita Wi-Fi, existe la Pico W.
- **En la placa física:** MicroPython se instala arrastrando el archivo UF2 al volumen que monta la Pico.

Verificado el 16 de noviembre de 2026 en la documentación oficial de Wokwi, Raspberry Pi y MicroPython.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, proyecto nuevo de MicroPython con la Pico | https://wokwi.com/projects/new/micropython-pi-pico |
| La Pico en Wokwi (funciones simuladas) | https://docs.wokwi.com/parts/wokwi-pi-pico |
| Guía de MicroPython de Wokwi | https://docs.wokwi.com/guides/micropython |
| Referencia rápida de MicroPython para el RP2 | https://docs.micropython.org/en/latest/rp2/quickref.html |
| La serie Pico (Raspberry Pi) | https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html |

Ayemi no tiene relación con Wokwi ni con Raspberry Pi.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
