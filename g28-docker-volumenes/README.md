# Tus datos sobreviven al contenedor: volúmenes de Docker

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi; sigue a [`g6-docker`](../g6-docker/)
(tu primer contenedor), a [`g15-docker-compose`](../g15-docker-compose/) (tu app y su base de datos con un solo
comando) y a [`g20-dockerfile-capas`](../g20-dockerfile-capas/) (tu propio `Dockerfile`). Aquí ves **dónde viven los
datos** de un contenedor de PostgreSQL: sin volumen, el contenedor nuevo arranca vacío; con un volumen con nombre, tu
tabla sobrevive a `docker rm`.

## Lo que hay en esta carpeta

| Archivo | Qué es |
|---|---|
| [`g28-volumenes/compose.yaml`](g28-volumenes/compose.yaml) | Postgres de práctica con el volumen `g28-datos`, declarado como externo |
| [`comandos.md`](comandos.md) | Los comandos del video, en orden, la versión en una línea, el bind mount y los avisos |

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `export MSYS_NO_PATHCONV=1` | Solo en Git Bash: que no convierta `/var/lib/postgresql` en una ruta de Windows |
| `docker run -d --name g28-db …` | Crea y arranca el contenedor de práctica (con o sin `-v`) |
| `-v g28-datos:/var/lib/postgresql` | Monta el volumen `g28-datos` donde Postgres 18 guarda sus datos |
| `docker exec g28-db psql -U postgres -c "…"` | Corre SQL dentro del contenedor |
| `docker rm -f g28-db` | Borra el contenedor (un volumen con nombre se queda) |
| `docker volume ls --filter name=g28` | Lista solo los volúmenes que llevan `g28` en el nombre |
| `docker volume inspect g28-datos` | Muestra los datos del volumen, como dónde lo guarda Docker (`Mountpoint`) |
| `docker compose up -d` / `docker compose down` | Arranca y quita el mismo Postgres desde `compose.yaml` (el volumen externo no se toca) |
| `docker volume rm g28-datos` | Borra el volumen y sus datos |

## La idea en una línea

Lo que el contenedor guarda dentro de sí no pasa al contenedor nuevo; lo que guarda en un **volumen** sobrevive
hasta que tú borras el volumen. Un volumen lo crea y lo administra Docker; un **bind mount** es una carpeta de tu
computadora.

Necesitas Docker Desktop o Docker Engine en Linux: https://docs.docker.com/get-started/get-docker/

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Volúmenes | https://docs.docker.com/engine/storage/volumes/ |
| Bind mounts | https://docs.docker.com/engine/storage/bind-mounts/ |
| Dónde guarda datos Docker (resumen) | https://docs.docker.com/engine/storage/ |
| Volúmenes en Compose | https://docs.docker.com/reference/compose-file/volumes/ |
| `docker volume ls`, `inspect` y `rm` | https://docs.docker.com/reference/cli/docker/volume/ls/ |
| Imagen oficial de PostgreSQL | https://hub.docker.com/_/postgres |
| `psql` | https://www.postgresql.org/docs/current/app-psql.html |
| Git Bash y las rutas (Docker Desktop) | https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics/ |
| Video anterior: tu propio Dockerfile | [`../g20-dockerfile-capas/`](../g20-dockerfile-capas/) |

Datos verificados el 25 de noviembre de 2026 en la documentación oficial de Docker, la imagen oficial de PostgreSQL,
la documentación de PostgreSQL y las notas de Git para Windows. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
