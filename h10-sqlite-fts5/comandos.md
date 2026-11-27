# Busca texto al instante en SQLite con FTS5 · la guía del video

## 1. Lo que necesitas

- **Node.js 26** (https://nodejs.org/). Trae SQLite incluido, con FTS5. Comprueba la versión:

  ```bash
  node --version
  ```

- Esta carpeta, con `buscar.js` y `package.json`. No hay dependencias: **no corras `npm install`**.

**En Windows, usa Git Bash:** los comandos de esta guía se copian tal cual.

## 2. Córrelo

Desde esta carpeta:

```bash
npm start
```

`npm start` corre el script `start` de `package.json`: `node --disable-warning=ExperimentalWarning buscar.js`.

Si ves `no such module: fts5`, tu Node no trae FTS5: usa Node.js 26 de nodejs.org.

## 3. Lee la salida, parte por parte

```text
Tareas: 20000
```

El ciclo insertó 20 000 tareas. Cada texto se arma con `verbos[i % 7]`, `cosas[i % 11]`, `lugares[i % 13]` y
`notas[i % 5]`: el resto de dividir el número de fila escoge un elemento de cada lista. Sin azar: siempre salen las
mismas.

```text
LIKE: 5455 filas en 15.72 ms
FTS5: 5455 filas en 0.72 ms
```

- **Las dos cuentan lo mismo:** 5455 tareas dicen «sensor».
- **`LIKE '%sensor%'`** busca el pedazo «sensor» en cualquier parte del texto. Como el patrón empieza con `%`, SQLite
  no puede usar un índice: revisa las 20 000 filas.
- **`MATCH 'sensor'`** busca la palabra en el índice que FTS5 armó al llenar `buscador`: va directo a las filas que la
  tienen.
- **Los tiempos** son el promedio de 20 corridas de cada consulta, medidos con `performance.now()`. Cambian en cada
  corrida y en cada máquina; lo que se mantiene es que `MATCH` tarda menos.

```text
Las 3 más relevantes:
Soldar el sensor del patio y otro sensor
Probar el sensor del laboratorio y otro sensor
Calibrar el sensor del invernadero y otro sensor
```

`bm25()` calcula qué tan bien coincide cada fila: **mientras mejor coincide, más chico el número**. Por eso
`ORDER BY bm25(buscador)` (de menor a mayor) deja arriba lo más relevante. Aquí ganan las que dicen «sensor» dos veces;
empatan entre sí y salen por orden de `id`. Atajo: FTS5 trae una columna oculta, `rank`, que vale lo mismo que
`bm25()`, así que `ORDER BY rank` da el mismo orden.

## 4. Lo que conviene recordar

- **La tabla virtual no lleva tipos:** `fts5(texto)`, sin `TEXT` ni `PRIMARY KEY`. FTS5 da error si se los pones.
- **`rowid` une las dos tablas:** `INSERT INTO buscador (rowid, texto) SELECT id, texto FROM tareas` guarda en el
  buscador el mismo `id` de cada tarea. Con ese `rowid` puedes volver a la tabla `tareas`.
- **El buscador no se actualiza solo:** se llenó una vez. Si agregas tareas, insértalas también en `buscador`.
- **MATCH busca palabras completas; LIKE, pedazos.** Son herramientas distintas: si necesitas encontrar «ensor» dentro
  de «sensor», es `LIKE`.
- **FTS5 no distingue mayúsculas ni acentos** (con su separador de palabras por omisión, `unicode61`).

## 5. Practica en cinco minutos

Haz los cambios con estos comandos (o a mano, en `buscar.js`) y corre `npm start` después de cada uno.

**1. Acentos.** Busca «bateria», sin acento:

```bash
sed -i "s/%sensor%/%bateria%/; s/MATCH 'sensor'/MATCH 'bateria'/" buscar.js
npm start
```

`LIKE` cuenta 0 (el texto dice «batería», con acento) y `FTS5` cuenta 1818: quita los acentos al buscar.

**2. Mayúsculas.** Regresa a «sensor», pero en mayúsculas:

```bash
sed -i "s/%bateria%/%sensor%/; s/MATCH 'bateria'/MATCH 'SENSOR'/" buscar.js
npm start
```

`FTS5` cuenta 5455, igual que con minúsculas.

**3. Pedazos de palabra.** Busca «ensor»:

```bash
sed -i "s/%sensor%/%ensor%/; s/MATCH 'SENSOR'/MATCH 'ensor'/" buscar.js
npm start
```

`LIKE` cuenta 5455 (encuentra el pedazo dentro de «sensor») y `FTS5` cuenta 0 (no hay ninguna palabra «ensor»). Con 0
filas, la lista de relevantes sale vacía.

**4. Deja todo como estaba:**

```bash
sed -i "s/%ensor%/%sensor%/; s/MATCH 'ensor'/MATCH 'sensor'/" buscar.js
npm start
```

Vuelven los 5455 en las dos líneas y las tres tareas con «sensor» dos veces.

Fuentes: `https://www.sqlite.org/fts5.html`, `https://www.sqlite.org/lang_expr.html`,
`https://www.sqlite.org/optoverview.html`, `https://www.sqlite.org/fts3.html`,
`https://nodejs.org/docs/latest-v26.x/api/sqlite.html` y
`https://nodejs.org/docs/latest-v26.x/api/perf_hooks.html`, consultadas el 27 de noviembre de 2026.
