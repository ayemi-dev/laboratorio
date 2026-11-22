// App mínima del Laboratorio Ayemi (G20): un servidor de Express para practicar capas y caché de Docker.
const express = require("express");

const app = express();
const puerto = 3000;

app.get("/", (pedido, respuesta) => {
  respuesta.send("Hola desde tu propia imagen de Docker\n");
});

app.listen(puerto, () => {
  console.log(`App escuchando en el puerto ${puerto}`);
});
