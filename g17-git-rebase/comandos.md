# Rebase o merge · los comandos del video

| Comando | Qué hace |
|---|---|
| `git log --oneline --graph --all` | Dibuja la historia de **todas** tus ramas, un commit por línea con su hash corto |
| `git switch -c con-merge` | Crea la rama de práctica `con-merge` desde donde estás y cambia a ella |
| `git merge --no-edit main` | Une `main` a tu rama con un commit de fusión y acepta el mensaje automático («Merge branch 'main' into con-merge») |
| `git log --oneline --graph` | Dibuja la historia de la rama en la que estás |
| `git switch -c con-rebase nueva-portada` | Crea otra rama de práctica, `con-rebase`, desde `nueva-portada` (no desde donde estás) y cambia a ella |
| `git rebase main` | Vuelve a aplicar los commits de tu rama encima de `main`: la historia queda en línea recta |

## Cómo leer el dibujo de `--graph`

- Cada `*` es un commit. Entre paréntesis salen las ramas que apuntan a él y `HEAD`, la rama en la que estás.
- Con merge, el dibujo se abre (`|\`) y se cierra (`|/`): dos caminos que se juntan en el commit de fusión.
- Con rebase, todos los `*` quedan en una sola columna.
- Compara el hash de «Nueva portada» antes y después del rebase: es otro. Rebase no mueve tu commit, crea uno nuevo
  con el mismo cambio.

## Cuándo usar cada uno

- **Rebase:** para ordenar tus commits locales antes de subirlos (por ejemplo, ponerte al día con `main` antes de abrir
  tu pull request).
- **Merge:** para unir lo que ya subiste o lo que otros ya usan.
- **Nunca** hagas rebase de commits que ya subiste y en los que otros pudieron basar su trabajo: tendrían que arreglar
  su historia a mano.

## Avisos

- **Sin `--no-edit`, `git merge` abre el editor** para que escribas o revises el mensaje del commit de fusión. Si se
  abre, guarda y cierra el editor para terminar.

- **Si el rebase choca con un conflicto**, Git se detiene en el primer commit con problemas y deja las marcas de
  conflicto (como en el video de conflictos, [`../g8-conflictos-merge/`](../g8-conflictos-merge/)). Resuélvelo, marca
  el archivo como resuelto y sigue:

  ```bash
  git add index.html
  git rebase --continue
  ```

  O, para volver tu rama a como estaba antes del rebase:

  ```bash
  git rebase --abort
  ```

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica. Opción rápida: descarga
[`practica.sh`](practica.sh) en esa carpeta y córrelo:

```bash
bash practica.sh
cd practica-rebase
```

O arma el repositorio a mano (es lo mismo que hace el script):

```bash
mkdir practica-rebase
cd practica-rebase
git init -b main
echo "<h1>Hola</h1>" > index.html
git add index.html
git commit -m "Primera versión"
git switch -c nueva-portada
echo "<h1>Bienvenidos</h1>" > index.html
git commit -am "Nueva portada"
git switch main
echo "<p>Contacto</p>" > contacto.html
git add contacto.html
git commit -m "Agrega contacto"
git switch nueva-portada
```

Mira cómo se separaron las dos ramas:

```bash
git log --oneline --graph --all
```

Une con merge, en una rama de práctica:

```bash
git switch -c con-merge
git merge --no-edit main
git log --oneline --graph
```

Une con rebase, en otra rama de práctica:

```bash
git switch -c con-rebase nueva-portada
git rebase main
git log --oneline --graph
```

Comprueba que las dos dejan los mismos archivos (no imprime nada):

```bash
git diff con-merge con-rebase
```

Y que `nueva-portada` sigue con su hash original:

```bash
git log --oneline --graph --all
```

Si `git log` no muestra los nombres de las ramas entre paréntesis, agrega `--decorate` (el script ya lo deja
configurado solo en el repositorio de práctica). Si Git te pide tu nombre y correo antes del primer commit,
configúralos una vez (como en el video de Git y GitHub):

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@correo.com"
```

Fuentes: documentación oficial de Git (`git-rebase`, `git-merge`, `git-log` y `git-switch`, en
https://git-scm.com/docs) y el libro Pro Git («Rebasing», https://git-scm.com/book/en/v2/Git-Branching-Rebasing, y
«Basic Branching and Merging», https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), consultadas
el 22 de noviembre de 2026.
