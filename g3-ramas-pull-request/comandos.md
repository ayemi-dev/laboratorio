# Ramas, merge y pull requests · los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch -c nueva-portada` | Crea la rama `nueva-portada` y te pasa a ella (disponible desde Git 2.23) |
| `git branch` | Lista las ramas locales y marca la actual con un asterisco (`*`) |
| `git add .` | Prepara los cambios para el siguiente commit |
| `git commit -m "Nueva portada"` | Guarda el commit en la rama actual |
| `git switch main` | Cambia a la rama `main` |
| `git merge nueva-portada` | Junta los cambios de `nueva-portada` en `main` (si `main` no avanzó, hace *Fast-forward*) |
| `git merge otro-titulo` | Junta `otro-titulo`; si ambas ramas cambiaron la misma línea, Git detiene el merge y marca el conflicto |
| `cat index.html` | Muestra el contenido del archivo (en Git Bash, PowerShell, macOS y Linux; en `cmd` usa `type index.html`) |
| `git push -u origin nueva-portada` | Sube la rama `nueva-portada` a `origin` y la deja enlazada (*upstream*) |
| `git switch main` | Vuelve a `main` |
| `git pull` | Descarga e integra los cambios del remoto en la rama actual |

## Cómo se ve un conflicto y cómo se resuelve

Cuando dos ramas modifican de forma distinta la misma línea de un archivo, Git no elige por ti. Muestra:

```text
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Dentro del archivo verás las tres marcas del conflicto:

```html
<<<<<<< HEAD
<h1>Hola, mundo</h1>
=======
<h1>Bienvenidos</h1>
>>>>>>> otro-titulo
```

- Lo que está entre `<<<<<<< HEAD` y `=======` es lo que tienes en tu rama actual (`main`).
- Lo que está entre `=======` y `>>>>>>> otro-titulo` es lo que viene de la rama que estás juntando.

**Para resolverlo:**

1. Abre `index.html`, decide qué versión se queda (o combínalas) y **borra** las líneas `<<<<<<<`, `=======` y `>>>>>>>`.
2. Prepara el archivo corregido y guarda el commit:

```bash
git add index.html
git commit -m "Resuelve conflicto en el título"
```

(Si prefieres cancelar el merge y volver a como estaba antes, usa `git merge --abort`.)

## Pasos del pull request en GitHub

1. Sube tu rama con `git push -u origin nueva-portada`.
2. En tu repositorio en GitHub, haz clic en **Compare & pull request**.
3. Revisa en el menú desplegable de rama base (*base branch*) que vaya hacia `main`, escribe título y descripción, y haz clic en **Create Pull Request**.
4. Cuando el equipo haya revisado los cambios y esté listo, haz clic en **Merge pull request**.
5. En tu computadora, vuelve a `main` y descarga el cambio integrado:

```bash
git switch main
git pull
```

Fuentes: documentación oficial de Git (`git-switch`, `git-branch`, `git-merge`, `git-push`, `git-pull`, en https://git-scm.com/docs), libro Pro Git en español (https://git-scm.com/book/es/v2) y GitHub Docs (*About pull requests*, *Creating a pull request*, *Merging a pull request*, *About merge conflicts*), consultadas el 15 de noviembre de 2026.
