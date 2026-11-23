# Formularios con estado y validación en React · la guía del video

## Lo que necesitas

- Node.js 26 (https://nodejs.org/).
- La carpeta de [`h1-stack-node/`](../h1-stack-node/) (la API), la de [`h2-react/`](../h2-react/) (la página de React
  con Vite) y el `vite.config.js` de [`h5-react-fetch/`](../h5-react-fetch/). Descárgalas o clona este repositorio.

## Córrelo en dos terminales

**Terminal 1, la API** (desde una copia de la carpeta `h1-stack-node`). Antes, reemplaza `servidor.js` por el de esta
carpeta: [`servidor.js`](servidor.js). Escucha en el puerto 3000 y crea `tareas.db` con tres tareas:

```bash
npm install
npm start
```

**Terminal 2, la página** (desde una copia de la carpeta `h2-react`). Antes, pon en `src/` los archivos
[`App.jsx`](App.jsx) y [`NuevaTarea.jsx`](NuevaTarea.jsx) de esta carpeta, y en la raíz el
[`vite.config.js`](../h5-react-fetch/vite.config.js) de H5 (el proxy de `/api`):

```bash
npm install
npm run dev
```

Abre http://localhost:5173/. Verás «Mis tareas (3)» y, debajo, el formulario «Nueva tarea».

## Prueba la API sin la página

Con la API corriendo, en Git Bash o en la Terminal de Mac y Linux (en PowerShell las comillas funcionan distinto):

```bash
curl -i -X POST http://localhost:3000/api/tareas -H "Content-Type: application/json" -d '{"texto":"Probar la API"}'
curl -i -X POST http://localhost:3000/api/tareas -H "Content-Type: application/json" -d '{"texto":""}'
```

El primero responde `201 Created` con la tarea nueva y su `id`; el segundo, `400 Bad Request` con
`{"error":"Falta el texto."}`. En la terminal 1 verás `Nueva tarea: Probar la API`.

## Cada parte del código

### `NuevaTarea.jsx`

| Parte | Qué hace |
|---|---|
| Los tres `useState` | `texto` (lo que escribes), `error` (el mensaje, vacío si no hay) y `envio` (`true` mientras se guarda) |
| `value={texto}` y `onChange={cambiar}` | El campo controlado: su valor sale del estado y `cambiar` lo actualiza con cada tecla. Sin `onChange`, no podrías escribir |
| `<form onSubmit={enviar}>` | `enviar` corre al dar clic en «Guardar» o al presionar Enter en el campo |
| `e.preventDefault()` | Evita que el navegador envíe el formulario a la página actual y la recargue |
| `if (limpio === '')` | Valida antes de enviar: si el texto está vacío (o solo tiene espacios), guarda el error y se detiene |
| `<label htmlFor="texto">` e `id="texto"` | Ligan la etiqueta «Nueva tarea» con el campo |
| `aria-invalid={error !== ''}` | Marca el campo como inválido mientras hay un error |
| `aria-describedby="error-texto"` | Liga el campo con el párrafo del mensaje: el lector de pantalla lo lee como su descripción |
| `<p id="error-texto" role="alert">` | El mensaje. Está **siempre** en la página y solo cambia su texto: una alerta se anuncia cuando cambia su contenido |
| `setEnvio(true)` … `finally { setEnvio(false); }` | Marca el envío al empezar y lo quita al terminar, salga bien o mal |
| `<button disabled={envio}>` | Mientras se guarda, el botón está desactivado: no recibe clics, así que el doble clic no envía dos veces |
| `guardarTarea(texto)` | Hace el `fetch` con `method: 'POST'`, el encabezado `Content-Type: application/json` y el cuerpo en JSON; revisa `res.ok` como en H5 |
| `onNueva(...)` | Le pasa a `App` la tarea que devolvió la API (con su `id`) |

### `App.jsx`

Es el de H5 con cinco líneas nuevas: el `import` de `NuevaTarea`, la función `agregar` (suma la tarea nueva a la lista)
y `<NuevaTarea onNueva={agregar} />` debajo de la lista.

### `servidor.js`

Es el de H1 con dos cambios:

- `app.use(express.json());` lee los cuerpos JSON y los deja en `req.body`.
- `app.post('/api/tareas', …)` limpia el texto, responde `400` si llega vacío y, si no, lo guarda en SQLite, imprime
  `Nueva tarea: …` y responde `201` con la tarea y su `id` (`lastInsertRowid`).

## Avisos

- **Valida también en el servidor.** La validación de la página ayuda a quien escribe, pero cualquiera puede mandar una
  petición sin pasar por ella (como con `curl`). Por eso la API también rechaza el texto vacío.
- **No repitas el mismo mensaje esperando otro anuncio.** Si el texto de la alerta no cambia, el lector de pantalla no
  lo vuelve a anunciar.
- **No agregues el párrafo con `role="alert"` solo cuando hay error.** Déjalo en la página desde el principio, vacío, y
  cambia su texto.
- **Otra forma en React 19:** puedes pasar una función a `action` del `<form>` en lugar de usar `onSubmit`. Este
  ejemplo usa `onSubmit` para que se vea cada paso.
- **El proxy es solo para desarrollo** (como en H5). En producción, la página y la API se publican juntas o la API se
  llama con su dirección completa.

## Practica en cinco minutos

Con la API y la página corriendo:

1. **El error.** Da clic en «Guardar» con el campo vacío: aparece «Escribe una tarea.». Escribe solo espacios y
   vuelve a intentar: el mismo mensaje.
2. **El envío.** Escribe una tarea y presiona Enter: aparece en la lista, el contador sube y el campo se vacía. En la
   terminal 1 verás `Nueva tarea: …`.
3. **Sin envío doble.** Abre las herramientas del navegador (F12), pestaña «Network» (Red), cambia «No throttling» por
   «Slow 4G», escribe otra tarea y da doble clic en «Guardar»: verás «Guardando…» y **una sola** petición `POST` a
   `/api/tareas`. Regrésalo a «No throttling» al terminar.
4. **Sin la API.** Detén la API con Ctrl + C en la terminal 1, escribe una tarea y guarda: verás «No se pudo
   guardar.». Vuelve a arrancarla:

   ```bash
   npm start
   ```

5. **Lo que quedó guardado.** Abre http://localhost:3000/api/tareas: ahí están tus tareas nuevas, con su `id`.

## Enlaces

- Campo controlado: https://react.dev/reference/react-dom/components/input
- Formulario y `onSubmit`: https://react.dev/reference/react-dom/components/form
- Los estados de un formulario: https://react.dev/learn/reacting-to-input-with-state
- Evitar el comportamiento por defecto: https://react.dev/learn/responding-to-events
- Rol `alert`: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/alert_role
- `aria-invalid`: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid
- `aria-describedby`: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby
- Atributo `disabled`: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled
- `fetch` con cuerpo y encabezados: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- `express.json()`: https://expressjs.com/en/5x/api/express/
- `statement.run()` de `node:sqlite`: https://nodejs.org/api/sqlite.html

Datos verificados el 22 de noviembre de 2026 en react.dev, MDN, expressjs.com y nodejs.org.
