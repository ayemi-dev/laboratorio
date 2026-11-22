# La terminal, nivel 4: tuberías, grep y redirecciones

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y cuarta parte de la terminal, después de [la terminal sin miedo](../g4-terminal-sin-miedo/), [tuberías, redirecciones y tu primer script](../g9-terminal-scripts/) y [alias, historial y atajos](../g12-terminal-atajos/). Aquí, una línea de terminal responde preguntas sobre un archivo de registro (log): cuántos errores tiene y cuál se repite. En Git Bash (Windows) y en Linux; en Mac, casi igual.

- **`grep -i`**: busca una palabra sin importar mayúsculas. **`-n`** dice en qué línea está; **`-r`** busca en toda la carpeta.
- **`|`** (tubería): lo que sale de un comando entra al siguiente.
- **`wc -l`**: cuenta líneas. **`sort | uniq -c`**: ordena y cuenta las líneas repetidas.
- **`>`** guarda en un archivo (lo crea o lo reescribe), **`>>`** agrega al final y **`2>`** manda los avisos de error a otro archivo.

## El log de práctica

[`app.log`](app.log) tiene 8 líneas que escribimos para el video (no es el registro de ningún programa real). Descárgalo en tu carpeta `mi-pagina`, junto al `notas.txt` de los videos anteriores, y repite cada paso.

## Los comandos del video

| Comando | Qué responde |
|---|---|
| `grep -i error app.log` | ¿Qué líneas dicen «error», con mayúsculas o sin ellas? |
| `grep -in error app.log` | ¿En qué línea está cada una? |
| `grep -i error app.log \| wc -l` | ¿Cuántas son? |
| `grep -i error app.log \| sort \| uniq -c` | ¿Cuántas veces se repite cada una? |
| `grep -i error app.log > revisar.txt` | Guárdalas en un archivo |
| `grep -i warn app.log >> revisar.txt` | Agrega los avisos al final, sin borrar |
| `grep -i error ayer.log 2> fallos.txt` | Si algo falla, el aviso va a otro archivo |
| `grep -rn sensor .` | ¿Dónde dice «sensor» en toda la carpeta? |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Tuberías en Bash | https://www.gnu.org/software/bash/manual/html_node/Pipelines.html |
| Redirecciones en Bash (`>`, `>>`, `2>`) | https://www.gnu.org/software/bash/manual/html_node/Redirections.html |
| `grep` | https://man7.org/linux/man-pages/man1/grep.1.html |
| `wc` | https://man7.org/linux/man-pages/man1/wc.1.html |
| `sort` | https://man7.org/linux/man-pages/man1/sort.1.html |
| `uniq` | https://man7.org/linux/man-pages/man1/uniq.1.html |
| Redirigir en la Terminal de Mac | https://support.apple.com/guide/terminal/redirect-terminal-input-and-output-apd1dbe647b-7e11-49dc-aa76-89aa7e53ce36/mac |
| Video anterior: alias, historial y atajos | [`../g12-terminal-atajos/`](../g12-terminal-atajos/) |

Datos verificados el 21 de noviembre de 2026 en el manual de Bash de GNU, las páginas man de GNU (grep 3.12 y coreutils 9.11) y la guía de la Terminal de Apple. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
