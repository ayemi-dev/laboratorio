# Tu primer GitHub Actions: que GitHub corra tus pruebas solo en cada push

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y continuación de [Git y GitHub](../g2-git-github/) y de [ramas y pull requests](../g3-ramas-pull-request/). Ya subes tu código a GitHub; ahora un archivo de 11 líneas hace que GitHub corra tus pruebas en cada push, y el resultado aparece en la pestaña **Actions** y como palomita verde en tu pull request.

- **El archivo** vive en `.github/workflows/` y es YAML (`.yml` o `.yaml`).
- **`on: [push]`** lo dispara en cada push, también en ramas que todavía no unes a `main`.
- **Tres pasos**: `actions/checkout` baja tu código, `actions/setup-node` instala Node.js y `npm test` corre tus pruebas.

## La plantilla

En [`plantilla/`](plantilla/) está el proyecto del video, tal cual: cópialo a la raíz de tu repositorio (la carpeta `.github` también; en algunos sistemas está oculta).

| Archivo | Qué es |
|---|---|
| [`plantilla/.github/workflows/pruebas.yml`](plantilla/.github/workflows/pruebas.yml) | El flujo de trabajo: en cada push, baja el código, instala Node.js 24 y corre `npm test` |
| [`plantilla/package.json`](plantilla/package.json) | Define `npm test` como `node --test` (el ejecutor de pruebas que trae Node.js) |
| [`plantilla/suma.js`](plantilla/suma.js) | La función que se prueba |
| [`plantilla/suma.test.js`](plantilla/suma.test.js) | La prueba; `node --test` encuentra solo los archivos que terminan en `.test.js` |

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

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `npm test` | Corre tus pruebas en tu computadora |
| `git switch -c pruebas-automaticas` | Crea una rama nueva y te cambia a ella |
| `git add .github/workflows/pruebas.yml` | Prepara el archivo del flujo de trabajo |
| `git commit -m "Pruebas en cada push"` | Guarda el cambio |
| `git push -u origin pruebas-automaticas` | Sube la rama a GitHub; ese push dispara la ejecución |

La guía completa, con cómo preparar el proyecto, dónde ver la ejecución, el pull request y qué cambiar si tu proyecto tiene dependencias, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Repositorio de práctica del video (público) | https://github.com/ayemi-dev/practica-actions |
| Descargar Node.js | https://nodejs.org/en/download |
| Inicio rápido de GitHub Actions (GitHub Docs) | https://docs.github.com/en/actions/get-started/quickstart |
| Probar Node.js con GitHub Actions (GitHub Docs) | https://docs.github.com/en/actions/tutorials/build-and-test-code/nodejs |
| Sintaxis de los flujos de trabajo (GitHub Docs) | https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax |
| Ver las ejecuciones (GitHub Docs) | https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history |
| Verificaciones en los pull requests (GitHub Docs) | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks |
| `actions/checkout` | https://github.com/actions/checkout |
| `actions/setup-node` | https://github.com/actions/setup-node |
| Ejecutor de pruebas de Node.js | https://nodejs.org/api/test.html |
| Videos anteriores: Git y GitHub; ramas y pull requests | [`../g2-git-github/`](../g2-git-github/) · [`../g3-ramas-pull-request/`](../g3-ramas-pull-request/) |

Datos verificados el 21 de noviembre de 2026 en la documentación oficial de GitHub y de Node.js. Ayemi no tiene relación con GitHub ni con Microsoft.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
