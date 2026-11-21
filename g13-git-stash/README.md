# git stash: guarda tu trabajo a medias sin hacer commit

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Ramas y pull request](../g3-ramas-pull-request/) y de [Deshacer sin miedo en Git](../g7-git-deshacer/).

## El caso

Estás en tu rama `nueva-portada` con cambios a medias. Te piden un arreglo urgente en `main`, pero Git no te deja
cambiar de rama: perderías tus cambios. No hace falta un commit a medias:

| Paso | Comando | Qué pasa |
|---|---|---|
| 1. Guardar | `git stash push -m "portada a medias"` | Guarda tus cambios con un nombre y deja la carpeta como en tu último commit |
| 2. Revisar | `git stash list` | Muestra lo guardado. El más reciente es `stash@{0}` |
| 3. Cambiar y arreglar | `git switch main` y `git commit -am "Arreglo urgente"` | Ahora sí cambias de rama y guardas el arreglo |
| 4. Regresar | `git switch nueva-portada` | Vuelves a tu rama |
| 5. Recuperar | `git stash pop` | Te regresa los cambios y los quita de la lista |

`git stash` solo hace lo mismo que `git stash push`, pero sin nombre.

La guía completa, con los avisos (archivos nuevos, conflictos al recuperar, `apply` y `drop`) y una práctica de cinco
minutos sin GitHub, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `git stash` | https://git-scm.com/docs/git-stash |
| `git switch` | https://git-scm.com/docs/git-switch |
| Pro Git: «Stashing and Cleaning» | https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning |
| Video anterior de esta parte: Ramas y pull request | [`../g3-ramas-pull-request/`](../g3-ramas-pull-request/) |

Datos verificados el 21 de noviembre de 2026 en la documentación oficial de Git (git-scm.com). Ayemi no tiene relación
con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
