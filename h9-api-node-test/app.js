// La API de H8, lista para probarse:
// crearApp('tareas.db') o (':memory:')
import express from 'express';
import { Database } from 'node:sqlite';

export function crearApp(ruta) {
  // La base: un archivo o la memoria
  const db = new Database(ruta);
  db.exec(`
    CREATE TABLE IF NOT EXISTS proyectos (
      id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS tareas (
      id INTEGER PRIMARY KEY,
      texto TEXT NOT NULL,
      proyecto_id INTEGER
    );
    INSERT OR IGNORE INTO proyectos
      VALUES (1, 'Tienda'), (2, 'Blog');
  `);

  const app = express();

  // CORS: deja pasar a tu app de React
  const ORIGEN = 'http://localhost:5173';
  app.use((req, res, next) => {
    res.set('Access-Control-Allow-Origin',
      ORIGEN);
    res.set('Access-Control-Allow-Headers',
      'Content-Type');
    if (req.method === 'OPTIONS') {
      return res.sendStatus(204);
    }
    next();
  });

  app.use(express.json()); // lee el JSON
  app.set('json spaces', 2); // lo ordena

  // GET /tareas: cada tarea con su proyecto
  const listar = db.prepare(`
    SELECT tareas.id, tareas.texto,
      proyectos.nombre AS proyecto
    FROM tareas
    JOIN proyectos
      ON proyectos.id = tareas.proyecto_id
  `);

  app.get('/tareas', (req, res) => {
    res.json(listar.all());
  });

  // POST /tareas: los datos van aparte (?)
  const crear = db.prepare(`
    INSERT INTO tareas (texto, proyecto_id)
    VALUES (?, ?)
  `);

  app.post('/tareas', (req, res) => {
    const { texto, proyecto_id } = req.body;
    // Sin texto no se guarda: error 400
    if (typeof texto !== 'string' || !texto) {
      return res.status(400)
        .json({ error: 'Falta el texto' });
    }
    const r = crear.run(texto, proyecto_id);
    res.status(201)
      .json({ id: r.lastInsertRowid });
  });

  return app;
}
