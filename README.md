# Laboratorio Ayemi

Código y guías de los videos cortos del **Laboratorio Ayemi**. Cada video plantea un problema real y lo resuelve con una herramienta gratuita o con código. Aquí está todo lo que se usa en cada uno, para que lo repitas tú.

| Carpeta | Video | Saga |
|---|---|---|
| [`a2-oracle-12gb/`](a2-oracle-12gb/) | Un servidor gratis para siempre, con 12 GB de RAM | A · Gratis y oficial |
| [`c1-idea-requisitos/`](c1-idea-requisitos/) | De la idea a los requisitos con IA | C · Web moderna |
| [`d1-limpiar-audio/`](d1-limpiar-audio/) | Limpia el ruido de tu audio con Python | D · Python que resuelve problemas |
| [`e1-pieza-por-codigo/`](e1-pieza-por-codigo/) | Una pieza 3D escrita en Python con build123d | E · Modelado 3D con código |
| [`e2-gabinete-por-codigo/`](e2-gabinete-por-codigo/) | Un gabinete de base y tapa escrito en Python | E · Modelado 3D con código |
| [`af1-wokwi-arduino/`](af1-wokwi-arduino/) | Simula un Arduino gratis en el navegador | F · Microcontroladores |
| [`f2-wokwi-esp32/`](f2-wokwi-esp32/) | Un ESP32 simulado que consulta el clima en internet | F · Microcontroladores |
| [`f5-kicad-primera-placa/`](f5-kicad-primera-placa/) | De protoboard a placa con KiCad | F · Microcontroladores |

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
