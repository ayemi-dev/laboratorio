# Un STM32 Blue Pill simulado en el navegador (Wokwi)

Una Blue Pill (STM32F103C8, ARM Cortex-M3) simulada en [Wokwi](https://wokwi.com/) lee un potenciómetro con su convertidor analógico de 12 bits (de 0 a 4095), ajusta el brillo de un LED con PWM y muestra el valor y el voltaje en una pantalla OLED SSD1306 por I2C. El graficador de la consola serie dibuja la curva.

## Usar

1. Abre un proyecto nuevo con STM32: https://wokwi.com/projects/new/st-nucleo-c031c6 (la lista de proyectos nuevos no trae la Blue Pill; al pegar el diagrama, la placa cambia).
2. En la pestaña `diagram.json`, reemplaza todo por [`diagram.json`](diagram.json): Blue Pill, OLED en I2C (SDA en B7, SCL en B6), potenciómetro en A0 y LED en A8.
3. En `sketch.ino`, borra el ejemplo y pega [`sketch.ino`](sketch.ino).
4. Agrega las librerías de [`libraries.txt`](libraries.txt) desde «Library Manager» (Adafruit SSD1306 y Adafruit GFX Library).
5. Pulsa el botón verde de iniciar simulación. Haz clic en la perilla y muévela con el ratón o con las teclas Re Pág y Av Pág (Inicio y Fin la llevan a los extremos). La pantalla, el LED y el graficador cambian al momento.

## Para tomar en cuenta

- **Sin Wi-Fi:** a diferencia del ESP32 de [f2-wokwi-esp32](../f2-wokwi-esp32/), el STM32F103 no tiene radio. Su fuerte es el control: temporizadores, convertidores y buses como I2C, SPI, USB y CAN.
- **Lo que Wokwi simula:** GPIO, USART, I2C, SPI, los temporizadores TIM1 a TIM4 (que usa `analogWrite()`) y el ADC1 en conversión básica. El DMA, el RTC y el ADC2 todavía no. Revisa la tabla de la página de la Blue Pill antes de diseñar algo que dependa de ellos.
- **Fila de compilación:** en el plan gratuito, la compilación puede esperar unos segundos en fila.
- **Núcleo de Arduino para STM32 (stm32duino):** `analogReadResolution(12)` pide los 12 bits completos del convertidor.

Verificado el 13 de noviembre de 2026 en la documentación de Wokwi y en la hoja de datos de ST.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Wokwi, nuevo proyecto con STM32 | https://wokwi.com/projects/new/st-nucleo-c031c6 |
| Blue Pill en Wokwi (funciones simuladas) | https://docs.wokwi.com/parts/board-stm32-bluepill |
| Hardware que soporta Wokwi | https://docs.wokwi.com/getting-started/supported-hardware |
| Hoja de datos del STM32F103C8 (ST) | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf |
| Planes de Wokwi | https://wokwi.com/pricing |

Ayemi no tiene relación con Wokwi ni con STMicroelectronics.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
