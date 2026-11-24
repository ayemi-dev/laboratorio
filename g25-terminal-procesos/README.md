# La terminal, nivel 6: procesos, ps, kill y segundo plano

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y sexta parte de la terminal, después de [la terminal sin miedo](../g4-terminal-sin-miedo/), [tuberías, redirecciones y tu primer script](../g9-terminal-scripts/), [alias, historial y atajos](../g12-terminal-atajos/), [tuberías, grep y redirecciones](../g16-terminal-tuberias/) y [variables de entorno y el PATH](../g18-terminal-variables/). Aquí, un servidor de práctica que corre de fondo: cómo lo ves, cómo lo pausas sin cerrarlo, cómo lo reanudas y cómo lo terminas. Se corre en `bash` en Linux: el video se grabó en un contenedor Linux de práctica con Docker (imagen oficial `python:3.13-slim`). En Git Bash (Windows), `kill -STOP` no congela a Python, que es un programa nativo de Windows (lo comprobamos el 23 de noviembre de 2026).

- **`&`** al final de un comando lo manda al fondo: la terminal no espera a que termine.
- **`$!`** guarda el número de proceso (PID) del último que mandaste al fondo.
- **`jobs`** lista los trabajos de esta terminal; **`ps`**, los procesos con su PID.
- **`kill -STOP`** pausa un proceso y **`kill -CONT`** lo reanuda; **`kill`** a secas lo termina. Aceptan el PID o el número de trabajo (`%1`).
- **`wait`** espera a que termine y deja su código de salida en `$?`.

## Los scripts de práctica

- [`servidor`](servidor) (2 líneas): arranca el servidor web de prueba de Python, solo en tu propia máquina (`127.0.0.1`, puerto 8000), y guarda lo que escribe en un archivo `log`.
- [`procesos.sh`](procesos.sh) (17 líneas): los comandos del video, en orden. Lo escribimos para el video.

Guárdalos en una carpeta vacía y córrelos desde ahí. No necesitas teclas especiales: todo va en el script.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `./servidor &` | Arranca el servidor de fondo |
| `echo $!` | Muestra el PID del último proceso de fondo |
| `jobs` | Lista los trabajos y su estado (`Running`, `Stopped`) |
| `ps -p $! \| cut -c1-9` | Busca ese PID en la lista de procesos (solo la columna del PID) |
| `curl -sI -m 2 127.0.0.1:8000 \| head -n 1` | Pregunta al servidor; espera 2 segundos como máximo |
| `kill -STOP $!` | Lo pausa (por PID) |
| `kill -CONT %1` | Lo reanuda (por número de trabajo) |
| `kill %1` | Lo termina (señal TERM) |
| `wait $!` | Espera a que salga |
| `echo $?` | Su código de salida: 143 = 128 + 15 (la señal TERM) |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Control de trabajos en Bash | https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html |
| `jobs`, `kill` y `wait` | https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html |
| `$!` y `$?` | https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html |
| `set -m` | https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html |
| Página man de Bash | https://man7.org/linux/man-pages/man1/bash.1.html |
| `ps` (procps-ng) | https://man7.org/linux/man-pages/man1/ps.1.html |
| Imagen oficial de Python en Docker | https://hub.docker.com/_/python |
| Señales de Cygwin (por qué Git Bash no pausa a Python) | https://cygwin.com/cygwin-ug-net/kill.html |
| Servidor de prueba de Python | https://docs.python.org/3/library/http.server.html |
| curl | https://curl.se/docs/manpage.html |
| Video anterior: variables de entorno y el PATH | [`../g18-terminal-variables/`](../g18-terminal-variables/) |

Datos verificados el 23 de noviembre de 2026 en la página man de GNU Bash 5.3, la página man de `ps` (procps-ng), la guía de usuario de Cygwin, Docker Hub, la documentación de Python y el manual de curl. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
