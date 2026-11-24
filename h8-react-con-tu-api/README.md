# Conecta tu React a tu propia API

Video de la serie **Desarrollo web** del Laboratorio Ayemi y continuación de
[React nivel 3: formularios con estado y validación](../h6-react-formularios/) y de
[Tu primera API: Node y SQLite con GET y POST](../h7-api-node-sqlite/).

## El caso

La lista «Mis tareas» de React ahora habla directo con la API de Node: la lee con `GET` y guarda con `POST`. Pero tu
app corre en `http://localhost:5173` y tu API en `http://localhost:3000`: puertos distintos son **orígenes distintos**,
y el navegador no le entrega la respuesta a tu código hasta que el servidor autoriza ese origen con **CORS**.

| Paso | Dónde | Qué pasa |
|---|---|---|
| 1. La dirección | `.env` → `VITE_API_URL` | La app lee la URL de la API con `import.meta.env`. Solo llegan las variables que empiezan con `VITE_` |
| 2. Pedir y guardar | `api.js` | `fetch` con `GET` trae las tareas; con `POST` y JSON guarda una nueva. `res.ok` revisa la respuesta |
| 3. Carga y error | `App.jsx` | Los dos estados de antes: «Cargando…» y «No se pudieron cargar.» |
| 4. El bloqueo | El navegador | Sin CORS, la app muestra su error y la consola dice «blocked by CORS policy» |
| 5. CORS | `servidor.js` | `Access-Control-Allow-Origin` con el origen de tu app, `Access-Control-Allow-Headers` con `Content-Type` y la consulta previa (`OPTIONS`) respondida con `204` |

Según MDN: «CORS failures result in errors but for security reasons, specifics about the error are not available to
JavaScript. [...] The only way to determine what specifically went wrong is to look at the browser's console for
details.»

El código está en [`servidor.js`](servidor.js) (la API), [`api.js`](api.js), [`App.jsx`](App.jsx),
[`NuevaTarea.jsx`](NuevaTarea.jsx), [`vite.config.js`](vite.config.js) y [`.env.ejemplo`](.env.ejemplo) (la app). La
guía completa, con cómo correr las dos partes, cada pieza explicada, los avisos y una práctica de cinco minutos, está en
[`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| CORS (MDN) | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS |
| Política del mismo origen (MDN) | https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy |
| `Access-Control-Allow-Origin` (MDN) | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin |
| `fetch` (MDN) | https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch |
| Variables de entorno de Vite | https://vite.dev/guide/env-and-mode |
| Pedir datos con `useEffect` | https://react.dev/reference/react/useEffect |
| Express 5: `app.use` | https://expressjs.com/en/5x/api/application |
| Video anterior: tu primera API | [`../h7-api-node-sqlite/`](../h7-api-node-sqlite/) |

Datos verificados el 24 de noviembre de 2026 en developer.mozilla.org, vite.dev, react.dev y expressjs.com. Ayemi no
tiene relación con React, Meta, Vite, Mozilla, OpenJS Foundation ni Express.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
