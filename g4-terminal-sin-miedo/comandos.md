# La terminal sin miedo · los diez comandos del video

| Comando | Qué hace |
|---|---|
| `pwd` | Imprime la ruta completa de la carpeta en la que estás |
| `ls` | Lista el contenido de la carpeta actual |
| `mkdir respaldos` | Crea la carpeta `respaldos` |
| `cp index.html respaldos/` | Copia `index.html` dentro de la carpeta `respaldos` |
| `cd respaldos` | Entra a la carpeta `respaldos` |
| `cd ..` | Regresa a la carpeta de arriba (nota el espacio entre `cd` y `..`) |
| `mv borrador.txt notas.txt` | Cambia el nombre de `borrador.txt` a `notas.txt` (o mueve un archivo) |
| `rm notas.txt` | Borra `notas.txt` directamente, sin pasar por la papelera |
| `clear` | Limpia la pantalla de la terminal |
| `code .` | Abre la carpeta actual en Visual Studio Code |

## Cómo preparar la carpeta de práctica

Para probar los comandos sin tocar tus archivos personales, crea una carpeta de práctica (por ejemplo `mi-pagina`) con dos archivos adentro:

- `index.html` con el contenido `<h1>Hola</h1>`
- `borrador.txt` con una línea de texto cualquiera

Si además ejecutas `cd fotos` cuando no existe una carpeta `fotos`, la terminal te muestra el mensaje de error (`bash: cd: fotos: No such file or directory` en Git Bash) sin romper nada.

## Aviso sobre `rm`

A diferencia de borrar desde el explorador de archivos, `rm` **no mueve los archivos a la Papelera de reciclaje** ni pide confirmación por defecto (para pedir confirmación existe la opción `-i`). Úsalo con calma y revisa el nombre antes de presionar Enter. Además, sin opciones adicionales, `rm` no borra carpetas.

## Dos trucos para no escribir de más

- **Tab:** escribe las primeras letras de un nombre (por ejemplo `ls res`) y presiona `Tab` para autocompletar a `ls respaldos/`.
- **Flecha hacia arriba (`↑`):** trae de vuelta los comandos que ejecutaste antes.

## Dónde abrir la terminal en cada sistema

- **Windows:** usa **Git Bash**, que viene incluido al instalar Git for Windows (`https://gitforwindows.org/`).
- **macOS:** abre la app **Terminal** (desde Spotlight o en `/Applications/Utilities`). Para poder usar `code .` en macOS, abre primero VS Code, abre la paleta de comandos (`Cmd+Shift+P`), escribe `shell command`, elige la opción para instalar `code` en el `$PATH` y abre una terminal nueva.
- **Linux:** abre la terminal de tu sistema (en Ubuntu: tutorial oficial para principiantes).

Fuentes: páginas de manual de GNU coreutils en man7.org (`pwd`, `ls`, `mkdir`, `cp`, `mv`, `rm`), manual de GNU Bash (*Bourne Shell Builtins* y *Commands For Completion*), Git for Windows (`https://gitforwindows.org/`), guía de Terminal de Apple (`https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac`), documentación de Visual Studio Code (`https://code.visualstudio.com/docs/configure/command-line`, `setup/windows`, `setup/mac`), manual de `clear` (ncurses) y tutorial de la terminal de Ubuntu (`https://ubuntu.com/tutorials/command-line-for-beginners`), consultadas el 16 de noviembre de 2026.
