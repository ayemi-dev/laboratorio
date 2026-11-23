# React nivel 3: formularios con estado y validación

Video de la serie **Desarrollo web** del Laboratorio Ayemi y continuación de
[Trae datos de una API con useEffect](../h5-react-fetch/), con la API de
[Qué es un stack: el stack de Node.js](../h1-stack-node/).

## El caso

La lista «Mis tareas» de H5 ya leía sus tareas de la API. Ahora también **guarda**: un formulario «Nueva tarea» con tres
estados (el texto, el error y si está enviando) que valida antes de enviar, avisa el error también al lector de
pantalla y **no envía dos veces** aunque des doble clic.

| Paso | Dónde | Qué pasa |
|---|---|---|
| 1. Campo controlado | `value={texto}` y `onChange={cambiar}` | El valor del campo vive en el estado; cada tecla lo actualiza |
| 2. Enviar sin recargar | `onSubmit={enviar}` y `e.preventDefault()` | El navegador no recarga la página: el envío lo maneja React |
| 3. Validar | `if (limpio === '')` | Si el campo está vacío, se guarda un error y no se envía nada |
| 4. Avisar de forma accesible | `role="alert"`, `aria-invalid` y `aria-describedby` | El mensaje se ve y el lector de pantalla lo anuncia |
| 5. No enviar dos veces | `disabled={envio}` | Mientras se guarda, el botón está desactivado y no recibe clics |
| 6. Guardar en la API | `POST /api/tareas` | El servidor guarda y responde `201`; si llega vacío, responde `400` |

El formulario está en [`NuevaTarea.jsx`](NuevaTarea.jsx); `App.jsx` lo agrega debajo de la lista
([`App.jsx`](App.jsx)), y el servidor de H1 suma la ruta para guardar ([`servidor.js`](servidor.js)). La guía completa,
con cómo correr todo, cada parte explicada, la prueba con `curl`, los avisos y una práctica de cinco minutos, está en
[`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Campo controlado (`<input>`) | https://react.dev/reference/react-dom/components/input |
| Formulario y `onSubmit` (`<form>`) | https://react.dev/reference/react-dom/components/form |
| Los estados de un formulario («Reacting to Input with State») | https://react.dev/learn/reacting-to-input-with-state |
| Rol `alert` | https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/alert_role |
| `aria-invalid` | https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid |
| `aria-describedby` | https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby |
| Atributo `disabled` | https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled |
| `fetch` con `POST` y JSON | https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch |
| `express.json()` | https://expressjs.com/en/5x/api/express/ |
| Video anterior de esta parte: trae datos con useEffect | [`../h5-react-fetch/`](../h5-react-fetch/) |
| La API que se usa: el stack de Node.js | [`../h1-stack-node/`](../h1-stack-node/) |

Datos verificados el 22 de noviembre de 2026 en react.dev, MDN y expressjs.com. Ayemi no tiene relación con React,
Meta, Vite, Express ni Mozilla.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
