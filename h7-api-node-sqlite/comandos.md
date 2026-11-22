# Tu primera API con Node y SQLite · la guía del video

## Lo que necesitas

- Node.js 26 (https://nodejs.org/). Trae SQLite incluido: no hay que instalar una base aparte.
- curl. Viene en Git Bash, en la Terminal de Mac y en casi todas las de Linux. Necesitas la versión 7.82.0 o más
  nueva para `--json` (revísala con `curl --version`).
- Esta carpeta: `servidor.js`, `package.json`, `t1.json` y `t2.json`. Descárgala o clona este repositorio.

**En Windows, usa Git Bash.** En PowerShell 5.1, `curl` es otro comando (`Invoke-WebRequest`) y no entiende `--json`;
ahí tendrías que escribir `curl.exe`, y las comillas del JSON cambian. Con Git Bash, los comandos de esta guía se copian
tal cual.

## Córrela en dos terminales

**Terminal 1, la API** (desde esta carpeta). Instala Express, arranca y crea `tareas.db`:

```bash
npm install
npm start
```

Verás `API en el puerto 3000`. Déjala corriendo.

**Terminal 2, las pruebas** (desde esta misma carpeta, para que curl encuentre los JSON):

```bash
curl localhost:3000/tareas
curl --json @t1.json localhost:3000/tareas
curl --json @t2.json localhost:3000/tareas
curl localhost:3000/tareas
```

1. El primer GET responde `[]`: la tabla de tareas empieza vacía.
2. El POST de `t1.json` responde con el `id` de la tarea nueva (`1`).
3. El POST de `t2.json` manda un texto que intenta colar SQL: `'); DROP TABLE tareas; --`. Responde con el `id` `2`.
4. El último GET devuelve las dos tareas con su proyecto. La segunda tiene ese texto **guardado como texto**, y la
   tabla sigue ahí.

## Cada parte del código

| Parte | Qué hace |
|---|---|
| `new Database('tareas.db')` | Abre la base en un archivo (si no existe, la crea). En H4 vivía en memoria, con `':memory:'`; una API necesita que los datos se queden |
| `CREATE TABLE IF NOT EXISTS` | Las dos tablas de H4: `proyectos` y `tareas`, unidas por `proyecto_id`. Solo se crean la primera vez |
| `INSERT OR IGNORE INTO proyectos` | Crea `Tienda` (1) y `Blog` (2). Al volver a arrancar, como esos `id` ya existen, SQLite salta esas filas sin error |
| `app.use(express.json())` | Lee el cuerpo de las peticiones que llegan con `Content-Type: application/json` y lo deja en `req.body` |
| `app.set('json spaces', 2)` | Ordena el JSON de las respuestas con dos espacios de sangría, para que se lea en la terminal |
| `listar` | La consulta del GET, preparada una sola vez: el `JOIN` de H4, con el nombre del proyecto como `proyecto` |
| `app.get('/tareas', …)` | Responde con todas las filas (`listar.all()`); sin filas, un arreglo vacío |
| `crear` | El `INSERT` con dos `?`: los lugares donde van a entrar los valores |
| `app.post('/tareas', …)` | Toma `texto` y `proyecto_id` del JSON y los pasa a `crear.run(...)`, en el orden de los `?` |
| `res.status(201)` | Responde «201 Created»: se creó algo nuevo. `r.lastInsertRowid` es el `id` que SQLite le dio |
| `app.listen(3000, …)` | Pone el servidor a escuchar en el puerto 3000 |

## Por qué el texto de `t2.json` no hace daño

El SQL de `crear` está fijo: `INSERT INTO tareas (texto, proyecto_id) VALUES (?, ?)`. SQLite lo prepara **antes** de
ver los datos. Cuando llega la petición, `run` llena cada `?` con un valor. Ese valor nunca se convierte en parte del
SQL: es solo el contenido de una columna. Por eso `'); DROP TABLE tareas; --` se guarda como cualquier otro texto.

La documentación de Node.js lo dice así: «Parameters also offer protection against SQL injection attacks. For these
reasons, prepared statements are preferred over hand-crafted SQL strings when handling user input.»

La regla práctica: **nunca armes el SQL juntando texto con lo que manda el usuario.** Escribe un `?` y pasa el valor
a `run`, `get` o `all`.

## Avisos

- **Lo que llega en `req.body` no es confiable.** La documentación de Express pide validarlo antes de usarlo. Esta API
  todavía no lo hace: es la práctica 4.
- **Los parámetros protegen de la inyección de SQL, no de todo.** No revisan que el texto tenga sentido, ni que el
  proyecto exista: si mandas `"proyecto_id": 9`, la tarea se guarda, pero el GET no la muestra, porque el `JOIN` no
  encuentra el proyecto 9.
- **Borra `tareas.db` para empezar de cero.** Con la API detenida, borra el archivo y vuelve a correr `npm start`.
- **`--disable-warning=ExperimentalWarning`** en el script `start` solo silencia el aviso de que `node:sqlite` todavía
  no es estable del todo (en Node 26 es «candidato a estable»).

## Practica en cinco minutos

Con la API corriendo en la terminal 1:

1. **Los datos se quedan.** Detén la API con Ctrl + C, vuelve a arrancarla y pide las tareas: siguen ahí.

   ```bash
   npm start
   ```

   ```bash
   curl localhost:3000/tareas
   ```

2. **El código 201.** Con `-i`, curl muestra también la respuesta del servidor. La primera línea dice `201 Created`:

   ```bash
   curl -i --json @t1.json localhost:3000/tareas
   ```

3. **Otro proyecto.** Abre `t1.json`, cambia `"proyecto_id": 1` por `"proyecto_id": 2`, guarda y mándalo otra vez. En
   el GET, esa tarea sale con `"proyecto": "Blog"`.

   ```bash
   curl --json @t1.json localhost:3000/tareas
   curl localhost:3000/tareas
   ```

4. **Valida lo que llega.** Manda un JSON vacío:

   ```bash
   curl --json '{}' localhost:3000/tareas
   ```

   La API responde con un error 500, porque `texto` no llegó y nadie lo revisó antes de guardar. Arréglalo en `servidor.js`: al
   principio de la ruta POST, justo después de `const { texto, proyecto_id } = req.body;`, agrega:

   ```js
   if (typeof texto !== 'string' || !texto) {
     return res.status(400)
       .json({ error: 'Falta el texto' });
   }
   ```

   Detén la API con Ctrl + C, arráncala con `npm start` y repite el comando: ahora responde `400` con
   `"error": "Falta el texto"`.

## Enlaces

- SQLite en Node.js (`Database`, `prepare`, `run`, `all` y los parámetros):
  https://nodejs.org/docs/latest-v26.x/api/sqlite.html
- Parámetros en SQLite: https://www.sqlite.org/lang_expr.html
- `INSERT OR IGNORE`: https://www.sqlite.org/lang_conflict.html
- Express 5, aplicación (`app.get`, `app.post`, `app.set`, `app.listen`): https://expressjs.com/en/5x/api/application
- Express 5, `express.json()`: https://expressjs.com/en/5x/api/express/
- Express 5, respuesta (`res.status`, `res.json`): https://expressjs.com/en/5x/api/response/
- `201 Created`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/201
- curl, opción `--json`: https://curl.se/docs/manpage.html

Datos verificados el 22 de noviembre de 2026 en nodejs.org, expressjs.com, sqlite.org, curl.se y MDN.
