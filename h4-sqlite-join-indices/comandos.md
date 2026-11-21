# SQLite nivel 2 · JOIN e índice, paso a paso

## 1. Prepara la carpeta

Crea una carpeta vacía con dos archivos de esta guía: `proyectos.js` y `package.json`. Necesitas **Node.js 26**
(comprueba con `node --version`). No hay dependencias: **no corras `npm install`**.

## 2. Córrelo

Un solo comando, desde esa carpeta:

```bash
npm start
```

`npm start` corre el script `start` de `package.json`: `node --disable-warning=ExperimentalWarning proyectos.js`.

## 3. Lee la salida, parte por parte

### La tabla del JOIN

```text
┌─────────┬─────────────────┬──────────┐
│ (index) │ texto           │ nombre   │
├─────────┼─────────────────┼──────────┤
│ 0       │ 'Crear la API'  │ 'Tienda' │
│ 1       │ 'Probar la API' │ 'Tienda' │
└─────────┴─────────────────┴──────────┘
```

Cada tarea sale con el nombre de su proyecto. `JOIN proyectos ON proyectos.id = tareas.proyecto_id` junta cada fila
de `tareas` con la fila de `proyectos` cuyo `id` coincide con su `proyecto_id`; `WHERE proyectos.nombre = 'Tienda'`
deja solo las del proyecto Tienda. «Escribir el post» es del proyecto 2 (Blog), por eso no aparece.

### El plan antes del índice

```text
Antes del índice:
SCAN tareas
SEARCH proyectos USING INTEGER PRIMARY KEY (rowid=?)
```

- `SCAN tareas`: recorre la tabla `tareas` completa, fila por fila.
- `SEARCH proyectos USING INTEGER PRIMARY KEY (rowid=?)`: por cada tarea, busca su proyecto directo por el `id`
  (la llave primaria ya funciona como índice).

### El plan después del índice

```text
Después del índice:
SCAN proyectos
SEARCH tareas USING INDEX idx_proyecto (proyecto_id=?)
```

- `SEARCH tareas USING INDEX idx_proyecto (proyecto_id=?)`: ahora las tareas se buscan en el índice, sin recorrer
  toda la tabla.
- `SCAN proyectos`: SQLite cambió el orden. Puede reordenar las tablas de un `JOIN` como le convenga: recorre
  `proyectos` (aquí, dos filas) y por cada proyecto busca sus tareas en el índice.

`SCAN` significa recorrer la tabla completa; `SEARCH`, visitar solo una parte de las filas.

## 4. Lo que conviene recordar

- **Indexa la columna que une las tablas** (aquí, `proyecto_id`). sqlite.org dice que un índice en esas columnas
  «casi siempre» conviene.
- **El índice no cambia el resultado**, solo cómo llega SQLite a él: la tabla del JOIN es la misma con o sin índice.
- **Con tres filas no se nota la diferencia de tiempo.** En tablas grandes, buscar con un índice es mucho más rápido
  que recorrer toda la tabla.
- **El texto del plan puede cambiar** entre versiones de SQLite; fíjate en `SCAN` contra `SEARCH … USING INDEX`.

## 5. Pruébalo tú

- Cambia `'Tienda'` por `'Blog'` en `proyectos.js` y vuelve a correr `npm start`: sale «Escribir el post».
- Borra las dos líneas de `CREATE INDEX` y compara: los dos planes salen iguales, con `SCAN tareas`.

Fuentes: `https://www.sqlite.org/eqp.html`, `https://www.sqlite.org/lang_createindex.html`,
`https://www.sqlite.org/queryplanner.html`, `https://www.sqlite.org/optoverview.html`,
`https://www.sqlite.org/foreignkeys.html` y `https://nodejs.org/docs/latest-v26.x/api/sqlite.html`, consultadas el
21 de noviembre de 2026.
