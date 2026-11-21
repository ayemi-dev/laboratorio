# Colab gratis: lo que te da y cómo comprobarlo

Video de la serie **Gratis y oficial** del Laboratorio Ayemi. Google no publica cuánta memoria, disco o qué GPU te da
la versión gratuita de Colab: su FAQ oficial dice que los límites cambian con el tiempo. Aquí está lo que sí publica y
un cuaderno de cuatro comandos para ver qué te tocó a ti.

## Ábrelo en Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayemi-dev/laboratorio/blob/main/a14-colab-gratis/especificaciones.ipynb)

O descarga [`especificaciones.ipynb`](especificaciones.ipynb) y súbelo a Colab. La celda y cómo leer su resultado
están en [`comandos.md`](comandos.md).

## Lo que sí publica Google

| Dato | Qué dice la FAQ oficial |
|---|---|
| Qué es | Un servicio alojado de Jupyter Notebook, sin configuración, con acceso sin costo a recursos de cómputo, incluidas GPU y TPU |
| ¿Es gratis? | «Sí. Puedes usar Colab sin coste adicional.» |
| Límites | No están garantizados ni son ilimitados, y **Colab no los publica** porque cambian con el tiempo |
| Tiempo | En la versión gratuita, un cuaderno corre **12 horas como máximo**, y se apaga si lo dejas inactivo |
| GPU | En la versión gratuita, el acceso a las GPU está **muy restringido**; los tipos de GPU y TPU cambian con el tiempo |
| Memoria | Máquinas virtuales con una capacidad **estándar** de memoria del sistema (sin cifra publicada) |
| Archivos | Los cuadernos se guardan en Google Drive o se cargan desde GitHub. La máquina virtual se elimina tras un tiempo inactiva, y al compartir un cuaderno no se comparten la máquina ni sus archivos |
| Disco | Comprar más espacio en Drive no agranda el disco de la máquina de Colab |

## Lo que no se permite en la versión gratuita

Entre otras cosas, la FAQ prohíbe en los entornos gratuitos el control remoto (SSH o escritorio remoto) y los nodos de
cómputo distribuido, y en todos los entornos minar criptomonedas o usar varias cuentas para saltarse límites. Colab da
prioridad a quien programa activamente en un cuaderno. La lista completa está en la FAQ.

## Sugerencias

- Guarda tus resultados en Drive: la máquina virtual se elimina.
- Si no usas la GPU, regresa el tipo de entorno de ejecución a ninguno.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| FAQ oficial de Colab (español) | https://research.google.com/colaboratory/intl/es/faq.html |
| FAQ oficial de Colab (inglés) | https://research.google.com/colaboratory/faq.html |
| Abrir cuadernos de GitHub en Colab | https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb |
| Comandos con `!` en un cuaderno (IPython) | https://ipython.readthedocs.io/en/stable/interactive/reference.html |
| `nproc`, `free` y `df` | https://man7.org/linux/man-pages/man1/nproc.1.html · https://man7.org/linux/man-pages/man1/free.1.html · https://man7.org/linux/man-pages/man1/df.1.html |
| `nvidia-smi` | https://docs.nvidia.com/deploy/nvidia-smi/index.html |
| Video anterior: Canvas de Gemini | [`../a13-canvas-tablero/`](../a13-canvas-tablero/) |

Datos verificados el 20 de noviembre de 2026 en la FAQ oficial de Colab. Pueden cambiar. Ayemi no tiene relación con
Google.

---
Guía: CC BY-SA 4.0 · Cuaderno: MIT · ¿Quieres tu proyecto en línea, configurado y seguro? Lo construimos:
https://ayemi.org/enlaces
