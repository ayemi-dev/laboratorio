# SQLite: la base de datos que es un solo archivo

Tercer video de la serie **Desarrollo web: stacks y frameworks** del Laboratorio Ayemi. SQLite es una biblioteca en proceso que implementa un motor de base de datos SQL autocontenido, sin servidor aparte, sin instalación y transaccional dentro de un solo archivo.

## Los tres pasos en `tareas.js`

| Paso | Qué hace | Dónde se ve en `tareas.js` |
|---|---|---|
| 1. Crear la tabla | `CREATE TABLE IF NOT EXISTS tareas` crea la tabla con `id INTEGER PRIMARY KEY` (SQLite asigna el número solo) | Líneas 7–12 |
| 2. Insertar | `INSERT INTO tareas (texto) VALUES (?)` inserta la tarea que pasas en `process.argv[2]` | Líneas 15–18 |
| 3. Consultar | `SELECT id, texto FROM tareas` devuelve todas las filas sin cambiar la base y las imprime con `console.table` | Líneas 21–24 |

## Córrelo

Necesitas **Node.js 26** (se probó con `v26.13.1`, que incluye SQLite `3.54.1`). El proyecto no tiene dependencias: **no corras `npm install`**.

```bash
npm start -- "Crear la API"
npm start -- "Aprender SQLite"
```

Salida real de la segunda corrida (muestra que la primera tarea quedó guardada en `tareas.db`):

```text
> h3-sqlite@1.0.0 start
> node --disable-warning=ExperimentalWarning tareas.js Aprender SQLite

┌─────────┬────┬───────────────────┐
│ (index) │ id │ texto             │
├─────────┼────┼───────────────────┤
│ 0       │ 1  │ 'Crear la API'    │
│ 1       │ 2  │ 'Aprender SQLite' │
└─────────┴────┴───────────────────┘
```

### Notas sobre `node:sqlite` en Node 26

- **`Database` y `DatabaseSync`:** en Node 26.11 la clase `DatabaseSync` (la usada en [H1](../h1-stack-node/)) se renombró a `Database`; `DatabaseSync` sigue funcionando como alias obsoleto.
- **`--disable-warning=ExperimentalWarning`:** `node:sqlite` está como candidato a estable (estabilidad `1.2`) en Node 26 y emite un aviso de función experimental; `npm start` lo silencia con esa bandera, igual que en H1.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Qué es SQLite | https://www.sqlite.org/about.html |
| Sin servidor (`serverless`) | https://www.sqlite.org/serverless.html |
| Sin configuración (`zeroconf`) | https://www.sqlite.org/zeroconf.html |
| Dominio público (`copyright`) | https://www.sqlite.org/copyright.html |
| Módulo `node:sqlite` (Node.js 26) | https://nodejs.org/docs/latest-v26.x/api/sqlite.html |
| `CREATE TABLE` | https://www.sqlite.org/lang_createtable.html |
| `INSERT` | https://www.sqlite.org/lang_insert.html |
| `SELECT` | https://www.sqlite.org/lang_select.html |
| Node.js | https://nodejs.org/ |

Datos verificados el 17 de noviembre de 2026 en `sqlite.org` y en la documentación oficial de Node.js. Ayemi no tiene relación con el proyecto SQLite, con OpenJS Foundation ni con npm, Inc.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
