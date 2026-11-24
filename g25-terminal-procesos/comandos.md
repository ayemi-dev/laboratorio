# La terminal, nivel 6 · procesos, ps, kill y segundo plano

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en `bash` en **Linux**: el video se grabó en un contenedor Linux de práctica con Docker (imagen oficial `python:3.13-slim`, con `curl` y `procps` instalados). Necesitas Python 3 (el servidor de prueba viene incluido), `curl` y `ps`. **En Git Bash (Windows) no sale igual:** ver la sección 10.

## 1. Prepara la carpeta de práctica

Crea una carpeta vacía y entra en ella:

```sh
mkdir -p ~/practica-procesos
cd ~/practica-procesos
```

Guarda ahí los dos scripts de práctica, con saltos de línea **LF** (en VS Code, abajo a la derecha dice `CRLF` o `LF`):

- [`servidor`](servidor), sin extensión:

  ```sh
  #!/bin/bash
  exec python -m http.server -b 127.0.0.1 &>log
  ```

- [`procesos.sh`](procesos.sh): los comandos de abajo, en el mismo orden.

Dale permiso de ejecución al servidor y corre el script:

```sh
chmod +x servidor
bash procesos.sh
```

`-b 127.0.0.1` hace que el servidor solo responda en tu propia máquina. Es un servidor **de prueba**: Python avisa que no es para producción.

**¿Por qué un script y `set -m`?** En una terminal interactiva el control de trabajos ya viene encendido; en un script, no. La línea `set -m` lo enciende, para que `jobs` y `%1` funcionen igual que cuando escribes a mano. Así no hace falta ninguna tecla especial.

## 2. Al fondo con `&`

```sh
cat servidor
./servidor &
echo $!
```

El `&` al final manda el comando al fondo: la terminal no espera a que termine y sigue con la línea siguiente. `$!` guarda el número de proceso (PID) del último que mandaste al fondo. Sale un número, distinto cada vez (en el video, `414`).

Si escribes `./servidor &` a mano, la terminal además te muestra algo como `[1] 414`: el número de trabajo entre corchetes y el PID.

## 3. Verlo: `jobs` y `ps`

```sh
jobs
ps -p $! | cut -c1-9
```

```text
[1]+  Running                 ./servidor &
  PID TTY
  414 ?
```

`jobs` lista los trabajos de **esta** terminal: el 1 está corriendo (`Running`). `ps` lista los procesos; `-p $!` busca solo el de tu servidor y `cut -c1-9` conserva los primeros nueve caracteres: el PID (el mismo número de `echo $!`) y el inicio de `TTY` (`?`: no está atado a una terminal). Si corres `ps -p $!` sin `cut`, verás también las columnas `TIME` y `CMD`.

## 4. Pregúntale al servidor

```sh
sleep 1
curl -sI -m 2 127.0.0.1:8000 | head -n 1
```

```text
HTTP/1.0 200 OK
```

`sleep 1` le da un segundo para arrancar. `curl -sI` pide solo los encabezados, sin barra de progreso; `-m 2` espera dos segundos como máximo. `200 OK`: está vivo y contesta.

## 5. Pausa: `kill -STOP`

```sh
kill -STOP $!
curl -sI -m 2 127.0.0.1:8000 | head -n 1
jobs
```

```text
[1]+  Stopped                 ./servidor
```

`kill` no solo termina procesos: manda **señales**. `STOP` congela el proceso sin cerrarlo. `curl` espera sus dos segundos y no imprime nada: el servidor no contesta. `jobs` lo confirma: `Stopped`, detenido.

## 6. Reanudar: `kill -CONT %1`

```sh
kill -CONT %1
curl -sI -m 2 127.0.0.1:8000 | head -n 1
```

```text
HTTP/1.0 200 OK
```

`CONT` lo despierta donde se quedó. Esta vez no usamos el PID sino `%1`, el número de trabajo que muestra `jobs`: `kill` acepta los dos.

## 7. Terminar: `kill`, `wait` y `$?`

```sh
kill %1
wait $!
echo $?
```

```text
143
```

`kill` sin señal manda `TERM`, la de «termina, por favor». `wait` espera a que el proceso salga y `$?` guarda su código de salida. Cuando un proceso termina por la señal número *n*, Bash da `128 + n`: `TERM` es la 15, así que sale `143`. Puede aparecer también un aviso como `[1]+  Terminated  ./servidor`.

## 8. Si no funciona

- **`python: command not found`.** En Linux suele llamarse `python3`: cambia `python` por `python3` en `servidor`.
- **`ps: command not found`.** Algunas imágenes mínimas de Linux no lo traen: viene en el paquete `procps`.
- **El primer `curl` no imprime nada.** El servidor tardó más de un segundo en arrancar: cambia `sleep 1` por `sleep 2`.
- **`curl` no imprime nada nunca.** Otro programa ya usa el puerto 8000. Cierra lo que lo use o cambia el puerto en `servidor` y en los `curl` (por ejemplo, `-b 127.0.0.1 8080` y `127.0.0.1:8080`).
- **`kill: %1: no such job`.** Corriste el script sin `set -m`, o el trabajo ya terminó.
- **`bad interpreter` o `$'\r': command not found`.** Guardaste los scripts con CRLF: guárdalos con LF.
- **Lo que escribe el servidor.** Va al archivo `log` de la carpeta; ábrelo con `cat log`.

## 9. Ctrl+Z, `fg` y `bg` (no salen en el video)

Si un programa corre **en primer plano** en una terminal interactiva, Ctrl+Z lo detiene y te devuelve la terminal (el manual de Bash: «Typing the suspend character (typically ^Z, Control-Z) while a process is running stops that process»). Luego `bg` lo sigue de fondo y `fg` lo trae al frente. En el video usamos `kill -STOP` y `kill -CONT`, que hacen lo mismo desde un script, sin teclas.

## 10. ¿Y en Git Bash (Windows)?

Ahí Python es un programa nativo de Windows, y las señales de Git Bash (que vienen de Cygwin/MSYS2) no lo congelan: lo probamos el 23 de noviembre de 2026 y, después de `kill -STOP $!`, `curl` siguió recibiendo `HTTP/1.0 200 OK` y `jobs` siguió diciendo `Running`. Por eso el video se grabó en `bash` dentro de un contenedor Linux con Docker, donde Python es un proceso de Linux. Además, en Git Bash `ps` muestra otras columnas (entre ellas `WINPID` y la ruta completa del programa, con tu carpeta de usuario).

Fuentes: manual de GNU Bash 5.3 (página man de Bash en man7.org: JOB CONTROL, Lists, Special Parameters, `jobs`, `kill`, `wait`, `set -m`, Simple Commands), página man de `ps` (procps-ng), guía de usuario de Cygwin (`ps` y `kill`), imagen oficial de Python en Docker Hub, documentación de Python (`http.server`) y manual de curl, consultados el 23 de noviembre de 2026.
