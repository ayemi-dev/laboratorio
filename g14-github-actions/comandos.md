# Tu primer GitHub Actions · los comandos del video

| Comando | Qué hace |
|---|---|
| `npm test` | Corre el script `test` de `package.json` (aquí, `node --test`) en tu computadora |
| `git switch -c pruebas-automaticas` | Crea la rama `pruebas-automaticas` y te cambia a ella |
| `git add .github/workflows/pruebas.yml` | Prepara el archivo del flujo de trabajo para el commit |
| `git commit -m "Pruebas en cada push"` | Guarda el cambio en la rama |
| `git push -u origin pruebas-automaticas` | Sube la rama a GitHub y la deja enlazada; ese push dispara la ejecución |

## 1. Un proyecto con una prueba

Necesitas Node.js 20 o más nuevo (desde la versión 20 el ejecutor de pruebas `node --test` es estable) y un repositorio en GitHub, como el de [Git y GitHub](../g2-git-github/). Copia a la raíz de tu repositorio `package.json`, `suma.js` y `suma.test.js` de [`plantilla/`](plantilla/) y pruébalo:

```bash
npm test
```

Debe verse así (los tiempos en ms cambian en cada corrida):

```text
> practica-actions@1.0.0 test
> node --test

✔ suma dos números (…ms)
ℹ tests 1
ℹ suites 0
ℹ pass 1
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms …
```

Sin argumentos, `node --test` corre los archivos que terminan en `.test.js` (y otros patrones como `test.js` o la carpeta `test/`). Por eso la prueba se llama `suma.test.js`.

Sube esos tres archivos a `main` como siempre:

```bash
git add package.json suma.js suma.test.js
git commit -m "Proyecto con una prueba"
git push
```

## 2. El flujo de trabajo

GitHub solo busca flujos de trabajo en la carpeta `.github/workflows/` de tu repositorio, en archivos `.yml` o `.yaml`. Crea `.github/workflows/pruebas.yml` (o cópialo de la plantilla):

```yaml
name: Pruebas
on: [push]
jobs:
  pruebas:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: '24.x'
      - run: npm test
```

| Línea | Qué hace |
|---|---|
| `name: Pruebas` | El nombre que verás en la pestaña Actions |
| `on: [push]` | Cuándo corre: en cada push, a cualquier rama, aunque todavía no esté unida a `main` |
| `jobs:` → `pruebas:` | Un trabajo llamado `pruebas` |
| `runs-on: ubuntu-latest` | La máquina: la imagen estable más reciente de Ubuntu que da GitHub |
| `steps:` | Los pasos, en orden |
| `uses: actions/checkout@v7` | Baja tu código a esa máquina |
| `uses: actions/setup-node@v7` + `node-version: '24.x'` | Instala Node.js 24 (`with` le pasa datos a la acción) |
| `run: npm test` | Corre tus pruebas, igual que en tu computadora |

En YAML la sangría importa: usa espacios, no tabuladores, y respeta los niveles de la plantilla.

## 3. Súbelo en una rama nueva

```bash
git switch -c pruebas-automaticas
git add .github/workflows/pruebas.yml
git commit -m "Pruebas en cada push"
git push -u origin pruebas-automaticas
```

## 4. Mira la ejecución

1. En GitHub, abre tu repositorio y haz clic en la pestaña **Actions** (necesitas haber iniciado sesión, aunque el repositorio sea público).
2. A la izquierda, elige el flujo **Pruebas**.
3. Haz clic en la ejecución **Pruebas en cada push**: primero aparece en curso y, al terminar, en verde.
4. Abre el trabajo `pruebas` para ver cada paso; en **Run npm test** está la misma salida que viste en tu computadora.

Desde la terminal, con GitHub CLI: `gh run list` lista las ejecuciones y `gh run view` muestra una.

## 5. La palomita verde en el pull request

Abre un pull request de `pruebas-automaticas` hacia `main` (como en [ramas y pull requests](../g3-ramas-pull-request/)). GitHub Actions deja una verificación en el commit y el pull request la muestra: en verde si las pruebas pasan, en rojo si alguna falla. En la pestaña **Checks** del pull request ves qué corrió y por qué pasó o falló. A partir de aquí, cada push a la rama vuelve a correr las pruebas.

¿Quieres que no se pueda unir mientras falle? Protege la rama `main` y marca la verificación como obligatoria: así debe pasar antes de unir el pull request.

## Si tu proyecto tiene dependencias

Agrega `npm ci` antes de `npm test`: instala exactamente las versiones de tu `package-lock.json` y suele ser más rápido que `npm install`. Sin `package-lock.json`, `npm ci` falla: por eso la plantilla, que no tiene dependencias, no lo usa.

```yaml
      - run: npm ci
      - run: npm test
```

Fuentes: GitHub Docs (*Quickstart for GitHub Actions*, *Workflow syntax*, *Events that trigger workflows*, *GitHub-hosted runners*, *Building and testing Node.js*, *Viewing workflow run history*, *Using workflow run logs*, *About status checks*), los README de [`actions/checkout`](https://github.com/actions/checkout) y [`actions/setup-node`](https://github.com/actions/setup-node), y Node.js (https://nodejs.org/api/test.html, https://nodejs.org/en/about/previous-releases), consultadas el 21 de noviembre de 2026.
