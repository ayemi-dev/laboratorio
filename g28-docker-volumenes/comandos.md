# Volúmenes de Docker · los comandos del video

Todo se corre en **Git Bash**, la Terminal de Mac o Linux, dentro de la carpeta [`g28-volumenes/`](g28-volumenes/)
(donde está `compose.yaml`). Antes, abre Docker Desktop (o arranca Docker Engine en Linux).

Los nombres son de práctica y todos llevan `g28`: el contenedor `g28-db` y el volumen `g28-datos`. Si ya tienes algo
con esos nombres, cámbialos en todos los comandos. **Nunca borres lo que no es tuyo:** en tu computadora puede haber
volúmenes de otros proyectos con datos que importan.

Cuando un renglón termina en `\`, el comando sigue en el renglón de abajo: copia el bloque entero. Al final de cada
paso tienes la versión en una sola línea.

## 0. Solo en Git Bash

```bash
export MSYS_NO_PATHCONV=1
```

Git Bash convierte los argumentos que parecen rutas de Linux (como `/var/lib/postgresql`) en rutas de Windows, y el
`-v` llega roto a Docker (la documentación de Docker Desktop muestra el error `mount destination … not absolute`).
Esta variable lo apaga mientras dure la ventana. En Mac y Linux no hace falta.

## 1. Sin volumen: el contenedor nuevo arranca vacío

Crea un Postgres de práctica (la imagen exige una contraseña; `practica` es solo para este ejercicio):

```bash
docker run -d --name g28-db \
  -e POSTGRES_PASSWORD=practica \
  postgres:18-alpine
```

Espera unos segundos a que arranque (si el paso siguiente dice que no puede conectarse, espera y repítelo). Crea una
tabla con una fila:

```bash
docker exec g28-db psql -U postgres \
  -c "CREATE TABLE notas (texto text)" \
  -c "INSERT INTO notas VALUES ('hola')"
```

Borra el contenedor, crea otro igual y busca la tabla:

```bash
docker rm -f g28-db
docker run -d --name g28-db \
  -e POSTGRES_PASSWORD=practica \
  postgres:18-alpine
docker exec g28-db psql -U postgres \
  -c "SELECT * FROM notas"
```

```text
ERROR:  relation "notas" does not exist
```

**¿Por qué?** La imagen de Postgres guarda sus datos en un volumen **anónimo** (con un nombre al azar), uno por
contenedor. El contenedor nuevo recibió otro, vacío; tu tabla quedó en el anónimo del contenedor que borraste. Para no
dejar anónimos sueltos, borra este contenedor con `-v`, que se lleva sus volúmenes anónimos:

```bash
docker rm -f -v g28-db
```

(El del primer contenedor ya quedó suelto: búscalo con `docker volume ls` y bórralo **por su nombre** solo si estás
seguro de que es de este ejercicio.)

En una línea:

```bash
docker run -d --name g28-db -e POSTGRES_PASSWORD=practica postgres:18-alpine
docker exec g28-db psql -U postgres -c "CREATE TABLE notas (texto text)" -c "INSERT INTO notas VALUES ('hola')"
docker exec g28-db psql -U postgres -c "SELECT * FROM notas"
```

## 2. Con un volumen con nombre: la tabla sobrevive

```bash
docker run -d --name g28-db \
  -e POSTGRES_PASSWORD=practica \
  -v g28-datos:/var/lib/postgresql \
  postgres:18-alpine
docker exec g28-db psql -U postgres \
  -c "CREATE TABLE notas (texto text)" \
  -c "INSERT INTO notas VALUES ('hola')"
```

`-v g28-datos:/var/lib/postgresql` monta el volumen `g28-datos` en la carpeta donde Postgres guarda sus datos. Si el
volumen no existe, Docker lo crea. Ahora borra el contenedor y crea otro **con el mismo volumen**:

```bash
docker rm -f g28-db
docker run -d --name g28-db \
  -e POSTGRES_PASSWORD=practica \
  -v g28-datos:/var/lib/postgresql \
  postgres:18-alpine
docker exec g28-db psql -U postgres \
  -c "SELECT * FROM notas"
```

```text
 texto
-------
 hola
(1 row)
```

`docker rm` no borra un volumen con nombre: los datos estaban fuera del contenedor.

**Ojo con la carpeta:** desde Postgres 18 el volumen va en `/var/lib/postgresql`. En Postgres 17 o anterior, en
`/var/lib/postgresql/data`.

En una línea:

```bash
docker run -d --name g28-db -e POSTGRES_PASSWORD=practica -v g28-datos:/var/lib/postgresql postgres:18-alpine
```

## 3. Ver tus volúmenes

```bash
docker volume ls --filter name=g28
docker volume inspect g28-datos
```

`--filter name=g28` muestra solo los volúmenes que llevan `g28` en el nombre. `inspect` da sus datos; `Mountpoint` es
dónde lo guarda Docker (en Docker Desktop, dentro de su máquina virtual Linux: no es una carpeta de Windows ni de
Mac).

## 4. Volumen o bind mount

| | Volumen | Bind mount |
|---|---|---|
| Ejemplo | `-v g28-datos:/var/lib/postgresql` | `-v "$(pwd)/datos":/var/lib/postgresql` |
| Antes de `:` va | un **nombre** | una **ruta** de tu computadora |
| Quién lo administra | Docker (`docker volume ls`, `inspect`, `rm`) | tú: es una carpeta tuya |
| Cuándo | datos de la app, como una base de datos | ver o editar los archivos desde tu computadora, como tu código |

El video no corre el bind mount. Si lo pruebas en Git Bash, deja puesta la variable del paso 0: Docker Desktop acepta
las rutas al estilo de Git Bash (`/c/Users/…`). Si la carpeta no existe, Docker la crea.

## 5. El mismo volumen en Compose

Primero quita el contenedor de `docker run` (el volumen se queda):

```bash
docker rm -f g28-db
```

[`compose.yaml`](g28-volumenes/compose.yaml):

```yaml
services:
  db:
    image: postgres:18-alpine
    container_name: g28-db
    environment:
      POSTGRES_PASSWORD: practica
    volumes:
      - g28-datos:/var/lib/postgresql

volumes:
  g28-datos:
    external: true
```

- `volumes:` de abajo declara el volumen; `external: true` dice que **ya existe** (lo creaste en el paso 2): Compose no
  lo crea y, si no existe, da un error.
- `container_name: g28-db` deja el mismo nombre de contenedor, así la consulta es la misma de antes.

```bash
docker compose up -d
docker exec g28-db psql -U postgres \
  -c "SELECT * FROM notas"
```

Sale `hola` otra vez: el mismo volumen, ahora desde Compose.

## 6. Borrar, cuando tú lo decidas

```bash
docker compose down
docker volume rm g28-datos
docker volume ls --filter name=g28
```

- `docker compose down` quita el contenedor y la red, pero **nunca** un volumen externo.
- `docker volume rm` sí borra el volumen y sus datos. No puede borrar uno que un contenedor esté usando: por eso va
  después de `down`.
- La última lista sale vacía: ya no queda nada del ejercicio.

## Avisos

- **Borra solo lo tuyo, por su nombre.** Los comandos que limpian todo de golpe (los que terminan en `prune`) pueden
  llevarse volúmenes de otros proyectos.
- **La contraseña del ejercicio es de práctica.** En un proyecto real no se escribe en el comando ni se sube al
  repositorio.
- Si usaste `docker compose down -v` (como en el video de Compose): borra los volúmenes con nombre **declarados** en el
  archivo, pero no los externos.

Fuentes: documentación oficial de Docker (volúmenes, https://docs.docker.com/engine/storage/volumes/; bind mounts,
https://docs.docker.com/engine/storage/bind-mounts/; Compose, https://docs.docker.com/reference/compose-file/volumes/;
Docker Desktop en Git Bash, https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics/), imagen
oficial de PostgreSQL (https://hub.docker.com/_/postgres), `psql` (https://www.postgresql.org/docs/current/app-psql.html)
y notas de Git para Windows 2.56.1, consultadas el 25 de noviembre de 2026.
