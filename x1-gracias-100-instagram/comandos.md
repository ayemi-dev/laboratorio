# Cómo bajar todo el código del Laboratorio

Verificado el 20 de noviembre de 2026 en la documentación oficial de GitHub. Ayemi no tiene relación con GitHub.

## Opción 1 · Con Git (recomendada)

Así tienes una copia completa del repositorio en tu computadora. Si todavía no usas Git, empieza por [`g2-git-github/`](../g2-git-github/).

Abre la terminal en la carpeta donde quieras guardarlo (si la terminal te da miedo, mira [`g4-terminal-sin-miedo/`](../g4-terminal-sin-miedo/)) y escribe, uno por uno:

```bash
git clone https://github.com/ayemi-dev/laboratorio
cd laboratorio
ls
```

`ls` te muestra una carpeta por video. Para entrar a la de un video, por ejemplo la terminal sin miedo:

```bash
cd g4-terminal-sin-miedo
```

Los mismos comandos funcionan en Windows (PowerShell o Git Bash), en Linux y en Mac.

Cuando publiquemos videos nuevos, actualiza tu copia desde la carpeta `laboratorio`:

```bash
git pull
```

## Opción 2 · Sin Git, en un ZIP

Descarga este archivo y descomprímelo:

```text
https://github.com/ayemi-dev/laboratorio/archive/refs/heads/main.zip
```

También puedes abrir https://github.com/ayemi-dev/laboratorio, tocar el botón **Code** y luego **Download ZIP**. El ZIP no se actualiza solo: vuelve a bajarlo cuando haya videos nuevos.

## Fuentes

| Qué | Enlace |
|---|---|
| Clonar un repositorio | https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository |
| Descargar el código en un archivo comprimido | https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives |

## Licencias

El código va con licencia [MIT](../LICENSE) y las guías con [CC BY-SA 4.0](../LICENSE-GUIAS.md). Emi tiene su propia licencia: ver [`e6-emi-en-blender/`](../e6-emi-en-blender/).
