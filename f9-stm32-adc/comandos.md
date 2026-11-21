# STM32 y el ADC · las líneas clave del video

En Wokwi no hay terminal: todo pasa en `sketch.ino`. Estas son las líneas que importan, tal cual están en el código.

| Línea | Qué hace |
|---|---|
| `const int POT = PA0;` | Pone nombre al pin A0, que es una entrada del ADC |
| `Serial.begin(115200);` | Abre el puerto serie a 115200 baudios (bits por segundo) |
| `analogReadResolution(12);` | Pide los 12 bits del ADC: lecturas de 0 a 4095 (sin esta línea, 10 bits: de 0 a 1023) |
| `int valor = analogRead(POT);` | Lee el voltaje del pin y lo devuelve como número entero |
| `int porcentaje = map(valor, 0, 4095, 0, 100);` | Pasa la lectura del rango 0–4095 al rango 0–100 |
| `Serial.print(valor);` | Escribe la lectura en el monitor serie |
| `Serial.println(" %");` | Escribe el signo de porcentaje y salta de línea |
| `delay(250);` | Espera un cuarto de segundo antes de la siguiente lectura |

## Lo que vas a ver en el monitor serie

Una línea por lectura: primero el valor crudo, luego el porcentaje. Con la perilla al mínimo (tecla Inicio) y al máximo (tecla Fin):

```text
0  0 %
4095  100 %
```

## Por qué `map()` corta los decimales

`map()` hace la cuenta con números enteros: el resultado es la parte entera de `valor × 100 / 4095`, sin redondear. Por eso dos lecturas cercanas pueden dar el mismo porcentaje. Si quieres decimales:

```cpp
float porcentaje = valor * 100.0 / 4095;
```

## El circuito

| Pin del potenciómetro | Pin de la Blue Pill |
|---|---|
| VCC | 3V3 |
| GND | GND |
| SIG | A0 |

El monitor serie de Wokwi se conecta a A9 y A10 (puerto serie de la Blue Pill) en `diagram.json`.

Fuentes: documentación de Wokwi (Blue Pill, monitor serie y potenciómetro), referencia de Arduino (`analogRead()`, `map()`, `Serial.begin()`, `Serial.println()`) y API de stm32duino (`analogReadResolution()`), consultadas el 21 de noviembre de 2026.
