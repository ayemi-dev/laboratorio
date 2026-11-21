# El conflicto, resuelto · los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch main` | Cambia a la rama `main` |
| `cat index.html` | Muestra el contenido del archivo (en Git Bash, PowerShell, macOS y Linux; en `cmd` usa `type index.html`) |
| `git switch nueva-portada` | Vuelve a la rama del pull request; tus archivos quedan como en esa rama |
| `cat index.html` | Muestra la versión del archivo en `nueva-portada` |
| `git merge main` | Trae a la rama actual los cambios de `main`; si las dos cambiaron la misma línea, se detiene y marca el conflicto |
| `git add index.html` | Marca el archivo como resuelto |
| `git commit -m "Resuelve el conflicto"` | Guarda la resolución y termina el merge |
| `git push` | Sube la rama actual a su rama enlazada en GitHub (la que dejaste con `git push -u origin nueva-portada`) |

## 1. Prepara la práctica (o sigue desde el video de ramas)

Si vienes de [ramas y pull requests](../g3-ramas-pull-request/), ya tienes la carpeta `mi-pagina`, la rama `nueva-portada` subida con `git push -u origin nueva-portada` y su pull request abierto hacia `main`. Para provocar el conflicto a propósito, cambia **la misma línea** de `index.html` en las dos ramas y guarda un commit en cada una:

```bash
git switch nueva-portada
```

Edita `index.html` para que diga `<h1>Bienvenidos</h1>` y guarda:

```bash
git add index.html
git commit -m "Nueva portada"
git push
git switch main
```

Edita la misma línea para que diga `<h1>Hola, mundo</h1>` y guarda:

```bash
git add index.html
git commit -m "Otro título"
git push
```

Ahora el pull request de `nueva-portada` choca con `main`, y GitHub desactiva el botón **Merge pull request** hasta que lo resuelvas.

## 2. Provoca el conflicto en tu computadora

```bash
git switch nueva-portada
git merge main
```

Git se detiene con algo así:

```text
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

¿No sabes qué archivos quedaron sin unir? `git status` los lista como *unmerged* (en formato corto, `git status -s`, aparecen con `UU`).

## 3. Lee las marcas

Dentro de `index.html` verás:

```html
<<<<<<< HEAD
<h1>Bienvenidos</h1>
=======
<h1>Hola, mundo</h1>
>>>>>>> main
```

- Entre `<<<<<<< HEAD` y `=======` está **tu rama**, la que tenías abierta al hacer el merge (`nueva-portada`). VS Code lo llama *Current Change* (cambio actual).
- Entre `=======` y `>>>>>>> main` está **lo que llega** de la rama que estás uniendo (`main`). VS Code lo llama *Incoming Change* (cambio entrante).

## 4. Resuélvelo en VS Code

Abre la carpeta en VS Code (desde la terminal, `code .` dentro de `mi-pagina`). Encima del conflicto aparecen cuatro botones:

| Botón | Qué hace |
|---|---|
| **Accept Current Change** | Se queda solo con tu rama (en el video: `<h1>Bienvenidos</h1>`) |
| **Accept Incoming Change** | Se queda solo con lo que llega de `main` |
| **Accept Both Changes** | Deja las dos versiones, una después de la otra; revisa que no queden líneas repetidas |
| **Compare Changes** | Abre una vista para comparar las dos versiones |

También puedes editarlo a mano: deja el texto que quieras y **borra** las líneas `<<<<<<<`, `=======` y `>>>>>>>`. Para conflictos más grandes, VS Code tiene el editor de tres vías (**Resolve in Merge Editor** y, al final, **Complete Merge**).

Guarda el archivo.

## 5. Termina el merge y súbelo

```bash
git add index.html
git commit -m "Resuelve el conflicto"
git push
```

Si prefieres no salir de VS Code: en la vista de control de código fuente, prepara el archivo con **+** (pasa de *Merge Changes* a *Staged Changes*), escribe el mensaje y presiona **Commit**.

## 6. Une el pull request en GitHub

1. Abre el pull request: el botón **Merge pull request** ya está activo.
2. Haz clic en **Merge pull request** y luego en **Confirm merge**.
3. Opcional: borra la rama para mantener ordenada la lista de ramas.

Conflictos sencillos de una línea también se pueden resolver en la web de GitHub con el botón **Resolve conflicts** del pull request; para lo demás, la línea de comandos.

## ¿Te arrepentiste a medio merge?

```bash
git merge --abort
```

Cancela la resolución y vuelve a como estaba antes del merge (en VS Code: **Git: Abort Merge**). Por eso conviene hacer commit de tus cambios antes de correr `git merge`.

Fuentes: documentación oficial de Git (`git-switch`, `git-merge`, `git-status`, `git-push`, en https://git-scm.com/docs), libro Pro Git (https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), Visual Studio Code (https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts) y GitHub Docs (*About merge conflicts*, *Resolving a merge conflict using the command line*, *Resolving a merge conflict on GitHub*, *Merging a pull request*), consultadas el 20 de noviembre de 2026.
