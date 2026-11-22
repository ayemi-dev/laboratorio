# Git nivel 5: rebase o merge, cuándo usar cada uno

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Ramas y pull request](../g3-ramas-pull-request/) y de [El conflicto, resuelto](../g8-conflictos-merge/).

## El caso

Tu rama `nueva-portada` y `main` se separaron: cada una tiene un commit que la otra no. Hay dos formas de unirlas, y
las dos dejan los mismos archivos. Lo que cambia es la historia:

| | `git merge main` | `git rebase main` |
|---|---|---|
| Qué hace | Une las dos ramas con un **commit de fusión** (un commit con dos padres) | **Vuelve a aplicar** tus commits encima de `main` |
| Cómo queda la historia | Con la bifurcación, tal como pasó | En línea recta |
| Tus commits | Se quedan igual, con el mismo hash | Se crean de nuevo, con **otro hash** |
| Cuándo | Para unir lo que ya subiste o lo que otros ya usan | Para ordenar tus commits locales **antes** de subirlos |

**La regla (Pro Git):** no hagas rebase de commits que ya existen fuera de tu repositorio y en los que otros pudieron
basar su trabajo. Como rebase crea commits nuevos, quien ya tenía los viejos tendría que arreglar su historia a mano.

En el video, el merge y el rebase se hacen en dos **ramas de práctica** (`con-merge` y `con-rebase`), creadas desde
`nueva-portada`, para comparar las dos historias sin tocar la rama de trabajo.

## Archivos

| Archivo | Para qué |
|---|---|
| [`practica.sh`](practica.sh) | Arma en un paso el repositorio del video, con `main` y `nueva-portada` ya separadas |
| [`comandos.md`](comandos.md) | Cada comando del video, los avisos (conflictos durante el rebase, el editor del merge) y la práctica de cinco minutos |

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Pro Git: «Rebasing» | https://git-scm.com/book/en/v2/Git-Branching-Rebasing |
| Pro Git: «Basic Branching and Merging» | https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging |
| `git rebase` | https://git-scm.com/docs/git-rebase |
| `git merge` | https://git-scm.com/docs/git-merge |
| `git log` | https://git-scm.com/docs/git-log |
| `git switch` | https://git-scm.com/docs/git-switch |
| Video anterior de esta parte: El conflicto, resuelto | [`../g8-conflictos-merge/`](../g8-conflictos-merge/) |

Datos verificados el 22 de noviembre de 2026 en la documentación oficial de Git (git-scm.com) y en el libro Pro Git.
Ayemi no tiene relación con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
