# Git: quién cambió esta línea y por qué

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Deshacer sin miedo en Git](../g7-git-deshacer/). Ahí deshiciste un error; aquí averiguas quién cambió una línea,
cuándo y por qué, sin salir de la terminal.

## La idea: la historia de Git responde quién, cuándo y por qué

| Pregunta | Comando | Qué te da |
|---|---|---|
| ¿Qué pasó en este repositorio? | `git log -p --oneline` | Cada commit con su cambio (su «parche»). Todo está ahí, pero es largo |
| ¿Quién cambió **esta** línea? | `git blame --date=short index.html` | En cada línea, el commit que la cambió por última vez, su autor y su fecha |
| ¿Por qué la cambió? | `git show` y el hash que te dio `git blame` | El commit completo: autor, fecha, **mensaje** (el porqué) y el cambio |
| ¿Y si esa línea ya no existe? | `git log -S Hola --oneline` | Los commits donde el texto apareció o desapareció |

**Por eso importa el mensaje del commit:** `git blame` te dice quién y cuándo, pero el porqué solo está si alguien lo
escribió en el mensaje.

En el video, todo se hace en un **repositorio de práctica** con tres commits de dos autores de práctica («Textos» y
«Diseño»). [`practica.sh`](practica.sh) lo arma en un paso, con fechas fijas: los hashes te salen iguales que en el
video.

## Archivos

| Archivo | Para qué |
|---|---|
| [`practica.sh`](practica.sh) | Arma en un paso el repositorio del video, con su historia ya preparada |
| [`comandos.md`](comandos.md) | Cada comando del video, cómo leer su salida, los avisos y la práctica de cinco minutos |

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `git blame` | https://git-scm.com/docs/git-blame |
| `git log` | https://git-scm.com/docs/git-log |
| `git show` | https://git-scm.com/docs/git-show |
| Pro Git: «Debugging with Git» (`git blame`) | https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git |
| Pro Git: «Viewing the Commit History» (`-p` y `-S`) | https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History |
| Video anterior de esta parte: Deshacer sin miedo en Git | [`../g7-git-deshacer/`](../g7-git-deshacer/) |

Datos verificados el 22 de noviembre de 2026 en la documentación oficial de Git (git-scm.com) y en el libro Pro Git.
Ayemi no tiene relación con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
