import { Database } from 'node:sqlite';

// Abre el archivo (lo crea si no existe)
const db = new Database('tareas.db');

// 1. Crear la tabla
db.exec(`
  CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY,
    texto TEXT NOT NULL
  )
`);

// 2. Insertar la tarea que escribes
const insertar = db.prepare(
  'INSERT INTO tareas (texto) VALUES (?)'
);
insertar.run(process.argv[2]);

// 3. Consultar todas
const filas = db.prepare(
  'SELECT id, texto FROM tareas'
).all();
console.table(filas);

db.close();
