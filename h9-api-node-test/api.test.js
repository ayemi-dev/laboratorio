// Pruebas de tu API con node:test
import { it, before, after }
  from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { crearApp } from './app.js';

let servidor;
let url;

before(async () => {
  // Base en memoria: no toca tareas.db
  const app = crearApp(':memory:');
  // Puerto 0: el sistema da uno libre
  servidor = app.listen(0);
  await once(servidor, 'listening');
  const { port } = servidor.address();
  url = `http://localhost:${port}/tareas`;
});

after(() => servidor.close());

// POST con JSON, como la app de H8
function enviar(datos) {
  return fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(datos),
  });
}

it('GET empieza vacío', async () => {
  const res = await fetch(url);
  assert.strictEqual(res.status, 200);
  const tareas = await res.json();
  assert.deepStrictEqual(tareas, []);
});

it('POST guarda una tarea', async () => {
  const res = await enviar({
    texto: 'Probar la API',
    proyecto_id: 1,
  });
  assert.strictEqual(res.status, 201);
  const { id } = await res.json();
  assert.strictEqual(id, 1);
});

it('GET trae la tarea', async () => {
  const res = await fetch(url);
  const tareas = await res.json();
  assert.deepStrictEqual(tareas, [
    { id: 1, texto: 'Probar la API',
      proyecto: 'Tienda' },
  ]);
});

it('POST sin texto da 400', async () => {
  const res = await enviar({
    proyecto_id: 1,
  });
  assert.strictEqual(res.status, 400);
  const cuerpo = await res.json();
  assert.deepStrictEqual(cuerpo, {
    error: 'Falta el texto',
  });
});
