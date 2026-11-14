# Git y GitHub: qué hace cada comando

Segundo video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Si guardas tus versiones como `final2_ahora-si.zip`, Git es la herramienta que lo resuelve.

- **Git** guarda la historia de tu proyecto en tu computadora: cada versión, con su mensaje.
- **GitHub** guarda tus repositorios en la nube, para respaldarlos y compartirlos.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `git init` | Convierte la carpeta en un repositorio: crea la carpeta oculta `.git`, donde vive la historia |
| `git status` | Te dice qué archivos son nuevos, cuáles cambiaron y cuáles ya están listos para guardar |
| `git add <archivo>` o `git add .` | Elige qué cambios van en la siguiente versión (los pasa al «área de preparación») |
| `git commit -m "mensaje"` | Guarda esa versión con un mensaje que explica qué hiciste |
| `git log --oneline` | Muestra la lista de versiones, una por línea, de la más nueva a la más vieja |
| `git remote add origin <URL>` | Conecta tu repositorio con otro, por ejemplo el que creaste en GitHub |
| `git push -u origin main` | Sube tus versiones de la rama `main` a ese repositorio; con `-u`, la próxima vez basta `git push` |
| `git clone <URL>` | Descarga un repositorio completo, con toda su historia, en otra computadora |

El paso a paso para probarlo con un proyecto de ejemplo está en [`comandos.md`](comandos.md).

**En el siguiente video:** ramas y pull requests.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Descargar Git | https://git-scm.com/downloads |
| Documentación de los comandos | https://git-scm.com/docs |
| Libro Pro Git en español, en línea | https://git-scm.com/book/es/v2 |
| Qué son GitHub y Git | https://docs.github.com/en/get-started/start-your-journey/about-github-and-git |
| Video anterior: VS Code | [`../g1-vscode/`](../g1-vscode/) |

Datos verificados el 13 de noviembre de 2026 en la documentación oficial. Ayemi no tiene relación con GitHub.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
