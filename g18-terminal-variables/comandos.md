# La terminal, nivel 5 · variables de entorno y el PATH

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows) o en la terminal de **Linux**; al final, lo que cambia en Mac.

## 1. Prepara el script de práctica

Crea una carpeta `bin` en tu carpeta de inicio y entra a tu carpeta de inicio:

```sh
mkdir -p ~/bin
cd ~
```

Guarda en `~/bin` el [script de práctica](saludo), con el nombre `saludo` (sin extensión) y estas dos líneas:

```sh
#!/bin/bash
echo "Hola, $NOMBRE"
```

Si lo escribes en Windows, guárdalo con saltos de línea **LF** (en VS Code, abajo a la derecha dice `CRLF` o `LF`). Luego dale permiso de ejecución (en Linux es obligatorio; en Git Bash no estorba):

```sh
chmod +x ~/bin/saludo
```

## 2. «command not found»

```sh
saludo
```

```text
bash: saludo: command not found
```

El script existe, pero la terminal no lo encuentra. Cuando un comando no lleva `/`, Bash lo busca en cada carpeta de una lista, y si no está en ninguna, avisa (con el código de salida 127).

## 3. La lista: `PATH`

```sh
echo $PATH
```

En el video salió `/usr/local/bin:/usr/bin:/bin`: es un PATH de práctica, corto, para que cupiera en pantalla. **El tuyo tendrá más carpetas**, separadas también por dos puntos. Tu carpeta `bin` no está en la lista.

## 4. Con la ruta, sí corre

Si el nombre lleva `/`, Bash no busca: corre ese archivo.

```sh
cat bin/saludo
bin/saludo
```

```text
Hola,
```

Corre, pero el nombre sale vacío: la variable `NOMBRE` no existe para el script.

## 5. Una variable: `NOMBRE=Ayemi`

Una variable se crea con un igual, **sin espacios** a los lados (`NOMBRE = Ayemi` haría que Bash buscara un comando llamado `NOMBRE`). Se lee con el signo de pesos:

```sh
NOMBRE=Ayemi
echo $NOMBRE
bin/saludo
```

```text
Ayemi
Hola,
```

La terminal la ve; el script, todavía no.

## 6. `export`: compártela con tus scripts

```sh
export NOMBRE
bin/saludo
```

```text
Hola, Ayemi
```

`export` marca la variable para que la reciban los programas y scripts que abras desde esta terminal. Sin `export`, solo vive en tu terminal.

## 7. Suma tu carpeta al `PATH`

`PATH` es una variable como `NOMBRE`, y ya viene exportada. Pon tu carpeta `bin` al principio y conserva las demás con `$PATH` al final:

```sh
export PATH=~/bin:$PATH
saludo
```

```text
Hola, Ayemi
```

Ahora `saludo` funciona como cualquier comando, desde cualquier carpeta. **No olvides `:$PATH`**: si lo quitas, la terminal deja de encontrar los comandos que ya tenías (si te pasa, cierra la terminal y abre otra).

## 8. Que dure: `~/.bashrc`

Todo lo anterior se pierde al cerrar la terminal. Bash lee `~/.bashrc` cada vez que abres una, así que agrega ahí la línea (si el archivo no existe, se crea):

```sh
echo 'export PATH=~/bin:$PATH' >> ~/.bashrc
tail -n 1 ~/.bashrc
```

```text
export PATH=~/bin:$PATH
```

Las comillas simples guardan la línea tal cual, sin cambiar `~` ni `$PATH`. Abre una terminal nueva y prueba `saludo`. Si también quieres que `NOMBRE` dure, agrega `export NOMBRE=Ayemi` de la misma forma.

## 9. Si no funciona

- **En una terminal nueva de Git Bash, `saludo` sigue sin encontrarse.** Git Bash puede abrir como terminal de inicio de sesión, que lee `~/.bash_profile` en lugar de `~/.bashrc`. Si tienes un `~/.bash_profile` que no carga tu `~/.bashrc`, agrégale al final esta línea (la del video de alias, [nivel 3](../g12-terminal-atajos/comandos.md)):

  ```sh
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

- **`bad interpreter` o `$'\r': command not found` al correr el script.** Tiene saltos de línea de Windows (CRLF): guárdalo con LF.
- **`Permission denied`.** Falta `chmod +x ~/bin/saludo`.
- **Dejaron de funcionar `ls`, `cat` y los demás.** Escribiste `export PATH=~/bin` sin `:$PATH`. Cierra la terminal, abre otra y revisa la línea de `~/.bashrc`.
- **`Hola,` sin nombre.** Te faltó `export NOMBRE`, o creaste la variable en otra terminal.

## 10. En Mac

Desde macOS 10.15, la Terminal de Mac usa **zsh**, no Bash. `NOMBRE=Ayemi`, `echo $NOMBRE`, `export` y `export PATH=~/bin:$PATH` funcionan igual, pero el archivo de inicio de zsh es `~/.zshrc`, no `~/.bashrc`:

```sh
echo 'export PATH=~/bin:$PATH' >> ~/.zshrc
```

Fuentes: manual de GNU Bash 5.3 (página man de Bash en man7.org: COMMAND EXECUTION, PARAMETERS, Shell Variables, Tilde Expansion, ENVIRONMENT, INVOCATION y `export`) y ayuda de Apple «Use zsh as the default shell on Mac», consultados el 22 de noviembre de 2026.
