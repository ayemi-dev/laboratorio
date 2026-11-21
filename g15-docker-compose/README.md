# Docker Compose: tu app y su base de datos con un solo comando

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi; sigue a [`g6-docker`](../g6-docker/).
Allá corriste un contenedor; aquí, una app de Node.js y su base de datos Postgres arrancan juntas con
`docker compose up -d`, se prueban, muestran sus registros y se borran con `docker compose down -v`.

## Lo que hay en esta carpeta

| Archivo | Qué es |
|---|---|
| [`visitas/compose.yaml`](visitas/compose.yaml) | Los dos servicios: `app` (tu Node.js) y `db` (Postgres), y el volumen `datos` |
| [`visitas/Dockerfile`](visitas/Dockerfile) | Cómo se arma la imagen de la app |
| [`visitas/servidor.js`](visitas/servidor.js) | La app: cada visita a `http://localhost:3000` se guarda en Postgres y responde cuántas van |
| [`visitas/package.json`](visitas/package.json) | La única dependencia: `pg` (node-postgres) |
| [`comandos.md`](comandos.md) | Los comandos del video, uno por línea, con lo que hace cada uno y la salida esperada |

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `docker compose up -d` | Arma la imagen de la app, crea la red y el volumen, y arranca los dos contenedores en segundo plano |
| `curl http://localhost:3000` | Visita la app; cada visita se guarda en Postgres |
| `docker compose logs app` | Muestra lo que imprimió la app |
| `docker compose down -v` | Apaga y borra los contenedores y la red; con `-v`, también el volumen con los datos |

Necesitas Docker Desktop (ya trae Docker Compose) o Docker Engine con el complemento de Compose en Linux:
https://docs.docker.com/get-started/get-docker/

> La contraseña `practica` de `compose.yaml` es solo para practicar en tu computadora. Con datos reales, la
> documentación de Docker pide no pasar contraseñas en variables de entorno: usa secretos
> (https://docs.docker.com/compose/how-tos/use-secrets/).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Qué es Docker Compose | https://docs.docker.com/compose/ |
| Referencia de `compose.yaml` | https://docs.docker.com/reference/compose-file/ |
| Orden de arranque y `service_healthy` | https://docs.docker.com/compose/how-tos/startup-order/ |
| Redes en Compose (por qué la app encuentra `db`) | https://docs.docker.com/compose/how-tos/networking/ |
| `docker compose up`, `logs` y `down` | https://docs.docker.com/reference/cli/docker/compose/ |
| Imagen oficial de Postgres | https://hub.docker.com/_/postgres |
| Imagen oficial de Node.js | https://hub.docker.com/_/node |
| node-postgres (`pg`) | https://node-postgres.com/ |
| Video anterior: Docker | [`../g6-docker/`](../g6-docker/) |

Datos verificados el 21 de noviembre de 2026 en la documentación oficial de Docker, PostgreSQL, Node.js y
node-postgres. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
