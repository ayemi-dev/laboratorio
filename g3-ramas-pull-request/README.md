# Ramas, merge y pull requests: prueba ideas sin romper tu proyecto

Tercer video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Si ya usas Git para guardar versiones en `main`, las ramas te dejan probar ideas sin romper lo que ya funciona.

- **Rama (`branch`)**: una línea de trabajo aparte; mientras pruebas, `main` no cambia.
- **`git merge`**: junta los cambios de una rama en tu computadora.
- **Pull request**: en equipo, una propuesta en GitHub para revisar y comentar los cambios antes de juntarlos.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch -c nueva-portada` | Crea la rama `nueva-portada` y te pasa a ella |
| `git branch` | Lista las ramas y marca la actual con un asterisco (`*`) |
| `git add .` | Prepara los cambios para el siguiente commit |
| `git commit -m "Nueva portada"` | Guarda el commit en la rama en la que estás |
| `git switch main` | Cambia a la rama `main` |
| `git merge nueva-portada` | Junta los cambios de `nueva-portada` en la rama actual (`main`) |
| `git merge otro-titulo` | Intenta juntar `otro-titulo`; si ambas ramas cambiaron la misma línea, marca el conflicto |
| `cat index.html` | Muestra el archivo con las marcas del conflicto (`<<<<<<<`, `=======`, `>>>>>>>`) |
| `git push -u origin nueva-portada` | Sube la rama al remoto y la deja enlazada para futuros `git pull` / `git push` |
| `git pull` | Trae a tu computadora los cambios del remoto y los integra en la rama actual |

La guía completa con cómo resolver conflictos y los pasos del pull request está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Descargar Git | https://git-scm.com/downloads |
| `git switch` | https://git-scm.com/docs/git-switch |
| `git branch` | https://git-scm.com/docs/git-branch |
| `git merge` | https://git-scm.com/docs/git-merge |
| `git push` | https://git-scm.com/docs/git-push |
| `git pull` | https://git-scm.com/docs/git-pull |
| Libro Pro Git en español (Ramas) | https://git-scm.com/book/es/v2 |
| About pull requests (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests |
| Creating a pull request (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request |
| Merging a pull request (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request |
| About merge conflicts (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts |
| Video anterior: Git y GitHub | [`../g2-git-github/`](../g2-git-github/) |

Datos verificados el 15 de noviembre de 2026 en la documentación oficial de Git y de GitHub. Ayemi no tiene relación con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
