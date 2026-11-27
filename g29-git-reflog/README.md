# Git: recupera una rama que borraste

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Deshacer sin miedo en Git](../g7-git-deshacer/) y [Git: encuentra el commit que rompió todo](../g27-git-bisect/). Ahí
deshiciste commits y cazaste el que rompió algo; aquí recuperas una rama entera que borraste con `git branch -D`.

## La idea: Git anota por dónde pasó HEAD

Cada vez que haces un commit o cambias de rama, Git lo anota en el **reflog** de tu repositorio. Si borras una rama, sus
commits siguen ahí un tiempo, y el reflog te da su hash. Con ese hash creas la rama de nuevo.

| Paso | Comando | Qué hace |
|---|---|---|
| Ver tus ramas | `git branch` | Lista las ramas; la tuya lleva `*` |
| Borrar (el accidente) | `git branch -D tema-oscuro` | Borra la rama aunque sus commits no estén unidos a otra |
| Buscar el commit | `git reflog` | Cada lugar por el que pasó HEAD, del más nuevo al más viejo |
| Recuperar | `git branch tema-oscuro HASH` | Crea la rama de nuevo, apuntando a ese commit |
| Comprobar | `git log --oneline -3 tema-oscuro` | Los tres commits de la rama, de vuelta |

En el video, todo se hace en un **repositorio de práctica**: tres commits en `main` y la rama `tema-oscuro` con tres
más que no están en `main`. [`practica.sh`](practica.sh) lo arma en un paso, con fechas fijas (los hashes te salen
iguales que en el video).

## Archivos

| Archivo | Para qué |
|---|---|
| [`practica.sh`](practica.sh) | Arma el repositorio del video (`practica-reflog/`) con la rama `tema-oscuro` |
| [`comandos.md`](comandos.md) | Cada comando del video, cómo leer el reflog, los avisos y la práctica de cinco minutos |

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `git reflog` | https://git-scm.com/docs/git-reflog |
| `git branch` | https://git-scm.com/docs/git-branch |
| Pro Git: «Maintenance and Data Recovery» (recuperar datos) | https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery |
| Videos anteriores de esta parte | [`../g7-git-deshacer/`](../g7-git-deshacer/) y [`../g27-git-bisect/`](../g27-git-bisect/) |

Datos verificados el 27 de noviembre de 2026 en la documentación oficial de Git (git-scm.com, `git-reflog` 2.51.1 y
`git-branch` 2.56.0) y en el libro Pro Git. Ayemi no tiene relación con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
