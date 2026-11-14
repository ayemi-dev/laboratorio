# Git · los comandos del video

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

**Antes del primer commit**, dile a Git quién eres (una sola vez por computadora):

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@correo.com"
```

**Prueba con un proyecto de ejemplo:**

```bash
mkdir mi-pagina
cd mi-pagina
git init
echo "<h1>Hola</h1>" > index.html
git status
git add .
git commit -m "Primera versión"
git log --oneline
```

Para subirlo, crea un repositorio vacío en GitHub y usa la URL que te muestra:

```bash
git remote add origin https://github.com/tu-usuario/mi-pagina.git
git push -u origin main
```

Si tu rama se llama `master` en lugar de `main`, usa ese nombre en el `push`.

Fuentes: la documentación oficial de Git (https://git-scm.com/docs) y «About GitHub and Git» (https://docs.github.com/en/get-started/start-your-journey/about-github-and-git), consultadas el 13 de noviembre de 2026.
