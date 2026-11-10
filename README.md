# Laboratorio Ayemi

Código y guías de los videos cortos del **Laboratorio Ayemi**. Cada video plantea un problema real y lo resuelve con una herramienta gratuita o con código. Aquí está todo lo que se usa en cada uno, para que lo repitas tú.

| Carpeta | Video | Saga |
|---|---|---|
| [`a2-oracle-12gb/`](a2-oracle-12gb/) | Un servidor gratis para siempre, con 12 GB de RAM | A · Gratis y oficial |
| [`c1-idea-requisitos/`](c1-idea-requisitos/) | De la idea a los requisitos con IA | C · Web moderna |
| [`d1-limpiar-audio/`](d1-limpiar-audio/) | Limpia el ruido de tu audio con Python | D · Python que resuelve problemas |

**¿Necesitas algo más específico? Lo construimos:** https://ayemi.org/enlaces

## Licencias

- **Código** (`*.py`, `*.js`, `*.ino`, configuraciones): [MIT](LICENSE).
- **Guías y textos** (`*.md`): [CC BY-SA 4.0](LICENSE-GUIAS.md).

Los datos de terceros (ofertas, límites y precios) se verificaron en la fecha que indica cada guía y pueden cambiar. Ayemi no tiene relación con las empresas que se mencionan.

## Para contribuir

Este repositorio revisa cada commit:

```bash
git config core.hooksPath .githooks
```

El hook corre [gitleaks](https://github.com/gitleaks/gitleaks), para que no se suba ningún secreto, y `herramientas/revisar_nombres.py`, que bloquea los términos de una lista local que no se publica.
