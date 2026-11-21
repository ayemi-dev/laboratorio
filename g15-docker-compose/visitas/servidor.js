// App mínima del Laboratorio Ayemi (G15): cuenta las visitas y las guarda en Postgres.
// La conexión sale de PGHOST, PGUSER, PGPASSWORD y PGDATABASE, que pone compose.yaml.
const http = require("node:http");
const { Pool } = require("pg");

const pool = new Pool();
const TEXTO = { "Content-Type": "text/plain; charset=utf-8" };

async function preparar() {
  await pool.query(
    "CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, fecha TIMESTAMPTZ NOT NULL DEFAULT now())"
  );
  console.log("Tabla visitas lista en Postgres");
}

const servidor = http.createServer(async (pedido, respuesta) => {
  if (pedido.url !== "/") {
    respuesta.writeHead(404, TEXTO);
    respuesta.end("No encontrado\n");
    return;
  }
  try {
    await pool.query("INSERT INTO visitas DEFAULT VALUES");
    const { rows } = await pool.query("SELECT count(*) AS total FROM visitas");
    respuesta.writeHead(200, TEXTO);
    respuesta.end(`Visitas guardadas en Postgres: ${rows[0].total}\n`);
  } catch (error) {
    console.error("Error con la base de datos:", error.message);
    respuesta.writeHead(500, TEXTO);
    respuesta.end("Error con la base de datos\n");
  }
});

preparar()
  .then(() => {
    servidor.listen(3000, () => console.log("App escuchando en el puerto 3000"));
  })
  .catch((error) => {
    console.error("No se pudo preparar la base:", error.message);
    process.exit(1);
  });
