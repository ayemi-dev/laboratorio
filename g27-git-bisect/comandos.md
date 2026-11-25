# Encuentra el commit que rompió todo · los comandos del video

| Comando | Qué hace |
|---|---|
| `bash practica.sh` | Arma `practica-bisect/` con veinte commits y deja `prueba.sh` junto a él |
| `bash calc.sh 2 3` | Prueba la suma: debería dar `5` |
| `git bisect start` | Empieza la búsqueda |
| `git bisect bad` | Marca como malo el commit donde estás |
| `git bisect good v1.0` | Marca como buena la versión `v1.0`; Git salta a un commit de en medio |
| `git bisect good` | Tras probar, el commit de en medio está bien (si está mal: `git bisect bad`) |
| `git bisect run bash ../prueba.sh` | Corre `prueba.sh` en cada salto y se detiene en el primer commit malo |
| `git bisect reset` | Cierra la búsqueda y te regresa a donde estabas |

## Cómo leer el resultado

Al final, `git bisect run` (o tu última respuesta a mano) muestra algo así:

- **`HASH is the first bad commit`**: ese es el **primer commit malo**. Todo lo anterior funcionaba; desde ese commit,
  no. En el repositorio de práctica es «Ordena calc.sh» (`54644c9`).
- Debajo, el commit: autor, fecha y **mensaje**. Ojo: el mensaje puede no avisar del error («Ordena calc.sh» suena
  inofensivo).
- Luego, el **resumen de archivos** que tocó ese commit (aquí, solo `calc.sh`).
- Para ver la **línea exacta** que cambió, abre ese commit con `git show` (como en el video anterior):

  ```bash
  git show 54644c9
  ```

  Verás que `echo $(( $1 + $2 ))` pasó a `echo $(( $1 - $2 ))`: la suma se volvió resta.

Y no olvides `git bisect reset`: mientras la búsqueda sigue abierta, estás en un commit viejo, no en tu rama.

## La prueba para `git bisect run`

`git bisect run` corre el comando que le des en cada commit y mira **cómo sale**:

| Sale con | Git entiende |
|---|---|
| `0` | Este commit está **bien** (`good`) |
| De `1` a `127`, menos `125` | Este commit está **mal** (`bad`) |
| `125` | Este commit **no se puede probar**: sáltalo |
| Cualquier otro | Detiene la búsqueda |

`prueba.sh` tiene una sola línea que importa:

```bash
[ "$(bash calc.sh 2 3)" = "5" ]
```

Si la suma da `5`, sale con 0 (bien); si no, con 1 (mal). La documentación de Git recomienda dejar el script **fuera
del repositorio**: así ningún salto entre commits lo borra ni lo cambia. Por eso `practica.sh` lo pone en la carpeta de
arriba y el comando dice `../prueba.sh`.

## Avisos

- **Si un commit no se puede probar** (no compila, falta un archivo), sáltalo a mano con `git bisect skip`, o haz que
  tu script salga con `125`.
- **Para ver lo que llevas respondido:**

  ```bash
  git bisect log
  ```

- **`good` y `bad` no tienen que ser «error»:** si buscas cuándo **cambió** algo (no cuándo se rompió), Git acepta
  `old` y `new` en su lugar.
- **El paginador:** algunos comandos de Git abren un visor cuando la salida no cabe. Muévete con las flechas y sal con
  la tecla `q`.
- El autor del repositorio de práctica («Práctica») es de práctica. En un proyecto real, el commit que encuentres trae
  el nombre de quien lo hizo: úsalo para entender el error, no para buscar culpables.

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica. Descarga [`practica.sh`](practica.sh) en esa
carpeta y córrelo:

```bash
bash practica.sh
cd practica-bisect
```

Comprueba que la suma está rota (da `-1`):

```bash
bash calc.sh 2 3
```

A mano: empieza, marca el malo y el bueno, y prueba el commit al que salta Git:

```bash
git bisect start
git bisect bad
git bisect good v1.0
bash calc.sh 2 3
```

Si dio `5`, responde `git bisect good`; si dio `-1`, `git bisect bad`. Repite hasta que Git diga cuál es el primer
commit malo. O deja que lo haga solo desde donde vayas:

```bash
git bisect run bash ../prueba.sh
```

Mira el cambio que rompió la suma y cierra la búsqueda:

```bash
git show 54644c9
git bisect reset
```

Con `practica.sh`, el hash del primer commit malo es el mismo que en el video. En tu propio proyecto, usa el hash que
te dé `git bisect` y, en lugar de `v1.0`, el hash o la etiqueta de una versión que sepas que funcionaba.

Fuentes: documentación oficial de Git (`git-bisect`, https://git-scm.com/docs/git-bisect, versión 2.56.0; y
`git-show`, https://git-scm.com/docs/git-show) y el libro Pro Git («Debugging with Git»,
https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git), consultadas el 25 de noviembre de 2026.
