# La terminal, nivel 5: variables de entorno y el PATH

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y quinta parte de la terminal, después de [la terminal sin miedo](../g4-terminal-sin-miedo/), [tuberías, redirecciones y tu primer script](../g9-terminal-scripts/), [alias, historial y atajos](../g12-terminal-atajos/) y [tuberías, grep y redirecciones](../g16-terminal-tuberias/). Aquí, un script que está en tu carpeta y la terminal dice `command not found`: por qué pasa y cómo se arregla. En Git Bash (Windows) y en Linux; en Mac, casi igual.

- **Una variable** guarda un valor: se crea con `NOMBRE=Ayemi` y se lee con `$NOMBRE`.
- **`export`** pasa la variable a los programas y scripts que abres desde esa terminal. Sin `export`, tu script no la ve.
- **`PATH`** es la variable con la lista de carpetas, separadas por dos puntos, donde la terminal busca comandos. Si tu comando no está en ninguna, sale `command not found`.
- **`~/.bashrc`** es el archivo que Bash lee al abrir una terminal: lo que pongas ahí dura.

## El script de práctica

[`saludo`](saludo) tiene 2 líneas que escribimos para el video. Guárdalo en una carpeta `bin` dentro de tu carpeta de inicio (`~/bin/saludo`) y repite cada paso.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `echo $PATH` | Muestra las carpetas donde la terminal busca comandos |
| `bin/saludo` | Corre el script con su ruta, sin buscarlo |
| `NOMBRE=Ayemi` | Crea una variable (solo en esta terminal) |
| `echo $NOMBRE` | La lee |
| `export NOMBRE` | La pasa a los programas y scripts que abras |
| `export PATH=~/bin:$PATH` | Suma tu carpeta `bin` al principio del PATH |
| `echo 'export PATH=~/bin:$PATH' >> ~/.bashrc` | Lo deja fijo para las terminales nuevas |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Cómo busca comandos Bash | https://www.gnu.org/software/bash/manual/html_node/Command-Search-and-Execution.html |
| Variables de Bash (`PATH`, `HOME`) | https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Variables.html |
| `export` | https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html |
| Archivos de inicio (`~/.bashrc`) | https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html |
| Página man de Bash | https://man7.org/linux/man-pages/man1/bash.1.html |
| zsh en Mac | https://support.apple.com/en-us/102360 |
| Video anterior: tuberías, grep y redirecciones | [`../g16-terminal-tuberias/`](../g16-terminal-tuberias/) |

Datos verificados el 22 de noviembre de 2026 en el manual de Bash de GNU (página man de Bash 5.3) y la ayuda de Apple sobre zsh. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
