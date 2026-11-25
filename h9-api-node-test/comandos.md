# Prueba tu API de Node sin instalar nada con node:test · la guía del video

## Lo que necesitas

- Node.js 26 (https://nodejs.org/). Trae `node:test`, `node:assert`, `fetch` y SQLite incluidos.
- Esta carpeta: `package.json`, `app.js`, `servidor.js` y `api.test.js`. Descárgala o clona este repositorio.

**En Windows, usa Git Bash** (como en H7 y H8): los comandos de esta guía se copian tal cual.

«Sin instalar nada» quiere decir sin biblioteca de pruebas: Express, el de la API, sí se instala con `npm install`.

## Córrelas

Desde esta carpeta:

```bash
npm install
node --test
```

Verás las cuatro pruebas con `✔` y, al final, un resumen con `pass 4` y `fail 0`. No hace falta que la API esté
corriendo: las pruebas la levantan solas, en otro puerto, y la apagan al terminar. Tampoco se crea `tareas.db`.

`npm test` hace lo mismo (en `package.json`, el script `test` es `node --test`):

```bash
npm test
```

La API se sigue arrancando como antes, en el puerto 3000 y con `tareas.db`:

```bash
npm start
```

## Cada parte del código

| Parte | Qué hace |
|---|---|
| `export function crearApp(ruta)` (`app.js`) | Arma la API de H8 (la de H7 con CORS) y la devuelve **sin** ponerla a escuchar. `ruta` es el archivo de la base |
| `if (typeof texto !== 'string' \|\| !texto)` | La validación que la guía de H7 dejó como práctica 4: sin texto, responde `400` con `{ "error": "Falta el texto" }` |
| `crearApp('tareas.db')` y `app.listen(3000, …)` (`servidor.js`) | El arranque de siempre: la base en un archivo y el puerto 3000 |
| `import { it, before, after } from 'node:test'` | El corredor de pruebas de Node. `it` es otro nombre de `test` |
| `import assert from 'node:assert/strict'` | Las comprobaciones, en modo estricto |
| `crearApp(':memory:')` | La base vive en memoria: cada vez que corren las pruebas empieza vacía y `tareas.db` no se toca |
| `app.listen(0)` | Puerto 0: el sistema operativo da uno libre. Así no choca con tu API si la tienes corriendo en el 3000 |
| `await once(servidor, 'listening')` | Espera a que el servidor esté escuchando antes de seguir |
| `servidor.address().port` | El puerto que tocó; con él se arma `url` |
| `after(() => servidor.close())` | Apaga el servidor al final. Corre aunque alguna prueba falle |
| `enviar(datos)` | Un `fetch` con `POST` y JSON, igual al de la app de H8 |
| `assert.strictEqual(res.status, 201)` | Revisa el código de estado |
| `assert.deepStrictEqual(tareas, [...])` | Revisa el JSON completo, campo por campo |

Las cuatro pruebas, en orden:

1. `GET empieza vacío`: `200` y `[]`.
2. `POST guarda una tarea`: `201` y el `id` `1`.
3. `GET trae la tarea`: la tarea con su proyecto, `'Tienda'`.
4. `POST sin texto da 400`: `400` y `{ "error": "Falta el texto" }`.

## Avisos

- **Las pruebas de un archivo corren en orden y comparten la base.** La tercera solo pasa si la segunda guardó la
  tarea. Para pruebas que no dependan entre sí, crea la app en un `beforeEach`.
- **Cuatro pruebas no cubren toda la API.** Son el punto de partida: cada vez que agregues una ruta, agrega su prueba.
- **Si una prueba falla, `node --test` termina con código de salida 1.** Por eso sirve en GitHub Actions (el video G21
  de la serie lo hace con otras pruebas).
- **`--disable-warning=ExperimentalWarning`** en el script `start` solo silencia el aviso de que `node:sqlite` todavía
  no es estable del todo (en Node 26 es «candidato a estable»). Si `node --test` muestra ese aviso, es el mismo y no
  afecta a las pruebas.

## Practica en cinco minutos

1. **Míralo en rojo.** En `api.test.js`, cambia `proyecto: 'Tienda'` por `proyecto: 'Blog'`, guarda y corre:

   ```bash
   node --test
   ```

   Falla solo `GET trae la tarea`. La comparación marca con `+` lo que llegó (`'Tienda'`) y con `-` lo que esperabas
   (`'Blog'`). Regresa `'Tienda'` y vuelve el verde.

2. **El código de salida.** Con la prueba rota otra vez, corre esto y luego mira el número que imprime `echo`:

   ```bash
   node --test
   echo $?
   ```

   Con una prueba en rojo, `1`; con todo en verde, `0`.

3. **Tu propia prueba.** Agrega al final de `api.test.js` una prueba que guarde una tarea en el proyecto 2 y revise que
   responda `201`:

   ```js
   it('POST en Blog', async () => {
     const res = await enviar({
       texto: 'Escribir la guía',
       proyecto_id: 2,
     });
     assert.strictEqual(res.status, 201);
   });
   ```

   Corre `node --test`: ahora son cinco en verde.

4. **Tus datos no se tocan.** Después de correr las pruebas, revisa que en la carpeta no apareció `tareas.db`:

   ```bash
   ls
   ```

## Enlaces

- Corredor de pruebas (`node --test`, `test`, `it`, `before`, `after`): https://nodejs.org/api/test.html
- `node:assert` (`strictEqual`, `deepStrictEqual`, modo estricto): https://nodejs.org/api/assert.html
- Express 5, `app.listen` y el puerto 0: https://expressjs.com/en/5x/api/application
- SQLite en Node.js (`Database` y `':memory:'`): https://nodejs.org/api/sqlite.html
- `once` de `node:events`: https://nodejs.org/api/events.html
- `server.address()`: https://nodejs.org/api/net.html
- `fetch` en Node.js: https://nodejs.org/api/globals.html
- `400 Bad Request`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/400

Datos verificados el 25 de noviembre de 2026 en nodejs.org (documentación de Node.js v26.13.1), expressjs.com y MDN.
