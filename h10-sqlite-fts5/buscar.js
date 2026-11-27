import { Database } from 'node:sqlite';

// En memoria: cada corrida empieza igual
const db = new Database(':memory:');

// Datos falsos para practicar
const verbos = ['Revisar', 'Cambiar',
  'Limpiar', 'Calibrar', 'Probar',
  'Soldar', 'Medir'];
const cosas = ['el sensor', 'la bomba',
  'el motor', 'la placa', 'el relevador',
  'la pantalla', 'el cable',
  'la batería', 'el ventilador',
  'la antena', 'el teclado'];
const lugares = ['del invernadero',
  'de la bodega', 'del taller',
  'de la cocina', 'del portón',
  'de la oficina', 'del techo',
  'del patio', 'de la entrada',
  'del sótano', 'del laboratorio',
  'de la azotea', 'del garaje'];
const notas = ['', ' hoy',
  ' y anotar la lectura',
  ' y otro sensor',
  ' antes del viernes'];

// 1. Veinte mil tareas de práctica
db.exec(`CREATE TABLE tareas (
  id INTEGER PRIMARY KEY,
  texto TEXT NOT NULL
)`);
const insertar = db.prepare(`
  INSERT INTO tareas (texto)
  VALUES (?)`);
for (let i = 0; i < 20000; i++) {
  const texto = [verbos[i % 7],
    cosas[i % 11], lugares[i % 13]]
    .join(' ') + notas[i % 5];
  insertar.run(texto);
}
console.log('Tareas:', db.prepare(
  'SELECT count(*) AS n FROM tareas'
).get().n);

// 2. FTS5: una tabla virtual para buscar
db.exec(`
  CREATE VIRTUAL TABLE buscador
    USING fts5(texto);
  INSERT INTO buscador (rowid, texto)
    SELECT id, texto FROM tareas;
`);

// 3. Cuánto tarda cada búsqueda
function medir(nombre, sql) {
  const consulta = db.prepare(sql);
  const t0 = performance.now();
  let fila;
  for (let i = 0; i < 20; i++) {
    fila = consulta.get();
  }
  const fin = performance.now();
  const ms = (fin - t0) / 20;
  console.log(nombre, fila.total,
    'filas en', ms.toFixed(2), 'ms');
}

medir('LIKE:', `SELECT count(*) AS total
  FROM tareas
  WHERE texto LIKE '%sensor%'`);
medir('FTS5:', `SELECT count(*) AS total
  FROM buscador
  WHERE buscador MATCH 'sensor'`);

// 4. Las más relevantes primero (bm25)
const mejores = db.prepare(`
  SELECT texto FROM buscador
  WHERE buscador MATCH 'sensor'
  ORDER BY bm25(buscador)
  LIMIT 3`).all();
console.log('Las 3 más relevantes:');
for (const fila of mejores) {
  console.log(fila.texto);
}

db.close();
