# SQLite nivel 2: une tablas con JOIN y hazlo rápido con un índice

Cuarto video de la serie **Desarrollo web: stacks y frameworks** del Laboratorio Ayemi y segunda parte de
[SQLite](../h3-sqlite/). Dos tablas (proyectos y tareas), un `JOIN` que las une y el plan de SQLite antes y después
de crear un índice.

## Los cuatro pasos en `proyectos.js`

| Paso | Qué hace | Dónde se ve en `proyectos.js` |
|---|---|---|
| 1. Dos tablas | `proyectos` y `tareas`; cada tarea guarda el número de su proyecto en `proyecto_id` | Líneas 6–17 (y los datos de ejemplo, 19–27) |
| 2. JOIN | `JOIN proyectos ON proyectos.id = tareas.proyecto_id` une cada tarea con su proyecto; `WHERE` deja solo las de «Tienda» | Líneas 29–37 |
| 3. El plan | `EXPLAIN QUERY PLAN` antes de la consulta muestra cómo la va a resolver SQLite | Líneas 39–48 |
| 4. El índice | El plan, `CREATE INDEX idx_proyecto ON tareas (proyecto_id)` y el plan otra vez | Líneas 50–54 |

La guía paso a paso, con qué significa cada línea del plan, está en [`comandos.md`](comandos.md).

## Córrelo

Necesitas **Node.js 26**. El proyecto no tiene dependencias: **no corras `npm install`**. Desde esta carpeta:

```bash
npm start
```

Salida (sin las dos líneas de `>` que imprime npm):

```text
┌─────────┬─────────────────┬──────────┐
│ (index) │ texto           │ nombre   │
├─────────┼─────────────────┼──────────┤
│ 0       │ 'Crear la API'  │ 'Tienda' │
│ 1       │ 'Probar la API' │ 'Tienda' │
└─────────┴─────────────────┴──────────┘
Antes del índice:
SCAN tareas
SEARCH proyectos USING INTEGER PRIMARY KEY (rowid=?)
Después del índice:
SCAN proyectos
SEARCH tareas USING INDEX idx_proyecto (proyecto_id=?)
```

La base vive en memoria (`new Database(':memory:')`, como el primer ejemplo de la documentación de Node): cada vez
que lo corres empieza de cero, sin índice, y el «antes y después» sale igual. No deja ningún archivo.

### Notas

- **«Rápido», con honestidad:** con tres filas no notarás diferencia de tiempo; lo que cambia es el plan. Con
  muchas filas, buscar con un índice es mucho más rápido que recorrer toda la tabla, según la documentación de
  SQLite. El índice no cambia el resultado, solo cómo llega SQLite a él.
- **El formato del plan puede cambiar** entre versiones de SQLite (lo advierte sqlite.org). Si tu salida dice algo
  distinto, lo importante es lo mismo: `SCAN` recorre la tabla completa y `SEARCH … USING INDEX` usa el índice.
- **`Database` y `DatabaseSync`:** en Node 26 la clase se llama `Database`; `DatabaseSync` sigue funcionando como
  alias obsoleto.
- **`--disable-warning=ExperimentalWarning`:** `node:sqlite` es candidato a estable en Node 26 y emite un aviso de
  función experimental; `npm start` lo silencia, igual que en H1 y H3.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `EXPLAIN QUERY PLAN` | https://www.sqlite.org/eqp.html |
| `CREATE INDEX` | https://www.sqlite.org/lang_createindex.html |
| Cómo usa SQLite los índices | https://www.sqlite.org/queryplanner.html |
| Cómo resuelve SQLite los JOIN | https://www.sqlite.org/optoverview.html |
| Índices en columnas que apuntan a otra tabla | https://www.sqlite.org/foreignkeys.html |
| Módulo `node:sqlite` (Node.js 26) | https://nodejs.org/docs/latest-v26.x/api/sqlite.html |
| Node.js | https://nodejs.org/ |
| Video anterior: SQLite, la base de datos que es un solo archivo | [`../h3-sqlite/`](../h3-sqlite/) |

Datos verificados el 21 de noviembre de 2026 en `sqlite.org` y en la documentación oficial de Node.js. Ayemi no tiene
relación con el proyecto SQLite, con OpenJS Foundation ni con npm, Inc.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
