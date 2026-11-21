# React nivel 2: trae datos de una API con useEffect (y sin el error del doble render)

Video de la serie **Desarrollo web** del Laboratorio Ayemi y continuación de [Qué es React](../h2-react/), con la API
de [Qué es un stack: el stack de Node.js](../h1-stack-node/).

## El caso

La lista «Mis tareas» de H2 tenía sus tareas escritas en el código. Ahora las pide a la API del primer video
(`GET /api/tareas`), y en desarrollo **la petición sale dos veces**. No es un error: es el modo estricto de React
buscando efectos sin limpieza.

| Paso | Dónde | Qué pasa |
|---|---|---|
| 1. Pedir los datos | `fetch` dentro de `useEffect` | `useEffect` sincroniza tu componente con un sistema externo, como una API |
| 2. Correr al montar | arreglo de dependencias vacío, `[]` | El efecto corre cuando el componente aparece por primera vez |
| 3. Tres estados | `tareas`, `carga` y `error` | La página muestra «Cargando…», la lista o el mensaje de error |
| 4. Revisar la respuesta | `if (!res.ok)` | `fetch` no falla solo porque el servidor responda con un error (404, 504…) |
| 5. Limpiar | la bandera `ignorar` | Al desmontar, la respuesta vieja se ignora y no pisa a la nueva |

En desarrollo, el modo estricto (`<StrictMode>`, que ya trae la plantilla de Vite) monta el componente, lo desmonta y
lo vuelve a montar: por eso ves dos peticiones. **No lo quites**: con la limpieza, solo cuenta una respuesta. En
producción sale una sola petición.

El código está en [`App.jsx`](App.jsx) y [`vite.config.js`](vite.config.js). La guía completa, con cómo correr la API y
la página, cada parte explicada, los avisos y una práctica de cinco minutos, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `useEffect` | https://react.dev/reference/react/useEffect |
| Efectos y limpieza («Synchronizing with Effects») | https://react.dev/learn/synchronizing-with-effects |
| Modo estricto (`<StrictMode>`) | https://react.dev/reference/react/StrictMode |
| `fetch()` | https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch |
| `Response.ok` | https://developer.mozilla.org/en-US/docs/Web/API/Response/ok |
| Proxy del servidor de Vite (`server.proxy`) | https://vite.dev/config/server-options |
| Video anterior de esta parte: Qué es React | [`../h2-react/`](../h2-react/) |
| La API que se usa: el stack de Node.js | [`../h1-stack-node/`](../h1-stack-node/) |

Datos verificados el 21 de noviembre de 2026 en react.dev, MDN y vite.dev. Ayemi no tiene relación con React, Meta,
Vite ni Mozilla.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
