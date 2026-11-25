# Git: encuentra el commit que rompió todo

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Git: quién cambió esta línea y por qué](../g22-git-log-blame/). Ahí rastreaste una línea; aquí encuentras qué commit
rompió algo que funcionaba, aunque haya veinte (o mil) en medio.

## La idea: partir la historia a la mitad hasta dar con el commit

`git bisect` hace una búsqueda binaria en la historia: tú le dices un commit malo (el de hoy) y uno bueno (una
versión que funcionaba); Git salta a uno de en medio, lo pruebas y le respondes. Cada respuesta descarta la mitad.

| Paso | Comando | Qué hace |
|---|---|---|
| Empezar | `git bisect start` | Abre la búsqueda |
| Marcar el malo | `git bisect bad` | El commit donde estás (hoy) está mal |
| Marcar el bueno | `git bisect good v1.0` | Esa versión funcionaba; Git salta a un commit de en medio |
| Responder | `git bisect good` o `git bisect bad` | Tras probar el commit de en medio; Git salta al siguiente |
| Que lo haga solo | `git bisect run bash ../prueba.sh` | Corre la prueba en cada salto hasta el primer commit malo |
| Terminar | `git bisect reset` | Te regresa a donde estabas antes de empezar |

En el video, todo se hace en un **repositorio de práctica** de veinte commits sobre `calc.sh`, una suma de dos números.
Uno de esos commits la convierte en resta. [`practica.sh`](practica.sh) lo arma en un paso, con fechas fijas (los
hashes te salen iguales que en el video), y deja junto a él `prueba.sh`, la prueba que usa `git bisect run`.

## Archivos

| Archivo | Para qué |
|---|---|
| [`practica.sh`](practica.sh) | Arma el repositorio del video (`practica-bisect/`) y su prueba (`prueba.sh`, fuera del repositorio) |
| [`comandos.md`](comandos.md) | Cada comando del video, cómo leer el resultado, los avisos y la práctica de cinco minutos |

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `git bisect` | https://git-scm.com/docs/git-bisect |
| Pro Git: «Debugging with Git» (búsqueda binaria) | https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git |
| `git show` | https://git-scm.com/docs/git-show |
| Video anterior de esta parte: Git, quién cambió esta línea y por qué | [`../g22-git-log-blame/`](../g22-git-log-blame/) |

Datos verificados el 25 de noviembre de 2026 en la documentación oficial de Git (git-scm.com, `git-bisect` 2.56.0) y en
el libro Pro Git. Ayemi no tiene relación con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
