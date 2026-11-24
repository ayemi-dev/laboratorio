# Conecta tu React a tu propia API · la guía del video

## Lo que necesitas

- Node.js 26 (https://nodejs.org/). Vite pide Node 20.19 o 22.12 como mínimo; la API usa `node:sqlite`, que en Node 26
  trae la clase `Database`.
- Dos carpetas:
  - `api`: la API del video anterior ([`../h7-api-node-sqlite/`](../h7-api-node-sqlite/): `package.json` y `t1.json`)
    con el [`servidor.js`](servidor.js) de esta carpeta, que suma el bloque de CORS.
  - `web`: la app de React de [`../h2-react/`](../h2-react/) (creada con `npm create vite@latest`) con los archivos de
    esta carpeta: [`vite.config.js`](vite.config.js) y [`.env.ejemplo`](.env.ejemplo) en la raíz de `web`, y
    [`api.js`](api.js), [`App.jsx`](App.jsx) y [`NuevaTarea.jsx`](NuevaTarea.jsx) en `web/src/`.
- curl, para la prueba del final. Viene en Git Bash, en la Terminal de Mac y en casi todas las de Linux.

**En Windows, usa Git Bash** para que los comandos de esta guía se copien tal cual.

## La variable de entorno

Desde la carpeta `web`, crea el archivo `.env` a partir del ejemplo:

```bash
cp .env.ejemplo .env
```

Su único renglón es la dirección de tu API:

```text
VITE_API_URL=http://localhost:3000
```

Vite lee `.env` al arrancar y lo deja en `import.meta.env`. **Solo** llegan a tu app las variables que empiezan con
`VITE_`. Si cambias `.env`, detén Vite y vuelve a arrancarlo.

## Córrela en dos terminales

**Terminal 1, la API** (desde `api`):

```bash
npm install
npm start
```

Verás `API en el puerto 3000`. Si la base está vacía, agrega una tarea desde otra terminal en `api`, para que la lista
no empiece vacía:

```bash
curl --json @t1.json localhost:3000/tareas
```

**Terminal 2, la app** (desde `web`):

```bash
npm install
npm run dev
```

Abre `http://localhost:5173/`. Verás «Mis tareas (1)». Escribe una tarea y dale «Guardar»: aparece en la lista y queda
en `tareas.db`.

## Por qué el navegador la bloqueaba

Hasta el video anterior, la app pedía `/api/tareas` y el **proxy** de Vite (`server.proxy` en `vite.config.js`) se la
pasaba a la API. Para el navegador, todo venía de `localhost:5173`. Pero ese proxy solo existe en el servidor de
desarrollo: cuando publicas tu app, ya no está. Por eso aquí la app llama **directo** a `http://localhost:3000`.

Un origen es protocolo, host y puerto. `http://localhost:5173` y `http://localhost:3000` cambian el puerto: son dos
orígenes. Cuando tu código hace un `fetch` a otro origen, el navegador solo le entrega la respuesta si el servidor
dice que ese origen puede leerla.

Sin el bloque de CORS (la API de H7 tal cual), la app muestra «No se pudieron cargar.». Tu código no sabe por qué:
el detalle del bloqueo solo aparece en la consola del navegador (F12, pestaña «Console»).

## Cada parte del código

| Parte | Qué hace |
|---|---|
| `import.meta.env.VITE_API_URL` | La dirección de la API, desde `.env` |
| `` const TAREAS = `${API}/tareas`; `` | La URL completa de la ruta, una sola vez |
| `pedirTareas()` | `fetch(TAREAS)` hace un `GET`. Si `res.ok` es falso (un estado fuera de 200 a 299), lanza un error |
| `guardarTarea(texto)` | `fetch` con `method: 'POST'`, el encabezado `Content-Type: application/json` y el cuerpo con `JSON.stringify` |
| `proyecto_id: 1` | La API de H7 guarda cada tarea en un proyecto: el 1 es `Tienda`. Sin proyecto, su `GET` (con `JOIN`) no la mostraría |
| `return { id, texto };` | La API responde solo el `id`; la app arma la tarea para sumarla a la lista |
| `App.jsx` y `NuevaTarea.jsx` | Los de H6, con un solo cambio: importan `pedirTareas` y `guardarTarea` de `./api.js` |
| `vite.config.js` | El de siempre, **sin** proxy |
| `const ORIGEN = 'http://localhost:5173';` | El único origen que tu API autoriza: el de tu app |
| `app.use((req, res, next) => { … })` | Un middleware sin ruta: corre en **todas** las peticiones, antes de las rutas |
| `Access-Control-Allow-Origin` | Le dice al navegador que ese origen puede leer la respuesta |
| `Access-Control-Allow-Headers` | Autoriza el encabezado `Content-Type`, que manda el `POST` con JSON |
| `if (req.method === 'OPTIONS')` | La consulta previa: antes del `POST` con JSON, el navegador pregunta con `OPTIONS`. Se responde `204` (sin contenido) y ahí termina |
| `next()` | En cualquier otra petición, deja pasar a la ruta que toca (`GET` o `POST`) |

**¿Por qué hay consulta previa en el `POST` y no en el `GET`?** Una petición «simple» solo puede llevar
`Content-Type` de tipo `application/x-www-form-urlencoded`, `multipart/form-data` o `text/plain`. El `POST` de la app
lleva `application/json`, así que el navegador pregunta antes. `GET` y `POST` son métodos permitidos sin más, por eso
no hace falta `Access-Control-Allow-Methods`.

## Avisos

- **Una variable `VITE_` no es secreta.** Su valor termina dentro del código que descarga el navegador. Ahí van URL,
  nunca claves ni contraseñas.
- **CORS no protege tu API de todo.** Lo aplica el navegador: curl, otro servidor o un script lo ignoran. Sirve para que
  otras páginas no lean tus respuestas desde el navegador de alguien; no reemplaza validar lo que llega.
- **No uses `*` como origen «para que funcione».** Autoriza el origen exacto de tu app. Cuando la publiques, cambia
  `ORIGEN` por su dirección real (por ejemplo, la de tu dominio).
- **Si Vite arranca en otro puerto** (porque el 5173 estaba ocupado, lo dice al arrancar), el origen cambia y vuelve el
  bloqueo. Cierra lo que usa el 5173 o cambia `ORIGEN`.
- **`server.cors` de `vite.config.js` no sirve aquí:** es el CORS del servidor de Vite, no el de tu API.
- **Sin `.env`**, `import.meta.env.VITE_API_URL` no existe y la app pide una dirección que no es la de tu API: verás
  «No se pudieron cargar.».

## Practica en cinco minutos

Con la API y la app corriendo:

1. **Mira la consulta previa.** Desde cualquier carpeta:

   ```bash
   curl -i -X OPTIONS localhost:3000/tareas
   ```

   La primera línea dice `204 No Content`, y entre los encabezados están `Access-Control-Allow-Origin` y
   `Access-Control-Allow-Headers`.

2. **Provoca el bloqueo.** En `servidor.js`, cambia el origen por uno que no es el tuyo:

   ```js
   const ORIGEN = 'http://localhost:5174';
   ```

   Detén la API con Ctrl + C, arráncala con `npm start` y recarga la página: «No se pudieron cargar.», y la consola
   explica que el origen no coincide. Vuelve a poner `5173`, reinicia la API y recarga.

3. **Mira el error de guardar.** Con la página abierta, detén la API y dale «Guardar» a una tarea: el formulario dice
   «No se pudo guardar.». Arranca la API otra vez.

## Enlaces

- CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- Política del mismo origen: https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy
- `Access-Control-Allow-Origin`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin
- `Access-Control-Allow-Headers`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Headers
- `OPTIONS`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/OPTIONS
- `fetch`: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- Variables de entorno de Vite: https://vite.dev/guide/env-and-mode
- Opciones del servidor de Vite (`server.port`, `server.proxy`, `server.cors`): https://vite.dev/config/server-options
- Pedir datos con `useEffect`: https://react.dev/reference/react/useEffect
- Express 5, `app.use`: https://expressjs.com/en/5x/api/application
- Express 5, `res.set` y `res.sendStatus`: https://expressjs.com/en/5x/api/response/

Datos verificados el 24 de noviembre de 2026 en developer.mozilla.org, vite.dev, react.dev y expressjs.com.
