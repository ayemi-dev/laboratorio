# La terminal, nivel 7 · encuentra cualquier cosa con find y grep

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows), que trae `find`, `grep`, `xargs` y `touch` de GNU. En Linux funciona igual. En macOS, `find`, `grep` y `touch` son otras versiones y algunas opciones cambian: consulta `man` en tu equipo.

## 1. Prepara la carpeta de práctica

Crea una carpeta vacía y entra en ella:

```sh
mkdir -p ~/practica-buscar
cd ~/practica-buscar
```

Guarda ahí los dos scripts de práctica, con saltos de línea **LF** (en VS Code, abajo a la derecha dice `CRLF` o `LF`):

- [`crear-practica.sh`](crear-practica.sh): crea `proyecto/` con cinco archivos.
- [`buscar.sh`](buscar.sh): los comandos de abajo, en el mismo orden.

Corre todo de una vez:

```sh
bash buscar.sh
```

O crea la carpeta y escribe cada comando a mano, desde `proyecto/`:

```sh
bash crear-practica.sh
cd proyecto
```

`crear-practica.sh` deja esto:

```text
proyecto/
├── app.py              usa saludar
├── docs/notas.md       una nota que menciona saludar
├── src/correo.py       usa saludar
├── src/saludo.py       define saludar
└── viejo/saludo_v1.py  una versión vieja (fecha de hace 10 días)
```

La fecha vieja la pone el script con `touch -d "10 days ago"`: así `find -mtime` tiene algo que encontrar.

**Antes de empezar, en Git Bash:** `type find` debe decir `/usr/bin/find`. Windows trae otro `find` que busca texto, no archivos; si te sale ese, abre Git Bash (no la consola de Windows).

## 2. Todos los archivos

```sh
find . -type f
```

```text
./app.py
./docs/notas.md
./src/correo.py
./src/saludo.py
./viejo/saludo_v1.py
```

El `.` es la carpeta actual: `find` empieza ahí y entra en todas las subcarpetas. `-type f` se queda solo con archivos (sin las carpetas). El orden puede cambiar en tu equipo.

## 3. Por extensión y por nombre

```sh
find . -name "*.py"
find . -name "saludo*"
```

`-name` compara el **nombre** del archivo (sin las carpetas) con un patrón: `*` vale por cualquier cosa. El primero da los cuatro `.py`; el segundo, `./src/saludo.py` y `./viejo/saludo_v1.py`.

**Las comillas importan:** sin ellas, la terminal cambia `*.py` por los archivos que haya en la carpeta actual antes de que `find` lo vea.

## 4. Por fecha

```sh
find . -mtime +7
```

```text
./viejo/saludo_v1.py
```

`-mtime` mide en días (de 24 horas) desde el último cambio: `+7` es más de siete, `-7` menos de siete. `find . -mtime -1` da lo que cambió en las últimas 24 horas.

## 5. Buscar dentro: `grep -rn`

```sh
grep -rn saludar
```

```text
app.py:1:from src.saludo import saludar
app.py:2:print(saludar("mundo"))
docs/notas.md:2:Pendiente: pruebas de saludar
src/correo.py:1:from .saludo import saludar
src/correo.py:4:    return saludar(n) + "."
src/saludo.py:1:def saludar(n):
viejo/saludo_v1.py:1:def saludar(n):
```

Cada línea es `archivo:número de línea:texto`. `-r` recorre todas las carpetas (sin carpeta, empieza en la actual) y `-n` da el número de línea. `-i` y `-n` ya salieron en [el nivel 4](../g16-terminal-tuberias/).

## 6. Contexto, mayúsculas y solo nombres

```sh
grep -rn -C 1 "def saludar" src
grep -rni pendiente
grep -rl saludar
```

- `-C 1` suma una línea antes y una después. Las de contexto llevan `-` en lugar de `:` (`src/saludo.py-2-…`). `-A 1` da solo la de después; `-B 1`, solo la de antes. Si hay varios grupos, `grep` los separa con `--`.
- `-i` ignora mayúsculas: `pendiente` encuentra `Pendiente`.
- `-l` da solo los nombres de los archivos que coinciden, una vez cada uno.

## 7. find y grep juntos: `xargs`

```sh
find . -name "*.py" | xargs grep -c saludar
```

```text
./app.py:2
./src/correo.py:2
./src/saludo.py:1
./viejo/saludo_v1.py:1
```

`find` elige los archivos (solo los `.py`, así `notas.md` queda fuera) y los manda por la tubería `|`. `xargs` los recibe y se los pasa a `grep` como si los hubieras escrito tú. `-c` cuenta las líneas que coinciden en cada archivo.

**Si tus archivos tienen espacios en el nombre**, usa esta forma, que no se confunde:

```sh
find . -name "*.py" -print0 | xargs -0 grep -c saludar
```

## 8. El caso útil: dónde se usa una función

```sh
grep -rn "saludar(" | grep -v "def "
```

```text
app.py:2:print(saludar("mundo"))
src/correo.py:4:    return saludar(n) + "."
```

Buscar `saludar(` con el paréntesis deja fuera las menciones sueltas (la nota) y los `import`. La segunda `grep`, con `-v`, se queda con las líneas que **no** dicen `def `: quita las definiciones. Quedan los dos lugares donde de verdad se llama a la función.

Cambia `saludar` por el nombre de tu función y corre lo mismo en tu proyecto. En JavaScript, cambia `"def "` por `"function "`.

## 9. Si algo no sale igual

- **`$'\r': command not found`:** el script se guardó con saltos de línea CRLF. Cámbialo a LF y vuelve a correrlo.
- **`ya existe proyecto/`:** `crear-practica.sh` no pisa una carpeta que ya existe. Bórrala tú o usa otra carpeta vacía.
- **`find` responde con un error que empieza con `FIND:`:** estás usando el `find` de Windows. Abre Git Bash.
- **`find . -mtime +7` no da nada:** revisa que `crear-practica.sh` haya corrido sin errores (`touch -d` es de GNU; en macOS cambia).
- **El orden de los resultados es otro, o los nombres salen con `./` delante en `grep -r`:** depende del sistema de archivos y de la versión; lo que se encuentra es lo mismo.

## Fuentes

- Manual de GNU find: https://www.gnu.org/software/findutils/manual/html_mono/find.html
- Manual de GNU grep: https://www.gnu.org/software/grep/manual/grep.html
- Páginas man: https://man7.org/linux/man-pages/man1/find.1.html, https://man7.org/linux/man-pages/man1/xargs.1.html, https://man7.org/linux/man-pages/man1/grep.1.html y https://man7.org/linux/man-pages/man1/touch.1.html
- Git for Windows: https://gitforwindows.org/

Datos verificados el 24 de noviembre de 2026.
