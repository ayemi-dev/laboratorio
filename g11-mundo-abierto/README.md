# ¿Cómo se programa un mundo como el de GTA?

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. GTA VI salió el 19 de noviembre de 2026, pero no encontramos detalles técnicos oficiales de cómo Rockstar programó su mundo. Así que hicimos una demo propia con la regla de fondo de cualquier mundo abierto: **el mundo solo existe cerca de ti.**

**Ayemi no tiene relación con Rockstar Games ni con Take-Two.** Esta demo es nuestra y no usa nada del juego: ni imágenes, ni código, ni datos.

## La demo: `mundo.html`

Un solo archivo. No se instala nada: ábrelo con doble clic y se ve en tu navegador. Las instrucciones paso a paso están en [`comandos.md`](comandos.md).

| Parte | Qué hace la demo | Dónde está en el código |
|---|---|---|
| **1 · Mapa por bloques** | El mapa de 48 × 48 casillas se parte en 64 bloques de 6 × 6. Solo se cargan los que están a 2 bloques o menos del jugador: 25 de 64 | `distanciaEnBloques()` y `RADIO_CARGA` |
| **2 · Nivel de detalle** | Los 9 bloques más cercanos se dibujan con ventanas y árboles; los demás cargados, con un color plano | `dibujarCasilla()` y `RADIO_DETALLE` |
| **3 · Caminos con A\*** | Los personajes cercanos (ámbar) buscan la ruta más corta hacia ti con A\*, esquivando edificios y el lago. Los cargados pero lejanos (gris) se quedan quietos | `buscarCamino()` y `pensarPersonajes()` |

A\* elige siempre la casilla con la **f** más baja: **f = lo recorrido + lo que falta** (lo que falta se estima con los pasos en línea recta por la cuadrícula).

| Tecla | Qué hace |
|---|---|
| `1` `2` `3` `4` | Modos: bloques, detalle, camino y todo |
| Flechas o `W` `A` `S` `D` | Mueves tú al jugador |
| `Enter` | Vuelve al recorrido automático |
| Espacio | Pausa |

## Cómo se hace en los motores de verdad

| Idea | Fuente |
|---|---|
| Celdas que se cargan y descargan según dónde está el jugador (Unreal Engine: World Partition) | https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine |
| Versiones simplificadas para lo lejano y lo no cargado (Unreal Engine: HLOD) | https://dev.epicgames.com/documentation/unreal-engine/world-partition-hierarchical-level-of-detail-in-unreal-engine |
| Nivel de detalle (Unity) | https://docs.unity3d.com/Manual/LevelOfDetail.html |
| Búsqueda de caminos con malla de navegación (Unreal Engine) | https://dev.epicgames.com/documentation/en-us/unreal-engine/navigation-system-in-unreal-engine |
| Mapas de casillas: dibujar solo lo que se ve (MDN) | https://developer.mozilla.org/en-US/docs/Games/Techniques/Tilemaps |
| A\*: Hart, Nilsson y Raphael (1968), *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100-107 | https://doi.org/10.1109/TSSC.1968.300136 |
| Nivel de detalle: Clark (1976), *Communications of the ACM*, 19(10), 547-554 | https://doi.org/10.1145/360349.360354 |

## Lo oficial de GTA VI

| Dato | Fuente |
|---|---|
| Salió el 19 de noviembre de 2026 en PlayStation 5 y Xbox Series X\|S | https://www.take2games.com/ir/news/rockstar-games-announces-pre-orders-grand-theft-auto-vi y https://www.rockstargames.com/VI |
| Rockstar tiene un motor propio, RAGE (Rockstar Advanced Game Engine); con él hizo GTA IV | https://ir.take2games.com/static-files/53773798-9091-42f8-bb65-6bda2b26b4a3 |

Datos verificados el 20 de noviembre de 2026. Ninguna fuente oficial dice qué técnicas usa GTA VI: lo de esta carpeta es cómo se programa un mundo abierto en general.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
