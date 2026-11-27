# Busca texto al instante en SQLite con FTS5

Décimo video de la serie **Desarrollo web: stacks y frameworks** del Laboratorio Ayemi y continuación de
[SQLite nivel 2: JOIN e índices](../h4-sqlite-join-indices/). Veinte mil tareas de práctica, la misma búsqueda con
`LIKE` y con FTS5, y el orden por relevancia con `bm25`.

## Los cuatro pasos en `buscar.js`

| Paso | Qué hace | Dónde se ve en `buscar.js` |
|---|---|---|
| Datos falsos | Siete verbos, once cosas, trece lugares y cinco notas que se combinan por número de fila | Líneas 6–25 |
| 1. Veinte mil tareas | La tabla `tareas (id, texto)` y un ciclo que inserta 20 000 textos armados con esas listas | Líneas 27–43 |
| 2. FTS5 | `CREATE VIRTUAL TABLE buscador USING fts5(texto)` y se llena con las tareas, conservando su `id` como `rowid` | Líneas 45–51 |
| 3. LIKE contra MATCH | `medir` corre cada conteo 20 veces y saca el promedio en milisegundos; `LIKE '%sensor%'` en `tareas`, `MATCH 'sensor'` en `buscador` | Líneas 53–72 |
| 4. Relevancia | `ORDER BY bm25(buscador)` y `LIMIT 3`: las tres más relevantes | Líneas 74–83 |

La guía paso a paso, con qué significa cada parte y una práctica de cinco minutos, está en
[`comandos.md`](comandos.md).

## Córrelo

Necesitas **Node.js 26**. El proyecto no tiene dependencias: **no corras `npm install`**. Desde esta carpeta:

```bash
npm start
```

Salida (sin las dos líneas de `>` que imprime npm; los tiempos son de una corrida en la máquina de la demo y en la tuya
serán otros):

```text
Tareas: 20000
LIKE: 5455 filas en 15.72 ms
FTS5: 5455 filas en 0.72 ms
Las 3 más relevantes:
Soldar el sensor del patio y otro sensor
Probar el sensor del laboratorio y otro sensor
Calibrar el sensor del invernadero y otro sensor
```

La base vive en memoria (`new Database(':memory:')`): cada vez que lo corres se arma de cero, con los mismos datos, y
no deja ningún archivo.

### Notas

- **Los datos son falsos.** Se generan combinando listas por número de fila, sin azar: siempre son las mismas 20 000
  tareas y siempre hay 5455 con la palabra «sensor».
- **Por qué LIKE revisa todo:** con `%` al inicio del patrón, SQLite no puede usar un índice para `LIKE` (lo dice
  sqlite.org, «The LIKE Optimization»): lee las 20 000 filas, una por una. FTS5 guarda su propio índice de palabras y
  `MATCH` va directo a las filas que tienen la palabra.
- **Los tiempos, con honestidad:** con 20 000 filas las dos búsquedas son rápidas para una persona; la diferencia crece
  con la tabla. sqlite.org da un ejemplo con FTS3 (otro módulo de texto completo de SQLite) y una tabla grande: unos
  0.03 s con `MATCH` contra 22.5 s con `LIKE`, en una PC de escritorio.
- **bm25:** mientras mejor coincide una fila, más chico es el número que devuelve `bm25()`; por eso `ORDER BY
  bm25(buscador)` deja arriba lo más relevante. Aquí ganan las tareas que dicen «sensor» dos veces (empatan entre sí y
  salen por orden de `id`). Atajo: `ORDER BY rank` hace lo mismo.
- **El buscador no se actualiza solo:** `buscador` es otra tabla, llenada una vez con las tareas. Si agregas tareas
  después, también tienes que insertarlas en `buscador`.
- **`Database` y `DatabaseSync`:** en Node 26 la clase se llama `Database`; `DatabaseSync` sigue funcionando como
  alias obsoleto.
- **`--disable-warning=ExperimentalWarning`:** `node:sqlite` es candidato a estable en Node 26; `npm start` silencia
  su aviso, igual que en H1, H3 y H4.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| FTS5 (tabla virtual, `MATCH`, `bm25`, `rank`, tokenizador) | https://www.sqlite.org/fts5.html |
| `LIKE` y el `%` | https://www.sqlite.org/lang_expr.html |
| Por qué `LIKE` con `%` al inicio no usa índice | https://www.sqlite.org/optoverview.html |
| Ejemplo de tiempos con una tabla grande (FTS3) | https://www.sqlite.org/fts3.html |
| Módulo `node:sqlite` (Node.js 26) | https://nodejs.org/docs/latest-v26.x/api/sqlite.html |
| `performance.now()` | https://nodejs.org/docs/latest-v26.x/api/perf_hooks.html |
| Video anterior: SQLite nivel 2, JOIN e índices | [`../h4-sqlite-join-indices/`](../h4-sqlite-join-indices/) |

Datos verificados el 27 de noviembre de 2026 en `sqlite.org` y en la documentación oficial de Node.js. Ayemi no tiene
relación con el proyecto SQLite, con OpenJS Foundation ni con npm, Inc.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
