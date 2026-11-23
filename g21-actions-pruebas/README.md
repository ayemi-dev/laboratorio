# GitHub Actions nivel 2: pruebas automáticas en cada pull request

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de [Tu primer GitHub Actions](../g14-github-actions/). En G14 GitHub corría tus pruebas en cada push y dejaba una palomita verde; aquí las pruebas corren en cada pull request, en dos versiones de Node.js a la vez, y si fallan **el pull request no se puede unir**.

- **`on: [pull_request]`** corre el flujo al abrir el pull request y en cada push a su rama.
- **La matriz** repite el trabajo en Node.js 24 y Node.js 26.
- **`cache: 'npm'` y `npm ci`** guardan la caché de npm entre ejecuciones e instalan exactamente lo de `package-lock.json`.
- **La protección de `main`** hace obligatorias las dos verificaciones, también para quien administra el repositorio.

## La plantilla

En [`plantilla/`](plantilla/) está el proyecto del video, tal cual: cópialo a la raíz de tu repositorio (la carpeta `.github` también; en algunos sistemas está oculta). [`proteccion.json`](proteccion.json) no va al repositorio: es la regla de protección que se manda a GitHub (sección 4 de [`comandos.md`](comandos.md)).

| Archivo | Qué es |
|---|---|
| [`plantilla/.github/workflows/pruebas.yml`](plantilla/.github/workflows/pruebas.yml) | El flujo de trabajo: en cada pull request, baja el código, instala Node.js 24 y 26 (con caché de npm), corre `npm ci` y `npm test` |
| [`plantilla/package.json`](plantilla/package.json) | Define `npm test` como `node --test` (el ejecutor de pruebas que trae Node.js) |
| [`plantilla/package-lock.json`](plantilla/package-lock.json) | El archivo de bloqueo que piden `npm ci` y la caché (este proyecto no tiene dependencias) |
| [`plantilla/suma.js`](plantilla/suma.js) | La función que se prueba |
| [`plantilla/suma.test.js`](plantilla/suma.test.js) | La prueba |
| [`proteccion.json`](proteccion.json) | La regla de protección de `main`: las verificaciones `pruebas (24.x)` y `pruebas (26.x)` obligatorias, también para administradores |

```yaml
name: Pruebas
on: [pull_request]
jobs:
  pruebas:
    runs-on: ubuntu-latest
    strategy:
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

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `git switch -c suma-rota` | Crea una rama nueva y te cambia a ella |
| `git diff` | Muestra el cambio que hiciste en `suma.js` (la suma pasa a resta) |
| `git commit -am "Resta en lugar de suma"` | Guarda el cambio de los archivos que Git ya conoce |
| `git push -u origin suma-rota` | Sube la rama a GitHub |
| `gh pr create --fill` | Abre el pull request con el mensaje del commit como título |
| `gh pr checks` | Muestra las verificaciones del pull request de tu rama |
| `gh pr merge --merge` | Intenta unirlo; con las verificaciones en rojo, GitHub no lo deja |

La guía completa, con cómo preparar el repositorio, proteger `main` (desde la terminal o desde Settings) y arreglar el pull request, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Repositorio de práctica del video (público) | https://github.com/ayemi-dev/practica-pruebas |
| GitHub CLI | https://cli.github.com |
| Eventos que disparan un flujo (GitHub Docs) | https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows |
| Matrices de trabajos (GitHub Docs) | https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations |
| Probar Node.js con GitHub Actions (GitHub Docs) | https://docs.github.com/en/actions/tutorials/build-and-test-code/nodejs |
| Ramas protegidas (GitHub Docs) | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches |
| API de protección de ramas (GitHub Docs) | https://docs.github.com/en/rest/branches/branch-protection |
| Verificaciones en los pull requests (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks |
| `actions/checkout` | https://github.com/actions/checkout |
| `actions/setup-node` | https://github.com/actions/setup-node |
| Versiones de Node.js | https://nodejs.org/en/about/previous-releases |
| Video anterior: Tu primer GitHub Actions | [`../g14-github-actions/`](../g14-github-actions/) |

Datos verificados el 22 de noviembre de 2026 en la documentación oficial de GitHub y de Node.js. Ayemi no tiene relación con GitHub ni con Microsoft.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
