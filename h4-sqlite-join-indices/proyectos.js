import { Database } from 'node:sqlite';

// En memoria: cada corrida empieza igual
const db = new Database(':memory:');

// 1. Dos tablas, unidas por proyecto_id
db.exec(`
  CREATE TABLE proyectos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
  );
  CREATE TABLE tareas (
    id INTEGER PRIMARY KEY,
    texto TEXT NOT NULL,
    proyecto_id INTEGER
  );
`);

// Datos de ejemplo
db.exec(`
  INSERT INTO proyectos (nombre)
    VALUES ('Tienda'), ('Blog');
  INSERT INTO tareas (texto, proyecto_id)
    VALUES ('Crear la API', 1),
           ('Probar la API', 1),
           ('Escribir el post', 2);
`);

// 2. JOIN: cada tarea con su proyecto
const consulta = `
  SELECT tareas.texto, proyectos.nombre
  FROM tareas
  JOIN proyectos
    ON proyectos.id = tareas.proyecto_id
  WHERE proyectos.nombre = 'Tienda'`;
const filas = db.prepare(consulta).all();
console.table(filas);

// 3. El plan: cómo lo resuelve SQLite
function plan(titulo) {
  console.log(titulo);
  const pasos = db.prepare(
    'EXPLAIN QUERY PLAN ' + consulta
  ).all();
  for (const paso of pasos) {
    console.log(paso.detail);
  }
}

// 4. Antes y después del índice
plan('Antes del índice:');
db.exec(`CREATE INDEX idx_proyecto
  ON tareas (proyecto_id)`);
plan('Después del índice:');

db.close();
