# Que tus claves no lleguen a GitHub · .gitignore y gitleaks

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows) o en la terminal de **Linux** o **Mac**. Necesitas **Git** y **gitleaks**.

> **Regla de oro:** tus claves viven en tu compu (por ejemplo, en `.env`) y **nunca** entran a un commit. Si una ya subió a GitHub, **rótala**: cancélala y crea otra.

## 0. Instala gitleaks

Según su repositorio oficial, gitleaks se instala con Homebrew, Docker o Go, o bajando el programa de su [página de versiones](https://github.com/gitleaks/gitleaks/releases). En Mac:

```sh
brew install gitleaks
```

En Windows, baja el `.zip` de Windows de la página de versiones y pon `gitleaks.exe` en una carpeta de tu `PATH` (lo vimos en G18). Comprueba:

```sh
gitleaks version
```

## 1. Arma el repositorio de práctica

En una carpeta nueva, **fuera** de tus proyectos:

```sh
mkdir practica
cd practica
git init
echo 'console.log("hola");' > app.js
```

Crea el `.env` con una clave **falsa** (dice EJEMPLO y FALSA y no da acceso a nada). El comentario del final es para que el gancho de commits de este repositorio no la bloquee; a tu terminal no le afecta:

```sh
printf '# clave FALSA de ejemplo\nAWS_ACCESS_KEY_ID=AKIAEJEMPLOFALSA2345\n' > .env  # gitleaks:allow
```

```sh
cat .env
```

Debe mostrar dos líneas: el comentario `# clave FALSA de ejemplo` y la variable `AWS_ACCESS_KEY_ID`.

> **¿Por qué esa forma?** gitleaks reconoce las claves por su forma. Esta se parece a una llave de acceso de AWS, así que su regla `aws-access-token` la encuentra. No uses la clave de ejemplo de la documentación de AWS (la que termina en `EXAMPLE`): gitleaks la deja pasar a propósito.

## 2. El error: `git add .`

```sh
git add .
git commit -m "primer commit"
```

En la salida verás `create mode 100644 .env`: tu clave ya está en un commit. Con un `git push`, subiría a GitHub.

## 3. La alarma: gitleaks

```sh
gitleaks git -v
```

Revisa todo el historial. Por cada clave muestra, entre otros, `RuleID` (qué tipo de clave), `File` (el archivo), `Line` (la línea) y `Commit` (el commit). Aquí: `aws-access-token`, `.env`, línea 2, el `primer commit`. Al final avisa cuántas fugas encontró.

- Si no encuentra nada, sale con **0**; si encuentra algo, con **1**. Por eso sirve para frenar un commit o un flujo de GitHub Actions como el de [G14](../g14-github-actions/).
- Con claves **reales**, agrega `--redact` para que no las imprima: `gitleaks git -v --redact`.
- `gitleaks detect` es el nombre viejo de `gitleaks git`: todavía funciona, pero ya no sale en la ayuda.

## 4. El arreglo: `.gitignore` y `git rm --cached`

```sh
echo .env >> .gitignore
git rm --cached .env
```

- La primera línea agrega `.env` a tu `.gitignore` (lo crea si no existe).
- `.gitignore` **no** afecta a los archivos que ya están en un commit. Por eso, `git rm --cached .env` lo saca del repositorio. Debe decir `rm '.env'`. **Tu archivo sigue en tu compu**: compruébalo con `cat .env`.

¿Prefieres la versión completa? Copia [`plantilla/.gitignore`](plantilla/.gitignore) a la raíz de tu proyecto: ignora `.env`, `.env.local`, `.env.production` y parecidos, deja pasar `.env.example` y también ignora `*.pem` y `*.key`.

## 5. La prueba: `git check-ignore`

```sh
git check-ignore -v .env
```

```text
.gitignore:1:.env	.env
```

Se lee: el archivo `.gitignore`, línea **1**, la regla `.env`, ignora el archivo `.env`. Si no imprime nada, `.env` **no** está ignorado.

## 6. La lección: el commit viejo la sigue guardando

```sh
git add .gitignore
git commit -m "ignora .env"
git log --oneline
gitleaks git -v
```

gitleaks la vuelve a encontrar, en el **primer commit**: sacarla ahora no cambia los commits de antes.

## 7. Si ya la subiste: rótala

1. **Rota la clave primero:** entra al servicio que te la dio, **cancélala** y **crea otra**. Pon la nueva solo en tu `.env`. Una clave cancelada ya no sirve para entrar, aunque siga en el historial.
2. Revisa que `.env` esté en `.gitignore` y fuera del repositorio (pasos 4 y 5).
3. Borrar la clave del historial y forzar el push **no basta**: puede seguir copiada en otros lados (clones, forks, cachés). Si aun así necesitas limpiarlo, sigue la guía de GitHub de abajo.

## Al terminar

Borra la carpeta `practica`: la clave es falsa, pero no la necesitas.

## Fuentes

- `gitignore`: https://git-scm.com/docs/gitignore — «A `gitignore` file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected»
- `git rm`: https://git-scm.com/docs/git-rm — `--cached`: «Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone.»
- `git check-ignore`: https://git-scm.com/docs/git-check-ignore — «Debug gitignore / exclude files»
- gitleaks: https://github.com/gitleaks/gitleaks — «Gitleaks is a tool for detecting secrets like passwords, API keys, and tokens in git repos»
- GitHub, datos sensibles: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository — «as a first step you need to revoke and/or rotate that secret.»

Verificado el 22 de noviembre de 2026.
