# Prueba tu API de Node sin instalar nada con node:test

Video de la serie **Desarrollo web** del Laboratorio Ayemi y continuación de
[Tu primera API: Node y SQLite con GET y POST](../h7-api-node-sqlite/) y de
[Conecta tu React a tu propia API](../h8-react-con-tu-api/).

## El caso

La API de tareas ya funciona, pero cada cambio obligaba a probarla otra vez a mano con curl. Node trae su propio
corredor de pruebas, `node:test`, y su módulo `assert`: sin instalar ninguna biblioteca de pruebas, levantas la API en
un puerto libre, con la base en memoria, le haces peticiones reales con `fetch` y `node --test` te dice en verde o en
rojo si sigue funcionando.

| Paso | Dónde | Qué pasa |
|---|---|---|
| 1. Separar | `app.js` y `servidor.js` | `crearApp(ruta)` arma la API sin ponerla a escuchar; `servidor.js` la arranca en el puerto 3000 con `tareas.db` |
| 2. Levantar | `before` en `api.test.js` | La API se levanta en el puerto 0 (el sistema da uno libre) y con la base en `':memory:'`: `tareas.db` no se toca |
| 3. Pedir | `fetch` | Cada prueba hace una petición real: `GET`, `POST` y un `POST` sin texto |
| 4. Revisar | `assert` | `strictEqual` revisa el estado (`200`, `201`, `400`) y `deepStrictEqual` el JSON completo |
| 5. Correr | `node --test` | Encuentra `api.test.js` solo y muestra cada prueba en verde o en rojo |
| 6. Apagar | `after` | Cierra el servidor al final, aunque alguna prueba falle |

Según la documentación de Express: «If port is omitted or is 0, the operating system will assign an arbitrary unused
port, which is useful for cases like automated tasks (tests, etc.).»

El código está en [`app.js`](app.js) (la API), [`servidor.js`](servidor.js) (el arranque),
[`api.test.js`](api.test.js) (las cuatro pruebas) y [`package.json`](package.json). La guía completa, con cómo
correrlas, cada parte explicada, los avisos y una práctica de cinco minutos, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Corredor de pruebas `node:test` | https://nodejs.org/api/test.html |
| `node:assert` | https://nodejs.org/api/assert.html |
| Express 5: `app.listen` y el puerto 0 | https://expressjs.com/en/5x/api/application |
| SQLite en Node.js (`':memory:'`) | https://nodejs.org/api/sqlite.html |
| `fetch` en Node.js | https://nodejs.org/api/globals.html |
| `400 Bad Request` (MDN) | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/400 |
| Video anterior: conecta tu React a tu API | [`../h8-react-con-tu-api/`](../h8-react-con-tu-api/) |

Datos verificados el 25 de noviembre de 2026 en nodejs.org (documentación de Node.js v26.13.1), expressjs.com y
developer.mozilla.org. Ayemi no tiene relación con OpenJS Foundation, Node.js, Express ni Mozilla.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
