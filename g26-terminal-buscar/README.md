# La terminal, nivel 7: encuentra cualquier cosa con find y grep

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y séptima parte de la terminal, después de [la terminal sin miedo](../g4-terminal-sin-miedo/), [tuberías, redirecciones y tu primer script](../g9-terminal-scripts/), [alias, historial y atajos](../g12-terminal-atajos/), [tuberías, grep y redirecciones](../g16-terminal-tuberias/), [variables de entorno y el PATH](../g18-terminal-variables/) y [procesos, ps, kill y segundo plano](../g25-terminal-procesos/). Aquí, un proyecto de práctica de cinco archivos y una pregunta: ¿dónde se usa esta función? Se corre en **Git Bash** (Windows), que trae las versiones GNU de `find`, `grep` y `xargs`; en Linux y macOS funciona igual.

- **`find`** busca archivos por fuera: por nombre o extensión (`-name`), por tipo (`-type f`) y por fecha (`-mtime`).
- **`grep`** busca dentro de los archivos: `-r` recorre las carpetas, `-n` da el número de línea, `-C` suma contexto, `-i` ignora mayúsculas, `-l` da solo los nombres, `-c` cuenta y `-v` se queda con lo que **no** coincide.
- **`xargs`** junta los dos: recibe los nombres que da `find` por la tubería y se los pasa a `grep`.

## Los scripts de práctica

- [`crear-practica.sh`](crear-practica.sh) (16 líneas): crea la carpeta `proyecto/` con cinco archivos cortos de Python y Markdown, y le pone a uno una fecha de hace diez días para practicar `-mtime`. Si `proyecto/` ya existe, avisa y no toca nada.
- [`buscar.sh`](buscar.sh) (13 líneas): los comandos del video, en orden. Lo escribimos para el video.

Guárdalos en una carpeta vacía y córrelos desde ahí con `bash buscar.sh`. No necesitas teclas especiales: todo va en el script.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `find . -type f` | Lista todos los archivos desde la carpeta actual |
| `find . -name "*.py"` | Busca por extensión |
| `find . -name "saludo*"` | Busca por el comienzo del nombre |
| `find . -mtime +7` | Lo que cambió hace más de 7 días |
| `grep -rn saludar` | Busca dentro de todo, con archivo y número de línea |
| `grep -rn -C 1 "def saludar" src` | Igual, con una línea de contexto |
| `grep -rni pendiente` | Sin distinguir mayúsculas |
| `grep -rl saludar` | Solo los nombres de los archivos |
| `find . -name "*.py" \| xargs grep -c saludar` | Cuántas líneas con `saludar` hay en cada `.py` |
| `grep -rn "saludar(" \| grep -v "def "` | Dónde se **usa** la función (sin sus definiciones) |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Manual de GNU find | https://www.gnu.org/software/findutils/manual/html_mono/find.html |
| Manual de GNU grep | https://www.gnu.org/software/grep/manual/grep.html |
| Página man de find | https://man7.org/linux/man-pages/man1/find.1.html |
| Página man de xargs | https://man7.org/linux/man-pages/man1/xargs.1.html |
| Página man de grep | https://man7.org/linux/man-pages/man1/grep.1.html |
| Página man de touch | https://man7.org/linux/man-pages/man1/touch.1.html |
| Git for Windows (Git Bash) | https://gitforwindows.org/ |
| Video anterior: procesos | [`g25-terminal-procesos/`](../g25-terminal-procesos/) |

Datos verificados el 24 de noviembre de 2026. Ayemi no tiene relación con GNU ni con Git for Windows.
