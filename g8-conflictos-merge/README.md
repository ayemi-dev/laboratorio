# El conflicto, resuelto: de los marcadores al pull request unido

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y segunda parte de [ramas y pull requests](../g3-ramas-pull-request/). En aquel video Git marcó un conflicto y lo dejamos en «tú decides». Aquí se decide: provocamos un conflicto real entre dos ramas, leemos las marcas, lo resolvemos en VS Code, terminamos el merge y unimos el pull request.

- **Conflicto**: dos ramas cambiaron la misma línea del mismo archivo y Git no puede elegir solo cuál se queda.
- **Mientras exista**, GitHub desactiva el botón **Merge pull request** del pull request.
- **Para resolverlo**: eliges qué se queda, quitas las marcas, `git add`, `git commit` y `git push`.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch main` | Cambia a la rama `main` |
| `cat index.html` | Muestra el archivo: en `main` el título dice `Hola, mundo` |
| `git switch nueva-portada` | Vuelve a la rama del pull request |
| `cat index.html` | La misma línea, en esta rama, dice `Bienvenidos` |
| `git merge main` | Trae a tu rama lo nuevo de `main`; si chocan, Git se detiene y marca el conflicto |
| `git add index.html` | Marca el archivo como resuelto |
| `git commit -m "Resuelve el conflicto"` | Termina el merge |
| `git push` | Sube la solución a tu rama en GitHub; el pull request ya se puede unir |

La guía completa, con cómo preparar la práctica, cómo leer las marcas, los botones de VS Code, cómo cancelar y los pasos en GitHub, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Descargar Git | https://git-scm.com/downloads |
| `git merge` (incluye cómo se presentan y se resuelven los conflictos) | https://git-scm.com/docs/git-merge |
| Libro Pro Git: conflictos básicos | https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging |
| Conflictos en VS Code | https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts |
| About merge conflicts (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts |
| Resolving a merge conflict using the command line (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line |
| Merging a pull request (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request |
| Video anterior: ramas y pull requests | [`../g3-ramas-pull-request/`](../g3-ramas-pull-request/) |

Datos verificados el 20 de noviembre de 2026 en la documentación oficial de Git, GitHub y Visual Studio Code. Ayemi no tiene relación con GitHub ni con Microsoft.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
