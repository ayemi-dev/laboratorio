# STM32 simulado: lee un potenciómetro con el ADC y míralo en el monitor serie

Continuación de [f3-stm32-wokwi](../f3-stm32-wokwi/) en la serie **Microcontroladores con herramientas modernas** del Laboratorio Ayemi. Una Blue Pill (STM32F103C8, ARM Cortex-M3) simulada en [Wokwi](https://wokwi.com/) lee un potenciómetro con su convertidor analógico (ADC) de 12 bits, de 0 a 4095; `map()` convierte esa lectura en porcentaje y el monitor serie muestra las dos cosas mientras giras la perilla. Tres cables, dieciocho líneas y ninguna librería.

## Usar

1. Abre un proyecto nuevo con STM32: https://wokwi.com/projects/new/st-nucleo-c031c6 (la lista de proyectos nuevos no trae la Blue Pill; al pegar el diagrama, la placa cambia).
2. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): Blue Pill y potenciómetro con VCC en 3V3, GND en GND y la señal (SIG) en A0. Los pines A9 y A10 van al monitor serie.
3. En `sketch.ino`, borra el ejemplo y pega [`sketch.ino`](sketch.ino).
4. Pulsa el botón verde de iniciar simulación. El monitor serie se abre solo con la primera línea.
5. Haz clic en la perilla y muévela con el ratón, con las flechas o con Re Pág y Av Pág; Inicio y Fin la llevan a los extremos. Cada línea del monitor muestra la lectura y su porcentaje, por ejemplo `4095  100 %` con la perilla al máximo.

Las líneas clave, explicadas una por una, están en [`comandos.md`](comandos.md).

## Para tomar en cuenta

- **10 o 12 bits:** en el núcleo de Arduino para STM32 (stm32duino), `analogRead()` devuelve 10 bits por defecto, como un Arduino Uno. `analogReadResolution(12)` pide los 12 bits del convertidor del STM32.
- **`map()` trabaja con enteros:** corta los decimales, no redondea. Si necesitas decimales, haz la cuenta con `float`.
- **Lo que Wokwi simula del ADC:** solo la conversión básica del ADC1; el ADC2 y el DMA todavía no. Revisa la tabla de la página de la Blue Pill antes de diseñar algo que dependa de ellos.
- **Fila de compilación:** sin iniciar sesión, la compilación puede esperar unos segundos en fila.

Verificado el 21 de noviembre de 2026 en la documentación de Wokwi, Arduino y stm32duino, y en la hoja de datos de ST.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, nuevo proyecto con STM32 | https://wokwi.com/projects/new/st-nucleo-c031c6 |
| Blue Pill en Wokwi (funciones simuladas) | https://docs.wokwi.com/parts/board-stm32-bluepill |
| Monitor serie de Wokwi | https://docs.wokwi.com/guides/serial-monitor |
| Potenciómetro en Wokwi | https://docs.wokwi.com/parts/wokwi-potentiometer |
| `analogRead()` (Arduino) | https://docs.arduino.cc/language-reference/en/functions/analog-io/analogRead/ |
| `map()` (Arduino) | https://docs.arduino.cc/language-reference/en/functions/math/map/ |
| API del núcleo de Arduino para STM32 | https://stm32duino.github.io/latest/API/ |
| Hoja de datos del STM32F103C8 (ST) | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf |
| Video anterior: el STM32 con perilla, LED y OLED | [`../f3-stm32-wokwi/`](../f3-stm32-wokwi/) |

Ayemi no tiene relación con Wokwi, Arduino ni STMicroelectronics.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
