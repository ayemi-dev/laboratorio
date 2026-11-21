# Deshacer en Git · los comandos del video

| Comando | Qué hace |
|---|---|
| `git log --oneline` | Muestra la lista de commits, uno por línea. `origin/main` marca hasta dónde ya subiste |
| `git diff` | Muestra lo que cambiaste en tus archivos y todavía no preparas con `git add` |
| `git restore index.html` | Regresa `index.html` a su última versión guardada (lo último que preparaste o, si no preparaste nada, tu último commit). **Los cambios que tenía se pierden** |
| `git status` | Te dice en qué estado está tu carpeta (después de `git restore`: «nothing to commit, working tree clean») |
| `git revert --no-edit HEAD` | Crea un commit **nuevo** que deshace el último commit (`HEAD`). Con `--no-edit` no se abre el editor del mensaje |
| `git push` | Sube ese commit nuevo a GitHub |
| `git reset HEAD~1` | Quita el último commit de tu rama (`HEAD~1` es el commit anterior). Tus cambios siguen en el archivo, sin preparar |
| `git status --short` | El estado en una línea por archivo (` M index.html`: modificado, sin preparar) |

## ¿Cuál uso?

1. **¿El cambio no está en ningún commit?** Mira la diferencia con `git diff`. Si no la quieres:

   ```bash
   git restore index.html
   ```

   Si ya lo habías preparado con `git add`, primero sácalo del área de preparación y luego restáuralo:

   ```bash
   git restore --staged index.html
   git restore index.html
   ```

2. **¿El commit ya está en GitHub (ya hiciste `git push`)?** Deshazlo con un commit nuevo y súbelo:

   ```bash
   git revert --no-edit HEAD
   git push
   ```

   `git revert` pide la carpeta limpia: si tienes cambios sin commit, guárdalos en un commit o descártalos antes.
   Para deshacer un commit que no es el último, copia su identificador de `git log --oneline` y úsalo en lugar de `HEAD`.

3. **¿El commit solo está en tu computadora (no has hecho `git push`)?**

   ```bash
   git reset HEAD~1
   ```

   El commit desaparece de tu historia y sus cambios se quedan en el archivo para que los corrijas y hagas otro commit.

## Avisos

- **No uses `git reset` con commits que ya subiste.** El manual de Git lo dice así: si el error ya es público, crea un
  commit nuevo que lo deshaga; cambiar una historia que ya compartiste causa problemas a quien la descargó.
- **`git reset --hard` no aparece en el video a propósito:** borra los cambios de tus archivos y es uno de los pocos
  casos en que Git destruye datos.
- **`git restore` descarta de verdad** lo que cambiaste en ese archivo. Úsalo solo si no lo quieres.
- `HEAD~1` quiere decir «un commit antes de `HEAD`» (`HEAD~2`, dos antes). Para no equivocarte, quita uno a la vez y
  revisa con `git log --oneline`.

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica:

```bash
mkdir practica-deshacer
cd practica-deshacer
git init
echo "<h1>Hola</h1>" > index.html
git add .
git commit -m "Primera versión"
```

Caso 1, archivo sin commit:

```bash
echo "<h1>Hla</h1>" > index.html
git diff
git restore index.html
git status
```

Caso 2, deshacer con un commit nuevo (en un repositorio con GitHub, después irían `git push`):

```bash
echo "<h1>Hla</h1>" > index.html
git commit -am "Título roto"
git revert --no-edit HEAD
git log --oneline
```

Caso 3, quitar un commit local:

```bash
echo "<p>Borrador</p>" >> index.html
git commit -am "Borrador"
git reset HEAD~1
git log --oneline
git status --short
```

Si Git te pide tu nombre y correo antes del primer commit, configúralos una vez (como en el video de Git y GitHub):

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@correo.com"
```

Fuentes: documentación oficial de Git (`git-restore`, `git-revert`, `git-reset`, `git-diff`, `git-status`, `git-push`,
`git-log`, `gitrevisions` y el manual de usuario, sección «Fixing mistakes», en https://git-scm.com/docs) y el libro
Pro Git («Undoing Things» y «Reset Demystified», https://git-scm.com/book/en/v2), consultadas el 20 de noviembre de 2026.
