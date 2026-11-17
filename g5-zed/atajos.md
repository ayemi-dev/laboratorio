# Zed: comandos de instalación y atajos

Guía de referencia rápida del video **Zed: el editor que se presenta como el más rápido** (Laboratorio Ayemi, serie Herramientas de desarrollador).

## Instalación oficial

Un solo comando en Windows y Linux; en macOS descarga directa oficial:

| Sistema | Cómo instalarlo |
|---|---|
| **Windows (PowerShell)** | `winget install -e --id ZedIndustries.Zed` |
| **Linux (terminal)** | `curl -f https://zed.dev/install.sh \| sh` |
| **macOS** | Descarga directa desde https://zed.dev/download (o `brew install --cask zed`) |

En Windows, Zed requiere una tarjeta gráfica compatible con DirectX 11.

## Atajos principales

Los cuatro atajos esenciales para moverte en Zed:

| Atajo (Windows / Linux) | Atajo (macOS) | Qué hace |
|---|---|---|
| `Ctrl+P` | `Cmd+P` | Ir a un archivo (buscador rápido) |
| `Ctrl+Shift+P` | `Cmd+Shift+P` | Abrir la paleta de comandos |
| `Ctrl+O` | `Cmd+O` | Abrir una carpeta |
| `Ctrl+,` | `Cmd+,` | Abrir los ajustes (`settings.json`) |

## Si vienes de Visual Studio Code

Zed comparte la misma filosofía de paleta de comandos (`Ctrl+Shift+P` / `Cmd+Shift+P`) que Visual Studio Code:

1. **Importar ajustes:**
   - Durante el primer inicio, en la pantalla de bienvenida mediante la opción *Import Settings from VS Code*.
   - Posteriormente, desde la paleta de comandos ejecutando `zed: import vs code settings`.
   - **Nota oficial:** Zed importa los ajustes principales del editor para asemejar el comportamiento, pero no importa extensiones ni atajos de teclado.

2. **Modo Vim:**
   - Puede activarse con la casilla correspondiente en la pantalla de bienvenida.
   - O en cualquier momento desde la paleta de comandos con `workspace: toggle vim mode`.

3. **Colaboración en tiempo real:**
   - Puedes abrir carpetas y editar tus archivos locales sin iniciar sesión ni crear ninguna cuenta.
   - Para las funciones de edición colaborativa en tiempo real y en equipo, sí es necesario iniciar sesión.

## Datos de la herramienta

- **Versión comprobada:** 1.28.1 (11 de noviembre de 2026).
- **Licencia:** código abierto (GPL-3.0 o posterior, con componentes Apache-2.0).
- **Lenguaje:** el repositorio oficial está escrito principalmente en Rust con aceleración por GPU.
- **Fuentes oficiales:** https://zed.dev/ · https://zed.dev/docs/getting-started · https://zed.dev/docs/migrate/vs-code · https://zed.dev/docs/vim · https://zed.dev/docs/collaboration · https://github.com/zed-industries/zed
