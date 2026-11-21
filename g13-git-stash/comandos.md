# git stash · los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch main` | Cambia a la rama `main`. Si tienes cambios sin commit en un archivo que es distinto en las dos ramas, Git se niega para no perderlos |
| `git stash push -m "portada a medias"` | Guarda tus cambios con el nombre «portada a medias» y deja tu carpeta como en tu último commit |
| `git status` | Te dice en qué estado está tu carpeta (después de guardar: «nothing to commit, working tree clean») |
| `git stash list` | Muestra lo que tienes guardado, del más reciente (`stash@{0}`) al más antiguo (`stash@{1}`, `stash@{2}`…), con la rama y el nombre |
| `git commit -am "Arreglo urgente"` | Guarda en un commit los archivos que Git ya sigue y que cambiaste (los archivos nuevos no entran) |
| `git switch nueva-portada` | Regresa a tu rama |
| `git stash pop` | Aplica lo último que guardaste y lo quita de la lista |
| `cat index.html` | Muestra el contenido del archivo: tu trabajo a medias está de vuelta |

## Sin nombre o con nombre

```bash
git stash
```

Es lo mismo que `git stash push`. En la lista sale como «WIP on» y el nombre de la rama. Con nombre es más fácil saber
qué es cada cosa cuando guardas más de una:

```bash
git stash push -m "portada a medias"
```

## Avisos

- **Los archivos nuevos no se guardan solos.** `git stash` guarda los archivos que Git ya sigue (modificados o
  preparados con `git add`). Si creaste un archivo nuevo y todavía no le hiciste `git add`, agrégale `-u`:

  ```bash
  git stash push -u -m "con el archivo nuevo"
  ```

- **Si `git stash pop` choca con conflictos, lo guardado no se borra de la lista.** Resuelve el conflicto (como en el
  video de conflictos, [`../g8-conflictos-merge/`](../g8-conflictos-merge/)) y luego bórralo a mano:

  ```bash
  git stash drop
  ```

- **Para aplicar sin borrar de la lista**, usa `apply` en lugar de `pop`:

  ```bash
  git stash apply
  ```

- **Para recuperar uno que no es el último**, nómbralo como sale en `git stash list`:

  ```bash
  git stash pop stash@{1}
  ```

  (Sin nombre, `pop` y `apply` usan siempre el más reciente, `stash@{0}`.)

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica:

```bash
mkdir practica-stash
cd practica-stash
git init -b main
echo "<h1>Hola</h1>" > index.html
git add .
git commit -m "Primera versión"
git switch -c nueva-portada
echo "<h1>Bienvenidos</h1>" > index.html
git commit -am "Nueva portada"
```

Tu trabajo a medias, y Git que no te deja cambiar de rama:

```bash
echo "<p>Contacto</p>" >> index.html
git switch main
```

Guarda, revisa y cambia:

```bash
git stash push -m "portada a medias"
git status
git stash list
git switch main
```

El arreglo urgente en `main`:

```bash
echo "<p>Abierto hoy</p>" >> index.html
git commit -am "Arreglo urgente"
```

Regresa y recupera tu trabajo:

```bash
git switch nueva-portada
git stash pop
cat index.html
git stash list
```

`cat index.html` muestra `<h1>Bienvenidos</h1>` y `<p>Contacto</p>`, y `git stash list` ya no muestra nada.

Si Git te pide tu nombre y correo antes del primer commit, configúralos una vez (como en el video de Git y GitHub):

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@correo.com"
```

Fuentes: documentación oficial de Git (`git-stash`, `git-switch`, `git-commit` y `git-status`, en
https://git-scm.com/docs) y el libro Pro Git («Stashing and Cleaning»,
https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning), consultadas el 21 de noviembre de 2026.
