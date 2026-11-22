# Que tus claves no lleguen a GitHub: .gitignore y gitleaks

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Continúa [Git y GitHub](../g2-git-github/) y [GitHub Actions](../g14-github-actions/): antes de tu próximo `git push`, asegúrate de que tu archivo `.env`, con tus claves, no va en el commit. Todo en un **repositorio de práctica** con una **clave FALSA**. En Git Bash (Windows), Linux y Mac.

- **`.gitignore`** le dice a Git qué archivos no debe seguir. La primera línea de tu `.gitignore` debería ser `.env`.
- **`.gitignore` no saca lo que ya entró en un commit.** Para eso, **`git rm --cached .env`**: lo quita del repositorio y lo deja en tu compu.
- **`git check-ignore -v .env`** te dice qué regla lo ignora, de qué archivo y en qué línea.
- **gitleaks** revisa todo el historial de Git y te dice el archivo, la línea y el commit donde hay una clave.
- **Si la clave ya subió a GitHub, rótala:** cancélala en el servicio que la dio y crea otra. Borrarla del historial no basta.

## La plantilla

[`plantilla/.gitignore`](plantilla/.gitignore) es un `.gitignore` para claves: ignora `.env` y sus variantes (`.env.local`, `.env.production`…), deja pasar `.env.example` y también ignora llaves y certificados (`*.pem`, `*.key`). Cópiala a la raíz de tu proyecto **antes del primer commit**.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `cat .env` | Muestra tu archivo de claves (en el video, una FALSA) |
| `git add .` | Mete todo al próximo commit, también `.env` si nada lo ignora |
| `gitleaks git -v` | Busca claves en todo el historial |
| `echo .env >> .gitignore` | Agrega `.env` a tu `.gitignore` |
| `git rm --cached .env` | Saca `.env` del repositorio sin borrarlo de tu compu |
| `git check-ignore -v .env` | Dice qué regla ignora `.env` y en qué línea |
| `git log --oneline` | Lista tus commits, uno por línea |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `gitignore` | https://git-scm.com/docs/gitignore |
| `git check-ignore` | https://git-scm.com/docs/git-check-ignore |
| `git rm` | https://git-scm.com/docs/git-rm |
| gitleaks (repositorio oficial) | https://github.com/gitleaks/gitleaks |
| Qué hacer si subiste una clave (GitHub) | https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository |
| Git for Windows (Git Bash) | https://gitforwindows.org/ |
| Videos anteriores | [`../g2-git-github/`](../g2-git-github/) y [`../g14-github-actions/`](../g14-github-actions/) |

Datos verificados el 22 de noviembre de 2026 en la documentación de Git (git-scm.com), el repositorio oficial de gitleaks y la documentación de GitHub. Ayemi no tiene relación con Git, GitHub, gitleaks, Amazon Web Services ni Git for Windows.

---
Guía: CC BY-SA 4.0 · Código: MIT · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
