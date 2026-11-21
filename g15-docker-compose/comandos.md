# Docker Compose · los comandos del video

Todo se corre dentro de la carpeta [`visitas/`](visitas/), donde está `compose.yaml`. Funcionan igual en Git Bash,
PowerShell, macOS y Linux. Antes, abre Docker Desktop (o arranca Docker Engine en Linux) y deja libre el puerto 3000.

## 1. Arranca la app y su base de datos

```bash
docker compose up -d
```

La primera vez descarga `postgres:18-alpine` y `node:24-alpine` y arma la imagen de la app; tarda un poco más. Al
final verás algo así (los nombres salen de la carpeta `visitas`):

```text
✔ Network visitas_default    Created
✔ Volume visitas_datos       Created
✔ Container visitas-db-1     Healthy
✔ Container visitas-app-1    Started
```

La app no arranca hasta que Postgres responde: eso lo hacen `depends_on` con `condition: service_healthy` y el
`healthcheck` con `pg_isready` de `compose.yaml`.

## 2. Pruébala

```bash
curl http://localhost:3000
curl http://localhost:3000
```

```text
Visitas guardadas en Postgres: 1
Visitas guardadas en Postgres: 2
```

También puedes abrir `http://localhost:3000` en el navegador. Cada visita es una fila nueva en la tabla `visitas`.

## 3. Mira lo que imprimió la app

```bash
docker compose logs app
```

```text
app-1  | Tabla visitas lista en Postgres
app-1  | App escuchando en el puerto 3000
```

Para seguirlos en vivo: `docker compose logs -f app` (sales con `Ctrl+C`). Para ver los contenedores del proyecto:
`docker compose ps`.

## 4. Apaga y borra todo

```bash
docker compose down -v
```

```text
✔ Container visitas-app-1    Removed
✔ Container visitas-db-1     Removed
✔ Volume visitas_datos       Removed
✔ Network visitas_default    Removed
```

- `docker compose down` (sin `-v`) borra los contenedores y la red, pero **conserva el volumen**: al volver a correr
  `docker compose up -d`, el contador sigue donde iba.
- Con `-v` también borra el volumen `datos`: **los datos de Postgres se pierden**. Úsalo solo cuando quieras
  empezar de cero.

## Si cambias el código de la app

```bash
docker compose up -d --build
```

`--build` vuelve a armar la imagen antes de arrancar.

## Qué dice cada parte de `compose.yaml`

| Línea | Qué hace |
|---|---|
| `build: .` | Arma la imagen de la app con el `Dockerfile` de esta carpeta |
| `ports: - "3000:3000"` | Une el puerto 3000 de tu computadora con el 3000 del contenedor |
| `PGHOST: db` | La app encuentra la base por el nombre del servicio, `db` |
| `PGUSER`, `PGPASSWORD`, `PGDATABASE` | Con qué usuario, contraseña y base se conecta `pg` |
| `depends_on` + `condition: service_healthy` | La app espera a que la base esté lista |
| `image: postgres:18-alpine` | Imagen oficial de Postgres 18 |
| `POSTGRES_PASSWORD: practica` | La contraseña del usuario `postgres` (obligatoria en la imagen) |
| `datos:/var/lib/postgresql` | Guarda los datos en el volumen `datos` (desde Postgres 18 se monta en esa ruta) |
| `test: pg_isready -U postgres` | Revisa si Postgres ya acepta conexiones |
| `interval: 2s` y `retries: 10` | Revisa cada 2 s, hasta 10 veces seguidas sin respuesta (sin `interval` serían 30 s) |

> `practica` es una contraseña de juguete, solo para tu computadora. Con datos reales no pases contraseñas en
> variables de entorno: usa secretos (https://docs.docker.com/compose/how-tos/use-secrets/).

Fuentes: documentación de Docker Compose (`https://docs.docker.com/compose/`, referencia de `compose.yaml` y de los
comandos `docker compose up`, `logs`, `down`, `ps` y `build`), imagen oficial de Postgres
(`https://hub.docker.com/_/postgres`), imagen oficial de Node.js (`https://hub.docker.com/_/node`), node-postgres
(`https://node-postgres.com/features/connecting`) y `pg_isready`
(`https://www.postgresql.org/docs/current/app-pg-isready.html`), consultadas el 21 de noviembre de 2026.
