# El mismo LED, compilado en tu compu y listo para simular en VS Code (PlatformIO + Wokwi)

El proyecto del LED parpadeante de [AF1](../af1-wokwi-arduino/) (Arduino Uno, ATmega328P a 16 MHz, LED «L» en el pin 13 con `LED_BUILTIN`), ahora como proyecto local de PlatformIO en VS Code, compilado en tu computadora y listo para simularse con la extensión Wokwi Simulator.

## Usar

1. Instala la extensión **PlatformIO IDE** en VS Code (corre en Windows, macOS y Linux; es de código abierto y sin cuotas de licencia).
2. Abre esta carpeta (`f6-wokwi-vscode/`) en VS Code.
3. Compila el proyecto con el botón **Build**, con `Ctrl+Alt+B`, o desde la terminal «PlatformIO Core (CLI)» con:

```text
pio run
```

La compilación genera `.pio/build/uno/firmware.hex` y `.pio/build/uno/firmware.elf`.

4. Para simularlo dentro de VS Code:
   - Instala la extensión **Wokwi Simulator** del Marketplace.
   - [`wokwi.toml`](wokwi.toml) apunta al `.hex` y al `.elf` que generó PlatformIO.
   - [`diagram.json`](diagram.json) describe el circuito (Arduino Uno).
   - Pide una licencia con `F1` → **Wokwi: Request a new License** (pide iniciar sesión con tu cuenta de Wokwi; la licencia personal dura 30 días, es gratis para proyectos de código abierto y de pago para uso comercial).
   - Arranca la simulación con `F1` → **Wokwi: Start Simulator**. Wokwi no compila: si cambias el código, vuelve a compilar y Wokwi recargará el firmware automáticamente.
5. Para llevarlo a una placa real conectada por USB, usa **PlatformIO: Upload** en la barra de PlatformIO.

## Para tomar en cuenta

- **Encabezado en C++:** en PlatformIO el código va en [`src/main.cpp`](src/main.cpp) y necesita `#include <Arduino.h>` al principio.
- **Configuración de placa:** [`platformio.ini`](platformio.ini) define `platform = atmelavr`, `board = uno` y `framework = arduino`.

Verificado el 17 de noviembre de 2026 en la documentación oficial de PlatformIO y Wokwi.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Qué es PlatformIO | https://docs.platformio.org/en/latest/what-is-platformio.html |
| PlatformIO IDE para VS Code | https://docs.platformio.org/en/latest/integration/ide/vscode.html |
| Arduino Uno en PlatformIO | https://docs.platformio.org/en/latest/boards/atmelavr/uno.html |
| Wokwi con PlatformIO | https://docs.wokwi.com/vscode/platformio |
| Primeros pasos y licencia de Wokwi para VS Code | https://docs.wokwi.com/vscode/getting-started |
| Licencia de Wokwi para VS Code | https://wokwi.com/license |
| Extensión Wokwi Simulator en el Marketplace | https://marketplace.visualstudio.com/items?itemName=wokwi.wokwi-vscode |

Ayemi no tiene relación con PlatformIO ni con Wokwi.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
