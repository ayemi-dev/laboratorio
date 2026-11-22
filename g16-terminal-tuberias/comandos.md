# La terminal, nivel 4 · tuberías, grep y redirecciones

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows) o en la terminal de **Linux**; al final, lo que cambia en Mac.

## 1. Prepara la carpeta de práctica

Usa la carpeta `mi-pagina` de los videos anteriores. Adentro deben estar:

- `notas.txt`, con las tres líneas de los videos anteriores (sin acentos):

  ```text
  falta: probar el sensor
  listo: comprar cables
  falta: subir el programa
  ```

- `app.log`, el [log de práctica](app.log) de esta guía (descárgalo o cópialo tal cual):

  ```text
  INFO: servidor iniciado
  ERROR: sensor sin respuesta
  WARN: memoria alta
  ERROR: sensor sin respuesta
  INFO: lectura guardada
  Error: disco lleno
  ERROR: sensor sin respuesta
  INFO: lectura guardada
  ```

Entra a la carpeta:

```sh
cd ~/mi-pagina
```

## 2. `grep`: busca una palabra

`grep` muestra las líneas que tienen la palabra que le pides. Distingue mayúsculas, así que esto no encuentra nada (en el log dice `ERROR` y `Error`, no `error`):

```sh
grep error app.log
```

Con `-i` deja de distinguirlas:

```sh
grep -i error app.log
```

```text
ERROR: sensor sin respuesta
ERROR: sensor sin respuesta
Error: disco lleno
ERROR: sensor sin respuesta
```

Con `-n`, además, te dice en qué línea está cada una (se pueden juntar: `-in`):

```sh
grep -in error app.log
```

```text
2:ERROR: sensor sin respuesta
4:ERROR: sensor sin respuesta
6:Error: disco lleno
7:ERROR: sensor sin respuesta
```

## 3. La tubería `|`: cuenta con `wc -l`

La barra `|` pasa lo que sale de un comando al siguiente. `wc -l` cuenta líneas, así que esto cuenta los errores:

```sh
grep -i error app.log | wc -l
```

```text
4
```

## 4. ¿Cuál se repite? `sort | uniq -c`

`uniq -c` junta las líneas iguales y dice cuántas veces aparece cada una, pero **solo si están seguidas**. Por eso va `sort` antes, que las ordena:

```sh
grep -i error app.log | sort | uniq -c
```

Sale una línea por cada error distinto, con su cuenta delante: `3` para `ERROR: sensor sin respuesta` y `1` para `Error: disco lleno`. El orden de las dos líneas y los espacios antes del número pueden cambiar según tu sistema.

## 5. Guárdalo: `>` y `>>`

`>` manda la salida a un archivo: si no existe, lo crea; si existe, **lo reescribe sin preguntar**. `>>` agrega al final, sin borrar lo que había.

```sh
grep -i error app.log > revisar.txt
grep -i warn app.log >> revisar.txt
wc -l revisar.txt
```

```text
5 revisar.txt
```

Cuatro errores más un aviso (`WARN`): cinco líneas en `revisar.txt`.

## 6. Los avisos de error, aparte: `2>`

Si le pides a `grep` un archivo que no existe, escribe un aviso en la pantalla:

```sh
grep -i error ayer.log
```

Ese aviso no sale por la salida normal, sino por la **salida de error**, y `2>` la manda a un archivo. La pantalla queda limpia y el aviso queda guardado:

```sh
grep -i error ayer.log 2> fallos.txt
cat fallos.txt
```

`cat fallos.txt` muestra el mismo aviso que antes salió en pantalla.

## 7. En toda la carpeta: `grep -r`

`-r` busca en todos los archivos de la carpeta (el punto `.` es la carpeta en la que estás). Con `-n`, cada línea dice de qué archivo y de qué línea viene:

```sh
grep -rn sensor .
```

Encuentra «sensor» en `app.log`, en el `revisar.txt` que acabas de crear y hasta en tu `notas.txt` (`falta: probar el sensor`). El orden de los archivos puede cambiar.

## 8. Si no funciona

- **`No such file or directory` con `app.log`.** No estás en la carpeta: entra primero con `cd ~/mi-pagina` y comprueba con `ls` que `app.log` está ahí.
- **`grep -i error app.log | wc -l` da otro número.** Revisa que copiaste el log completo, una entrada por línea.
- **`uniq -c` muestra la misma línea dos veces.** Te faltó `sort` antes: `uniq` solo junta las líneas iguales que están seguidas.
- **Perdiste lo que había en un archivo.** `>` lo reescribe. Para agregar, usa `>>`.

## 9. En Mac

En la Terminal de Mac, la barra `|`, `>` y `>>` funcionan igual. `grep`, `wc`, `sort` y `uniq` también están, pero no son las versiones de GNU que se usan en el video, así que la salida puede verse un poco distinta (por ejemplo, los espacios). Si una opción no hace lo mismo, revisa `man grep` (o el comando que sea) en tu Mac.

Fuentes: manual de GNU Bash 5.3 (Pipelines y Redirections), páginas man de GNU grep 3.12 y GNU coreutils 9.11 (`wc`, `sort` y `uniq`) en man7.org, y guía de la Terminal de Apple (Redirect Terminal input and output), consultados el 21 de noviembre de 2026.
