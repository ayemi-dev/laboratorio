# Quién cambió esta línea y por qué · los comandos del video

| Comando | Qué hace |
|---|---|
| `git log -p --oneline` | Muestra cada commit en una línea (hash corto y mensaje) y, debajo, su cambio |
| `git blame --date=short index.html` | Anota cada línea de `index.html` con el commit que la cambió por última vez, su autor y su fecha (solo el día) |
| `git show 803488e2` | Abre ese commit: autor, fecha, mensaje completo y el cambio |
| `git log -S Hola --oneline` | Busca los commits que cambiaron cuántas veces aparece el texto `Hola`: donde apareció y donde desapareció |

## Cómo leer la salida de `git blame`

Cada renglón es una línea del archivo:

- Al principio, el **hash** del commit que cambió esa línea por última vez. Con ese hash, `git show` te enseña el
  commit completo.
- Entre paréntesis, el **autor**, la **fecha** y el **número de línea**.
- Después, la línea tal como está hoy.
- Si el hash empieza con `^`, esa línea llegó en el **primer** commit del repositorio y no ha cambiado desde
  entonces (en el repositorio de práctica, «Primera versión»).

`git blame` te dice quién cambió la línea al último y cuándo. **El porqué está en el mensaje del commit**: por eso
vale la pena escribir mensajes que expliquen la razón, no solo «cambios».

## Cómo leer la salida de `git log -S`

`-S` no busca líneas que **contienen** el texto: busca commits que **cambiaron cuántas veces** aparece. Por eso, en
el repositorio de práctica, `git log -S Hola --oneline` da dos commits («Cambia el título», donde `Hola` desapareció,
y «Primera versión», donde apareció) y no «Agrega el horario», que no tocó el título. Sirve para encontrar algo que
**ya no está** en el archivo, donde `git blame` ya no puede ayudarte.

Si el texto tiene espacios, va entre comillas:

```bash
git log -S "Horario: 9 a 18" --oneline
```

## Avisos

- **`git log`, `git blame` y `git show` abren un paginador** cuando la salida no cabe en la pantalla. Muévete con las
  flechas y sal con la tecla `q`.
- **`git blame` muestra el último cambio de cada línea**, no el primero: si alguien solo movió espacios o la cambió
  de lugar, aparece esa persona. Para ver la historia de un archivo completa, usa `git log -p` con su nombre:

  ```bash
  git log -p --oneline index.html
  ```

- **Para una sola línea**, `-L` limita `git blame` a ese tramo (aquí, solo la línea 1):

  ```bash
  git blame -L 1,1 index.html
  ```

- Los autores del repositorio de práctica («Textos» y «Diseño») son de práctica. En un proyecto real, `git blame`
  enseña los nombres y correos que cada persona configuró en Git: úsalo para entender el código, no para buscar
  culpables.

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica. Descarga [`practica.sh`](practica.sh) en esa
carpeta y córrelo:

```bash
bash practica.sh
cd practica-blame
```

Mira toda la historia, cada commit con su cambio:

```bash
git log -p --oneline
```

Pregunta quién cambió cada línea:

```bash
git blame --date=short index.html
```

Abre el commit de la primera línea (con `practica.sh`, el hash es el mismo que en el video):

```bash
git show 803488e2
```

Busca el texto que ya no está:

```bash
git log -S Hola --oneline
```

¿Prefieres armarlo a mano? Es lo mismo que hace el script, pero con tu nombre y la fecha de hoy (los hashes te saldrán
distintos a los del video):

```bash
mkdir practica-blame
cd practica-blame
git init -b main
printf '<h1>Hola</h1>\n<p>Contacto</p>\n' > index.html
git add index.html
git commit -m "Primera versión"
printf '<h1>Hola</h1>\n<p>Horario: 9 a 18</p>\n<p>Contacto</p>\n' > index.html
git commit -am "Agrega el horario"
printf '<h1>Bienvenidos</h1>\n<p>Horario: 9 a 18</p>\n<p>Contacto</p>\n' > index.html
git commit -am "Cambia el título" -m "Hola se veía informal en la portada."
```

Si Git te pide tu nombre y correo antes del primer commit, configúralos una vez (como en el video de Git y GitHub):

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@correo.com"
```

Fuentes: documentación oficial de Git (`git-blame`, `git-log` y `git-show`, en https://git-scm.com/docs) y el libro
Pro Git («Debugging with Git», https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git, y «Viewing the Commit
History», https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History), consultadas el 22 de noviembre de 2026.
