# Tu primera API: Node y SQLite con GET y POST

Video de la serie **Desarrollo web** del Laboratorio Ayemi y continuación de
[SQLite nivel 2: une tablas con JOIN](../h4-sqlite-join-indices/) y de [React nivel 2: trae datos de una API](../h5-react-fetch/).

## El caso

Las tablas de proyectos y tareas de H4 ahora responden por HTTP: una ruta para leer y otra para guardar. Lo que manda
el usuario entra a SQLite como **parámetro** (`?`), nunca pegado dentro del SQL. Por eso un texto que intenta borrar
la tabla se guarda como texto.

| Paso | Dónde | Qué pasa |
|---|---|---|
| 1. La base | `new Database('tareas.db')` | Las dos tablas de H4, ahora en un archivo. `INSERT OR IGNORE` crea los proyectos una sola vez |
| 2. Leer | `GET /tareas` | Devuelve cada tarea con su proyecto, con el `JOIN` de H4 |
| 3. Guardar | `POST /tareas` | `express.json()` lee el JSON; la tarea se guarda y la API responde `201` (creado) con su `id` |
| 4. Parámetros | `VALUES (?, ?)` y `crear.run(texto, proyecto_id)` | Cada `?` se llena, en orden, con un valor que llega aparte del SQL |
| 5. Probar | `curl` | `curl --json @t1.json …` manda el archivo JSON en un POST |

Según la documentación de Node.js: «Parameters also offer protection against SQL injection attacks. For these
reasons, prepared statements are preferred over hand-crafted SQL strings when handling user input.»

El código está en [`servidor.js`](servidor.js), con [`package.json`](package.json) y los dos archivos de prueba
[`t1.json`](t1.json) y [`t2.json`](t2.json). La guía completa, con cómo correrla, cada parte explicada, los avisos y una
práctica de cinco minutos, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| SQLite en Node.js (`node:sqlite`) | https://nodejs.org/docs/latest-v26.x/api/sqlite.html |
| Parámetros en SQLite | https://www.sqlite.org/lang_expr.html |
| `INSERT OR IGNORE` | https://www.sqlite.org/lang_conflict.html |
| Express 5: `app.get`, `app.post`, `app.listen` | https://expressjs.com/en/5x/api/application |
| Express 5: `express.json()` | https://expressjs.com/en/5x/api/express/ |
| Express 5: `res.status` y `res.json` | https://expressjs.com/en/5x/api/response/ |
| `201 Created` | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/201 |
| curl (`--json`) | https://curl.se/docs/manpage.html |
| Video anterior de SQLite: une tablas con JOIN | [`../h4-sqlite-join-indices/`](../h4-sqlite-join-indices/) |

Datos verificados el 22 de noviembre de 2026 en nodejs.org, expressjs.com, sqlite.org, curl.se y MDN. Ayemi no tiene
relación con OpenJS Foundation, Express, SQLite, curl ni Mozilla.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
