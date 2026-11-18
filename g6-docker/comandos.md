# Comandos · G6 · Docker: «en mi máquina sí funciona»

## Dockerfile (`mi-pagina/Dockerfile`)

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
```

## Comandos principales (desde `mi-pagina/`)

```bash
docker build -t mi-pagina .
docker run -d -p 8080:80 mi-pagina
```

Navegador: `http://localhost:8080`

## Comandos para nombrar, listar y detener

```bash
docker run --name mi-pagina -d -p 8080:80 mi-pagina
docker ps
docker stop mi-pagina
```

## Fuentes oficiales (verificadas el 17 de noviembre de 2026)

- Instalar Docker: https://docs.docker.com/get-started/get-docker/
- Qué es Docker: https://docs.docker.com/get-started/docker-overview/
- Qué es una imagen: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/
- Qué es un contenedor: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
- Escribir un Dockerfile: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
- Referencia de Dockerfile: https://docs.docker.com/reference/dockerfile/
- Imagen oficial de nginx: https://hub.docker.com/_/nginx
