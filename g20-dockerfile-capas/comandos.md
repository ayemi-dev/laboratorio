# Tu propio Dockerfile, capas y caché · los comandos del video

Todo se corre dentro de la carpeta [`capas/`](capas/), donde está el `Dockerfile`, en **Git Bash**, macOS o Linux
(en PowerShell, mira la nota al final). Antes, abre Docker Desktop (o arranca Docker Engine en Linux).

La app es un servidor de Express de 13 líneas ([`capas/servidor.js`](capas/servidor.js)) con una sola dependencia,
`express` ([`capas/package.json`](capas/package.json)). Lo que importa aquí es cómo se arma su imagen.

## 1. El Dockerfile, línea por línea

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
CMD ["node", "servidor.js"]
```

| Línea | Qué hace |
|---|---|
| `FROM node:24-slim` | Parte de la imagen oficial de Node.js 24 en su variante `slim`, la que solo trae lo mínimo para correr `node` |
| `WORKDIR /app` | Las instrucciones que siguen trabajan en la carpeta `/app` de la imagen |
| `COPY package.json ./` | Copia **solo** la lista de dependencias |
| `RUN npm install` | Instala las dependencias de `package.json` (aquí, `express`) |
| `COPY . .` | Copia el resto del proyecto, menos lo que diga `.dockerignore` |
| `CMD ["node", "servidor.js"]` | El comando que corre el contenedor al arrancar |

Cada instrucción que cambia archivos es una **capa**, y Docker guarda cada capa en su **caché**. Si una capa cambia,
Docker rehace esa y **todas las que siguen**. Por eso el orden importa: lo que cambia poco (la base y las
dependencias) va arriba; lo que cambias a cada rato (tu código), al final.

## 2. Arma la imagen y pruébala

```bash
docker build -t capas:slim .
```

La primera vez descarga `node:24-slim` e instala `express`; tarda un poco más. Luego:

```bash
docker run --rm -d -p 3000:3000 --name capas capas:slim
curl http://localhost:3000
docker stop capas
```

```text
Hola desde tu propia imagen de Docker
```

## 3. El orden lento (para comparar)

Abre `Dockerfile`, cambia su contenido por este y guarda:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "servidor.js"]
```

Ármalo una vez para que la caché quede llena:

```bash
docker build -t capas:slim .
```

Ahora cambia una línea del código y vuelve a armar, midiendo el tiempo:

```bash
echo "// cambio" >> servidor.js
time docker build -t capas:slim .
```

`COPY . .` copia también `servidor.js`: como cambió, esa capa se rehace, y con ella `RUN npm install`, que va
después. En la salida verás el paso `RUN npm install` corriendo otra vez y, al final, el tiempo (`real`).

## 4. El orden correcto

Devuelve el `Dockerfile` al de la sección 1, ármalo una vez y repite el mismo cambio:

```bash
docker build -t capas:slim .
echo "// cambio" >> servidor.js
time docker build -t capas:slim .
```

Ahora `COPY package.json ./` y `RUN npm install` salen de la caché (`CACHED`): solo se rehace `COPY . .`. El tiempo
`real` baja (cuánto, depende de tu máquina y de tu conexión). Si cambias `package.json` (por ejemplo, agregas una dependencia), entonces sí se reinstala todo.

## 5. `.dockerignore`

```text
node_modules
.git
```

Lo que está en `.dockerignore` no entra al contexto del armado: `COPY . .` no se lleva tu `node_modules` (si
corriste `npm install` en tu computadora) ni la carpeta `.git`. Va en la raíz del contexto, junto al `Dockerfile`.

## 6. Cuánto pesa la base

Para comparar con la imagen completa de Node.js, cambia la primera línea del `Dockerfile` a `FROM node:24`, arma
con otra etiqueta y luego devuelve la línea a `FROM node:24-slim`:

```bash
docker build -t capas:completa .
docker image ls capas
```

Verás las dos etiquetas, `slim` y `completa`, con su tamaño. La de `slim` pesa mucho menos porque su base solo
trae lo mínimo para correr `node`.

> La documentación de la imagen oficial recomienda la imagen completa si no tienes límites de espacio o si tu app
> necesita más paquetes del sistema. Esta app, que solo usa Node.js y Express, corre bien con `slim`.

## 7. Limpia

```bash
docker image rm capas:slim capas:completa
```

## En PowerShell

- `time` es de Bash. En PowerShell, mide con `Measure-Command { docker build -t capas:slim . }`.
- Para el cambio de código, en lugar de `echo ... >>`, abre `servidor.js` en tu editor, agrega una línea al final
  (por ejemplo, `// cambio`) y guarda.

Fuentes: documentación de Docker (`https://docs.docker.com/build/cache/`,
`https://docs.docker.com/build/cache/optimize/`, `https://docs.docker.com/build/concepts/context/`,
`https://docs.docker.com/reference/dockerfile/` y `https://docs.docker.com/reference/cli/docker/buildx/build/`),
imagen oficial de Node.js (`https://hub.docker.com/_/node`), Express (`https://expressjs.com/`) y npm
(`https://docs.npmjs.com/cli/v11/commands/npm-install`), consultadas el 22 de noviembre de 2026.
