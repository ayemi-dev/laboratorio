# Recupera una rama que borraste · los comandos del video

| Comando | Qué hace |
|---|---|
| `bash practica.sh` | Arma `practica-reflog/` con tres commits en `main` y la rama `tema-oscuro` con tres más |
| `git branch` | Lista las ramas: `main` (con `*`, es donde estás) y `tema-oscuro` |
| `git branch -D tema-oscuro` | Borra la rama aunque sus commits no estén unidos a `main` (`-D` es `--delete --force`) |
| `git reflog` | Muestra cada lugar por el que pasó HEAD, del más nuevo al más viejo |
| `git branch tema-oscuro 1bb01f2` | Crea `tema-oscuro` de nuevo, en el commit «Tema listo» |
| `git log --oneline -3 tema-oscuro` | Comprueba que volvieron sus tres commits |

## Cómo leer el reflog

Cada renglón de `git reflog` tiene tres partes:

- **El hash** del commit donde quedó HEAD.
- **`HEAD@{n}`**: hace cuántos movimientos estuvo ahí HEAD. `HEAD@{0}` es ahora; `HEAD@{1}`, un movimiento antes.
- **Qué pasó**: `commit: …` (hiciste un commit), `checkout: moving from A to B` (cambiaste de rama),
  `commit (initial): …` (el primer commit del repositorio).

Para encontrar una rama borrada, busca el último `commit:` que hiciste en ella, justo antes del `checkout` con el que
saliste de ella. En el repositorio de práctica es `HEAD@{1}: commit: Tema listo` (`1bb01f2`). Además, cuando
borras una rama, Git te dice su último hash: `Deleted branch tema-oscuro (was 1bb01f2).`

Otra forma de escribirlo, sin copiar el hash (en Git Bash, Mac o Linux):

```bash
git branch tema-oscuro HEAD@{1}
```

Úsala solo si `HEAD@{1}` es de verdad el commit que buscas: cada commit o cambio de rama nuevo mueve los números.

## Avisos

- **¿Por qué el reflog de HEAD y no el de la rama?** Al borrar una rama, Git también borra su propio reflog. El de HEAD
  se queda.
- **Solo en tu computadora:** el reflog es del repositorio local. Si la rama solo estaba en otra computadora o en
  GitHub, aquí no aparece.
- **No dura para siempre:** por omisión, Git puede limpiar a los **30 días** las entradas de commits que ya no están en
  la rama (como los de una rama borrada) y a los **90 días** las demás. Si borraste algo, recupéralo pronto.
- **`-d` o `-D`:** `git branch -d` (minúscula) se niega a borrar una rama cuyos commits no estén unidos; `-D` borra sin
  preguntar. Usa `-d` por costumbre.
- **El paginador:** si `git reflog` abre un visor porque la salida no cabe, muévete con las flechas y sal con la tecla
  `q`.
- El autor del repositorio de práctica («Práctica») es de práctica y solo vive en la configuración de ese repositorio:
  `practica.sh` no toca tu configuración global.

## Practica en cinco minutos (sin GitHub)

En Git Bash, la Terminal de Mac o Linux, en una carpeta de práctica. Descarga [`practica.sh`](practica.sh) en esa
carpeta y córrelo:

```bash
bash practica.sh
cd practica-reflog
git branch
```

Borra la rama (el accidente) y comprueba que ya no está:

```bash
git branch -D tema-oscuro
git branch
```

Busca su último commit en el reflog:

```bash
git reflog
```

Créala de nuevo en ese commit y comprueba que volvieron sus tres commits:

```bash
git branch tema-oscuro 1bb01f2
git log --oneline -3 tema-oscuro
```

Con `practica.sh`, el hash es el mismo que en el video. En tu propio proyecto, usa el hash que te dé tu `git reflog`.

Fuentes: documentación oficial de Git (`git-reflog`, https://git-scm.com/docs/git-reflog, versión 2.51.1; y
`git-branch`, https://git-scm.com/docs/git-branch, versión 2.56.0) y el libro Pro Git («Maintenance and Data
Recovery», https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery), consultadas el 27 de noviembre
de 2026.
