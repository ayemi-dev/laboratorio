# GitHub Actions nivel 2 · los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch -c suma-rota` | Crea la rama `suma-rota` y te cambia a ella |
| `git diff` | Muestra lo que cambiaste y aún no guardas en un commit |
| `git commit -am "Resta en lugar de suma"` | Prepara y guarda en un paso los archivos que Git ya conoce |
| `git push -u origin suma-rota` | Sube la rama a GitHub y la deja enlazada |
| `gh pr create --fill` | Abre un pull request hacia la rama principal con el título y el cuerpo del commit |
| `gh pr checks` | Muestra el estado de las verificaciones del pull request de la rama actual |
| `gh pr merge --merge` | Intenta unir el pull request de la rama actual con un commit de unión |

Necesitas Node.js 20 o más nuevo, Git y [GitHub CLI](https://cli.github.com) con tu sesión (`gh auth login`), y un repositorio en GitHub donde seas administrador. Si vienes de [G14](../g14-github-actions/), es el mismo proyecto con un flujo más completo.

## 1. El proyecto en `main`

Copia a la raíz de tu repositorio todo lo de [`plantilla/`](plantilla/): `package.json`, `package-lock.json`, `suma.js`, `suma.test.js` y `.github/workflows/pruebas.yml`. Pruébalo:

```bash
npm ci
npm test
```

`npm test` debe terminar con `ℹ pass 1` y `ℹ fail 0` (los tiempos en ms cambian en cada corrida). Súbelo a `main`:

```bash
git add .
git commit -m "Proyecto con pruebas en cada pull request"
git push
```

Este push a `main` **no** dispara el flujo: solo corre con pull requests.

## 2. El flujo de trabajo

```yaml
name: Pruebas
on: [pull_request]
jobs:
  pruebas:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        node: ['24.x', '26.x']
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

| Línea | Qué hace |
|---|---|
| `on: [pull_request]` | Corre al abrir un pull request, al reabrirlo y en cada push a su rama. Las pruebas corren sobre el resultado de unir el pull request con la rama de destino |
| `strategy:` → `matrix:` → `node: ['24.x', '26.x']` | Crea dos copias del trabajo `pruebas`, una por versión. Node.js 24 y 26 son versiones LTS |
| `node-version: ${{ matrix.node }}` | Cada copia instala su versión |
| `cache: 'npm'` | Guarda la caché de npm entre ejecuciones (no `node_modules`). La llave sale de `package-lock.json`. Este proyecto no tiene dependencias, así que la caché casi no guarda nada; se nota cuando tu proyecto sí las tiene |
| `run: npm ci` | Instala exactamente lo de `package-lock.json`, sin modificarlo. Sin ese archivo, falla |
| `run: npm test` | Corre tus pruebas |

En GitHub, cada copia aparece como una verificación con el nombre del trabajo y su valor: `pruebas (24.x)` y `pruebas (26.x)`.

## 3. Protege `main`

Una verificación en rojo, por sí sola, no impide unir. Para que lo impida, protege la rama y hazla obligatoria. [`proteccion.json`](proteccion.json):

```json
{
  "required_status_checks": {
    "strict": false,
    "checks": [
      { "context": "pruebas (24.x)" },
      { "context": "pruebas (26.x)" }
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": null,
  "restrictions": null
}
```

- `checks`: las dos verificaciones que deben pasar antes de unir.
- `enforce_admins: true`: la regla también aplica a quien administra el repositorio (por defecto no aplica).
- `strict: false`: no exige que la rama esté al día con `main` antes de unir.
- `required_pull_request_reviews` y `restrictions` en `null`: sin revisiones obligatorias ni lista de quién puede subir.

Desde la carpeta de tu repositorio, con GitHub CLI (`{owner}/{repo}` lo llena `gh` con tu repositorio; cambia la ruta de `proteccion.json` a donde lo guardaste, fuera del repositorio):

```bash
gh api --method PUT repos/{owner}/{repo}/branches/main/protection --input proteccion.json
```

Desde la página: **Settings** → **Branches** → agrega una regla para `main`, activa la opción que exige verificaciones antes de unir, busca `pruebas (24.x)` y `pruebas (26.x)` (aparecen después de que el flujo corrió al menos una vez) y activa la opción que aplica la regla también a administradores.

La protección de ramas está disponible en repositorios públicos con GitHub Free y GitHub Free para organizaciones; en privados, con los planes de pago de GitHub. Protegerla pide permisos de administrador del repositorio.

## 4. Rómpelo a propósito

```bash
git switch -c suma-rota
```

En `suma.js`, cambia `return a + b;` por `return a - b;` y guarda. Revisa el cambio:

```bash
git diff
```

```diff
-  return a + b;
+  return a - b;
```

Súbelo y abre el pull request:

```bash
git commit -am "Resta en lugar de suma"
git push -u origin suma-rota
gh pr create --fill
```

## 5. Las verificaciones en rojo

Cuando terminen las dos ejecuciones:

```bash
gh pr checks
```

```text
pruebas (24.x)	fail	7s	https://github.com/ayemi-dev/practica-pruebas/actions/runs/45110813218/job/137482491346
pruebas (26.x)	fail	10s	https://github.com/ayemi-dev/practica-pruebas/actions/runs/45110813218/job/137482491554
```

Las dos, `pruebas (24.x)` y `pruebas (26.x)`, salen como fallidas: la prueba espera `5` y la resta da `-1`.

## 6. El merge bloqueado

```bash
gh pr merge --merge
```

```text
X Pull request ayemi-dev/practica-pruebas#2 is not mergeable: the base branch policy prohibits the merge.
To have the pull request merged after all the requirements have been met, add the `--auto` flag.
To use administrator privileges to immediately merge the pull request, add the `--admin` flag.
```

GitHub no lo une mientras las verificaciones obligatorias no pasen (y con `enforce_admins`, ni siquiera `--admin` lo salta). En la página del pull request el botón para unir queda bloqueado.

## 7. Arréglalo (no sale en el video)

Devuelve `return a + b;` en `suma.js` y:

```bash
git commit -am "Vuelve a sumar"
git push
```

Ese push vuelve a correr las dos verificaciones. Deben pasar en el **último** commit del pull request; las de commits anteriores no cuentan. Cuando estén en verde, `gh pr merge --merge` ya lo une.

En el repositorio de práctica, el pull request #2 se dejó en rojo y sin unir, como ejemplo.

Fuentes: GitHub Docs (*Events that trigger workflows*, *Running variations of jobs in a workflow*, *Building and testing Node.js*, *About protected branches*, *Branch protection* en la API REST, *About status checks*, *Troubleshooting required status checks*), el manual de GitHub CLI (`gh pr create`, `gh pr checks`, `gh pr merge`), los README de [`actions/checkout`](https://github.com/actions/checkout) y [`actions/setup-node`](https://github.com/actions/setup-node), y Node.js (https://nodejs.org/en/about/previous-releases), consultadas el 22 de noviembre de 2026.
