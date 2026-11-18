# G6 · Docker: «en mi máquina sí funciona»

Guía y archivos de ejemplo del video **G6** del **Laboratorio Ayemi**: lleva el entorno de tu proyecto con Docker usando un `Dockerfile` mínimo de dos líneas y la imagen oficial de nginx.

## Glosario

- **Imagen:** paquete con todo lo que tu aplicación necesita para correr; una vez creada, no cambia.
- **Contenedor:** una imagen en marcha, aislada; corre igual en tu computadora o en la nube.
- **Dockerfile:** archivo de texto con las instrucciones para crear la imagen.
- **`FROM`:** indica la imagen base de la que partes.
- **`COPY`:** copia archivos de tu computadora a la imagen.

## Pasos con `mi-pagina`

1. En la carpeta `mi-pagina`, junto a `index.html`, crea un archivo llamado `Dockerfile` (sin extensión) con estas dos líneas:

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
```

2. Desde la carpeta `mi-pagina`, construye la imagen:

```bash
docker build -t mi-pagina .
```

3. Corre el contenedor publicando el puerto `8080` de tu computadora hacia el `80` del contenedor:

```bash
docker run -d -p 8080:80 mi-pagina
```

4. Abre `http://localhost:8080` en tu navegador.

5. Para detenerlo fácil, córrelo con nombre y luego usa `docker ps` y `docker stop`:

```bash
docker run --name mi-pagina -d -p 8080:80 mi-pagina
docker ps
docker stop mi-pagina
```

## Instalar Docker y fuentes oficiales

- Instalar Docker (Docker Desktop en Windows, Mac y Linux; Docker Engine directo en Linux con licencia Apache 2.0): https://docs.docker.com/get-started/get-docker/
- Qué es un contenedor: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
- Imagen oficial de nginx en Docker Hub: https://hub.docker.com/_/nginx
- Referencia de `Dockerfile`: https://docs.docker.com/reference/dockerfile/

Datos verificados el 17 de noviembre de 2026 en la documentación oficial de Docker y en la página oficial de nginx en Docker Hub. Ayemi no tiene relación con Docker, Inc. ni con nginx.
