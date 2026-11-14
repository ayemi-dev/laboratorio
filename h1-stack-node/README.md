# Qué es un stack: el stack de Node.js

Primer video de la serie **Desarrollo web: stacks y frameworks** del Laboratorio Ayemi. Un *stack* es el conjunto de tecnologías con que se arma una aplicación, por capas: la interfaz que ves, el servidor que responde y la base de datos que guarda. En el stack de Node.js todo se escribe en JavaScript.

## La app del video

| Capa | En esta app | Archivo |
|---|---|---|
| Interfaz | HTML y JavaScript en el navegador | `publico/index.html` |
| Servidor | [Node.js](https://nodejs.org/) con [Express](https://expressjs.com/) | `servidor.js` |
| Base de datos | SQLite, incluido en Node (`node:sqlite`) | se crea `tareas.db` |

## Córrela

Necesitas Node.js 26 (la versión LTS vigente; se probó con la 26.13.1).

```bash
npm install
npm start
```

Abre http://localhost:3000. La página le pide las tareas a `/api/tareas` y el servidor las lee de la base.

`node:sqlite` está como *release candidate* en Node 26 y muestra un aviso de función experimental; `npm start` lo silencia con `--disable-warning=ExperimentalWarning`.

## Stacks con nombre

| Stack | Base de datos | Servidor | Interfaz | Entorno |
|---|---|---|---|---|
| MERN | MongoDB | Express | React | Node.js |
| MEAN | MongoDB | Express | Angular | Node.js |

En el siguiente video de la serie: qué es React.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Node.js (descarga y versiones LTS) | https://nodejs.org/ |
| Express | https://expressjs.com/ |
| npm | https://docs.npmjs.com/about-npm |
| `node:sqlite` | https://nodejs.org/docs/latest-v26.x/api/sqlite.html |
| Qué es MERN (y MEAN) | https://www.mongodb.com/resources/languages/mern-stack |

Datos verificados el 13 de noviembre de 2026 en las páginas oficiales. Ayemi no tiene relación con OpenJS Foundation ni con MongoDB, Inc.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
