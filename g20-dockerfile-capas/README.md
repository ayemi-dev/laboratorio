# Docker nivel 3: tu propio Dockerfile, capas y caché

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi; sigue a [`g6-docker`](../g6-docker/)
(tu primer contenedor) y a [`g15-docker-compose`](../g15-docker-compose/) (tu app y su base de datos con un solo
comando). Aquí escribes tu propio `Dockerfile` y ves por qué **el orden de sus líneas** decide cuánto tarda en
armarse: el mismo cambio de código reinstala todo con un orden y sale de la caché con el otro.

## Lo que hay en esta carpeta

| Archivo | Qué es |
|---|---|
| [`capas/Dockerfile`](capas/Dockerfile) | El `Dockerfile` en el orden correcto, con la base `node:24-slim` |
| [`capas/.dockerignore`](capas/.dockerignore) | Lo que no entra al armado: `node_modules` y `.git` |
| [`capas/servidor.js`](capas/servidor.js) | La app: un servidor de Express que responde en `http://localhost:3000` |
| [`capas/package.json`](capas/package.json) | La única dependencia: `express` |
| [`comandos.md`](comandos.md) | Los comandos del video, uno por línea, el orden lento para comparar y la base completa contra `slim` |

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `echo "// cambio" >> servidor.js` | Agrega una línea al final del código: un cambio real, de una línea |
| `time docker build -t capas:slim .` | Arma la imagen con el `Dockerfile` de esta carpeta y mide cuánto tardó |
| `docker image ls capas` | Lista las imágenes `capas` con su tamaño |

## La idea en una línea

Cada instrucción que cambia archivos es una capa en caché; si una cambia, se rehacen ella y todas las que siguen.
Lo que cambia poco va arriba (`FROM`, `COPY package.json ./`, `RUN npm install`) y tu código al final (`COPY . .`).

Necesitas Docker Desktop o Docker Engine en Linux: https://docs.docker.com/get-started/get-docker/

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Cómo funciona la caché de Docker | https://docs.docker.com/build/cache/ |
| Ordenar las capas y `.dockerignore` | https://docs.docker.com/build/cache/optimize/ |
| Contexto del armado y `.dockerignore` | https://docs.docker.com/build/concepts/context/ |
| Referencia del `Dockerfile` | https://docs.docker.com/reference/dockerfile/ |
| `docker build` | https://docs.docker.com/reference/cli/docker/buildx/build/ |
| Buenas prácticas (imagen base pequeña) | https://docs.docker.com/build/building/best-practices/ |
| Imagen oficial de Node.js | https://hub.docker.com/_/node |
| Express | https://expressjs.com/ |
| Video anterior: Docker Compose | [`../g15-docker-compose/`](../g15-docker-compose/) |

Datos verificados el 22 de noviembre de 2026 en la documentación oficial de Docker, Node.js, Express y npm. Ayemi no
tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
