# Deshacer sin miedo en Git: restore, revert y reset

Séptimo video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de
[Git y GitHub](../g2-git-github/). Ya subiste tu primer commit; ahora, cómo deshacer un error sin romper más.

## La idea: primero mira dónde está el error

| Dónde está el error | Comando | Qué pasa |
|---|---|---|
| En un archivo que cambiaste y **no** has guardado en un commit | `git restore index.html` | El archivo vuelve a su última versión guardada. Esos cambios se pierden |
| En un commit que **ya compartiste** (ya hiciste `git push`) | `git revert --no-edit HEAD` y luego `git push` | Git crea un commit **nuevo** que deshace el anterior. La historia queda completa |
| En un commit que **solo** está en tu computadora | `git reset HEAD~1` | El commit se quita y tus cambios siguen en el archivo |

**La regla:** si el error ya es público, crea un commit nuevo que lo deshaga (`git revert`). No cambies una historia que
ya compartiste: `git reset` solo en local.

Antes de deshacer, `git diff` te muestra qué cambiaste y `git status` en qué estado está tu carpeta.

La guía completa, con los avisos y una práctica de cinco minutos sin GitHub, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `git restore` | https://git-scm.com/docs/git-restore |
| `git revert` | https://git-scm.com/docs/git-revert |
| `git reset` | https://git-scm.com/docs/git-reset |
| Manual de Git: «Fixing mistakes» | https://git-scm.com/docs/user-manual#fixing-mistakes |
| Pro Git: «Undoing Things» | https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things |
| Video anterior de esta parte: Git y GitHub | [`../g2-git-github/`](../g2-git-github/) |

Datos verificados el 20 de noviembre de 2026 en la documentación oficial de Git (git-scm.com). Ayemi no tiene relación
con Git ni con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
