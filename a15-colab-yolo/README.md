# YOLO en Google Colab: qué es y cómo se usa

Video de la serie **Gratis y oficial** del Laboratorio Ayemi. Sigue al video del plan gratuito de Colab: ahora lo
ponemos a trabajar. YOLO mira una foto completa una sola vez y marca cada objeto con un recuadro y su nombre.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayemi-dev/laboratorio/blob/main/a15-colab-yolo/yolo_colab.ipynb)

## Las celdas del video

| Celda | Código | Qué hace |
|---|---|---|
| 1 | `!pip install ultralytics` | Instala Ultralytics en la máquina de Colab |
| 2 | `!wget -O foto.jpg https://ultralytics.com/images/bus.jpg` | Descarga una foto de ejemplo como `foto.jpg` (cámbiala por la tuya) |
| 3 | `from ultralytics import YOLO` | Trae YOLO a tu cuaderno |
| 3 | `modelo = YOLO("yolo26n.pt")` | Carga YOLO26; los pesos se descargan solos la primera vez |
| 3 | `r = modelo("foto.jpg", save=True)` | Analiza la foto y guarda una copia con los recuadros |

El cuaderno [`yolo_colab.ipynb`](yolo_colab.ipynb) trae además dos celdas: una que lista cada objeto con su confianza y
otra que muestra la foto con los recuadros. Paso a paso, en [`comandos.md`](comandos.md).

## Lo que conviene saber

- **YOLO26** es la versión más reciente de Ultralytics (enero de 2026). Viene entrenado con COCO: **80 tipos de
  objetos**, como autos, bicicletas y animales.
- **Colab es gratis**, pero sus recursos no están garantizados ni son ilimitados. En la versión gratuita, un cuaderno
  corre 12 horas como máximo y se desconecta si lo dejas inactivo. La máquina se borra: descarga tus resultados.
- **GPU:** para una foto no hace falta. Para entrenar tu propio modelo, actívala en
  **Entorno de ejecución > Cambiar tipo de entorno de ejecución**, campo **Aceleración por hardware**.
- **Licencia:** Ultralytics YOLO es AGPL-3.0. Si lo usas en un proyecto que no vas a publicar como código abierto,
  revisa su licencia Enterprise en https://www.ultralytics.com/license.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Preguntas frecuentes de Colab | https://research.google.com/colaboratory/faq.html |
| Abrir cuadernos de GitHub en Colab | https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb |
| Documentación de Ultralytics YOLO | https://docs.ultralytics.com/ |
| Inicio rápido (instalación y primer ejemplo) | https://docs.ultralytics.com/quickstart/ |
| Predicción y resultados | https://docs.ultralytics.com/modes/predict/ |
| Ultralytics en Google Colab | https://docs.ultralytics.com/integrations/google-colab/ |
| Cuaderno oficial de Ultralytics para Colab | https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb |
| Artículo original de YOLO (2015) | https://arxiv.org/abs/1506.02640 |

Datos verificados el 21 de noviembre de 2026 en las páginas oficiales de Google Colab, Ultralytics y arXiv. Ayemi no
tiene relación con Google ni con Ultralytics.

---
Guía: CC BY-SA 4.0 · Cuaderno: MIT · ¿Quieres tu proyecto en línea, configurado y seguro? Lo construimos: https://ayemi.org/enlaces
