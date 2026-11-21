# Mundo abierto en miniatura · cómo abrir y modificar la demo

Guía del video. Cada comando va en su propia línea y se copia tal cual. Funciona igual en Windows, Mac y Linux.

## 1. Consigue el archivo

**Opción fácil:** entra a la carpeta `g11-mundo-abierto` del repositorio en GitHub, abre `mundo.html` y usa el botón de descarga del archivo («Download raw file»).

**Con la terminal** (Git Bash en Windows, Terminal en Mac o Linux), descarga solo el archivo:

```sh
curl -O https://raw.githubusercontent.com/ayemi-dev/laboratorio/main/g11-mundo-abierto/mundo.html
```

O todo el repositorio del Laboratorio, con Git (lo viste en [Git y GitHub](../g2-git-github/)):

```sh
git clone https://github.com/ayemi-dev/laboratorio.git
cd laboratorio/g11-mundo-abierto
```

En **Windows PowerShell 5.1**, `curl` es otro nombre de `Invoke-WebRequest`; ahí usa:

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/ayemi-dev/laboratorio/main/g11-mundo-abierto/mundo.html -OutFile mundo.html
```

## 2. Ábrelo

Doble clic en `mundo.html`: se abre en tu navegador. No necesita internet ni instalar nada.

Para abrir un modo directo, agrega su nombre al final de la dirección en el navegador: `mundo.html#bloques`, `mundo.html#detalle`, `mundo.html#camino` o `mundo.html#todo`.

| Tecla | Qué hace |
|---|---|
| `1` | Modo 1 · El mapa se carga por bloques |
| `2` | Modo 2 · Detalle según la distancia |
| `3` | Modo 3 · Cada personaje busca su camino (se ven las casillas que revisó A\*) |
| `4` | Todo junto |
| Flechas o `W` `A` `S` `D` | Mueves tú al jugador |
| `Enter` | Vuelve al recorrido automático |
| Espacio | Pausa |

## 3. Lo que ves en pantalla

- **Marco cian:** los 9 bloques con todo el detalle (ventanas y árboles).
- **Marco cian oscuro:** los 25 bloques cargados. Entre los dos marcos, solo color plano.
- **Fuera de los marcos:** gris oscuro. Esos bloques no se dibujan ni se revisan: no existen.
- **Puntos ámbar:** personajes cercanos que buscan su camino hacia ti. **Grises:** cargados pero lejos, quietos.
- **Línea cian clara:** la ruta que encontró A\*.

## 4. Cámbiale algo (con VS Code o cualquier editor)

Abre `mundo.html` en tu editor, cambia un número, guarda y recarga el navegador (`F5`).

| Prueba | Línea que cambias | Qué pasa |
|---|---|---|
| Más mundo cargado | `const RADIO_CARGA = 2;   // cargados` → pon `3` | Se cargan hasta 49 bloques (7 × 7) |
| Más detalle | `const RADIO_DETALLE = 1; // con detalle` → pon `2` | Ventanas y árboles en los 25 bloques cercanos |
| Personajes más lentos | `const PENSAR_CADA = 0.2; // segundos` → pon `0.5` | Piensan y se mueven cada medio segundo |
| A\* sin estimación | `const f = g[i] + estimar(i);` → `const f = g[i];` | Sigue encontrando la ruta más corta, pero revisa muchas más casillas (míralo en el modo 3): es el algoritmo de Dijkstra |

Con `RADIO_CARGA` en `3`, cerca de la orilla del mapa el contador baja: los bloques de afuera no existen.

## 5. Qué hace cada función

| Función | Para qué |
|---|---|
| `distanciaEnBloques(bx, by)` | Cuántos bloques hay entre un bloque y el del jugador |
| `dibujar()` | Recorre los 64 bloques y solo dibuja los que están a `RADIO_CARGA` o menos |
| `dibujarCasilla(x, y, conDetalle)` | Pinta una casilla; si está lejos, solo su color |
| `buscarCamino(origen, meta)` | A\*: la ruta más corta entre dos casillas, sin pasar por edificios ni por el agua |
| `pensarPersonajes()` | Cada 0.2 s, los personajes cercanos buscan su ruta y dan un paso |

---
Código: MIT · Guía: CC BY-SA 4.0 · Ayemi no tiene relación con Rockstar Games ni con Take-Two.
