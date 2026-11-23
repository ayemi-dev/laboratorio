// Stack de Node.js en un archivo:
// servidor (Express) + datos (SQLite de Node)
import express from 'express';
import { DatabaseSync } from 'node:sqlite';

// Base de datos: un archivo, sin instalar nada
const db = new DatabaseSync('tareas.db');
db.exec(`CREATE TABLE IF NOT EXISTS tareas (
  id INTEGER PRIMARY KEY,
  texto TEXT NOT NULL
)`);
const total = db.prepare('SELECT COUNT(*) AS n FROM tareas').get().n;
if (total === 0) {
  const nueva = db.prepare('INSERT INTO tareas (texto) VALUES (?)');
  nueva.run('Diseñar la interfaz');
  nueva.run('Crear la API');
  nueva.run('Guardar en la base');
}

const app = express();
app.use(express.static('publico')); // la interfaz
app.use(express.json()); // lee los cuerpos JSON

// Servidor: una ruta que lee la base
app.get('/api/tareas', (req, res) => {
  const filas = db.prepare('SELECT * FROM tareas').all();
  res.json(filas);
});

// Y otra que guarda una tarea nueva
app.post('/api/tareas', (req, res) => {
  const texto = String(req.body?.texto ?? '').trim();
  if (texto === '') {
    return res.status(400).json({ error: 'Falta el texto.' });
  }
  const guardar = db.prepare('INSERT INTO tareas (texto) VALUES (?)');
  const { lastInsertRowid } = guardar.run(texto);
  console.log(`Nueva tarea: ${texto}`);
  res.status(201).json({ id: Number(lastInsertRowid), texto });
});

app.listen(3000, () => {
  console.log('Listo en http://localhost:3000');
});
