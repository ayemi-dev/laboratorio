# Trae datos de una API con useEffect · la guía del video

## Lo que necesitas

- Node.js 26 (https://nodejs.org/).
- La carpeta de [`h1-stack-node/`](../h1-stack-node/) (la API) y la de [`h2-react/`](../h2-react/) (la página de React
  con Vite). Descárgalas o clona este repositorio.

## Córrelo en dos terminales

**Terminal 1, la API** (desde la carpeta `h1-stack-node`). Escucha en el puerto 3000 y crea `tareas.db` con tres
tareas:

```bash
npm install
npm start
```

Compruébala en el navegador: http://localhost:3000/api/tareas devuelve las tareas en JSON.

**Terminal 2, la página** (desde una copia de la carpeta `h2-react`). Antes, reemplaza `src/App.jsx` y
`vite.config.js` por los de esta carpeta: [`App.jsx`](App.jsx) y [`vite.config.js`](vite.config.js).

```bash
npm install
npm run dev
```

Abre http://localhost:5173/. Verás «Mis tareas (3)» con las tareas que vienen de la API.

## Cada parte del código

| Parte | Qué hace |
|---|---|
| `server.proxy` en `vite.config.js` | En desarrollo, Vite pasa las peticiones que empiezan con `/api` al servidor del puerto 3000. Así la página pide `/api/tareas` sin escribir la dirección completa |
| `pedirTareas()` | Hace el `fetch` y revisa `res.ok`. Si la respuesta no salió bien (un código fuera de 200 a 299), lanza un error |
| Los tres `useState` | `tareas` (la lista), `carga` (empieza en `true`) y `error` (empieza en `false`) |
| `useEffect(() => { … }, [])` | Pide los datos cuando el componente aparece por primera vez (el arreglo vacío) |
| `.then`, `.catch` y `.finally` | Guardan las tareas, marcan el error o terminan la carga |
| `let ignorar = false;` y `return () => { ignorar = true; };` | La limpieza: si el componente se desmonta antes de que llegue la respuesta, esa respuesta se ignora |
| `if (carga)` y `if (error)` | Muestran «Cargando…» o «No se pudieron cargar.» antes de la lista |

## ¿Por qué sale la petición dos veces?

Tu `src/main.jsx` (el de la plantilla de Vite) envuelve la app en `<StrictMode>`. En desarrollo, el modo estricto monta
cada componente, lo desmonta y lo vuelve a montar justo después, para encontrar efectos sin limpieza. Por eso el
efecto corre dos veces y ves dos peticiones en la pestaña «Network» (Red) de las herramientas del navegador.

- **Es normal y solo pasa en desarrollo.** En producción sale una sola petición.
- **Con la limpieza, solo cuenta una respuesta:** la del primer montaje llega con `ignorar` en `true` y no toca el
  estado.
- **No quites `<StrictMode>`** ni uses un `useRef` para que el efecto corra una sola vez: eso esconde el problema, no
  lo arregla. La pregunta no es «cómo lo corro una vez», sino «cómo hago que funcione al volver a montar».

## Avisos

- **`fetch` no falla con un 404 o un 500.** Solo falla si la petición no llega (por ejemplo, sin red). Por eso se
  revisa `res.ok` y se lanza el error a mano.
- **La otra forma de limpiar** es cancelar la petición con `AbortController` en lugar de ignorar su resultado. Las dos
  son válidas según react.dev; la bandera es la más corta de leer.
- **Si usas un framework**, usa su propia forma de traer datos: react.dev dice que es más eficiente que escribir
  efectos a mano.
- **El proxy es solo para desarrollo.** En producción, la página y la API se publican juntas o la API se llama con su
  dirección completa.

## Practica en cinco minutos

Con la API y la página corriendo:

1. **Las dos peticiones.** Abre las herramientas del navegador (F12), pestaña «Network» (Red), filtra por `tareas` y
   recarga: verás dos peticiones a `/api/tareas`.
2. **El error.** Detén la API con Ctrl + C en la terminal 1 y recarga la página: verás «Cargando…» y luego «No se
   pudieron cargar.». Vuelve a arrancarla:

   ```bash
   npm start
   ```

3. **La carga.** En la pestaña «Network», cambia «No throttling» por «Slow 4G» y recarga: ahora sí se alcanza a ver
   «Cargando…». Regrésalo a «No throttling» al terminar.
4. **Una sola petición en producción.** Detén `npm run dev` con Ctrl + C y, en la terminal 2:

   ```bash
   npm run build
   npm run preview
   ```

   Abre la dirección que imprime y repite el paso 1: verás una sola petición.

## Enlaces

- `useEffect`: https://react.dev/reference/react/useEffect
- Efectos, limpieza y por qué corren dos veces: https://react.dev/learn/synchronizing-with-effects
- Modo estricto: https://react.dev/reference/react/StrictMode
- `fetch()`: https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch
- `Response.ok`: https://developer.mozilla.org/en-US/docs/Web/API/Response/ok
- Proxy de Vite: https://vite.dev/config/server-options

Datos verificados el 21 de noviembre de 2026 en react.dev, MDN y vite.dev.
