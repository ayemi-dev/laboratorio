# YOLO en Google Colab · paso a paso

## 1. Abre el cuaderno

- **Directo:** https://colab.research.google.com/github/ayemi-dev/laboratorio/blob/main/a15-colab-yolo/yolo_colab.ipynb
  (Colab abre cuadernos públicos de GitHub sin autorización; para correrlo, entra con tu cuenta de Google).
- **O desde cero:** crea un cuaderno nuevo en https://colab.research.google.com/ y pega las celdas de abajo, una por
  celda.

Corre las celdas en orden. El signo `!` al inicio indica un comando para la máquina de Colab, no código de Python.

## 2. Instala Ultralytics

```text
!pip install ultralytics
```

## 3. Consigue una foto llamada `foto.jpg`

Foto de ejemplo de Ultralytics:

```text
!wget -O foto.jpg https://ultralytics.com/images/bus.jpg
```

Para usar tu foto, cambia la dirección por la de tu imagen (debe ser una dirección pública que termine en la imagen).

## 4. Detecta los objetos

```python
from ultralytics import YOLO
modelo = YOLO("yolo26n.pt")
r = modelo("foto.jpg", save=True)
```

- `yolo26n.pt` son los pesos de YOLO26 para detección; se descargan solos la primera vez.
- `save=True` guarda la foto con los recuadros. En Python no se guarda si no lo pides.
- La salida dice qué encontró y cuántos de cada uno, y la carpeta donde guardó el resultado
  (`runs/detect/predict` la primera vez).

## 5. Lista los objetos con su confianza

```python
for caja in r[0].boxes:
    print(modelo.names[int(caja.cls)], round(float(caja.conf), 2))
```

La confianza va de 0 a 1. Los nombres salen en inglés: son las 80 clases de COCO, con las que viene entrenado
YOLO26.

## 6. Mira la foto con los recuadros

```python
from PIL import Image
Image.fromarray(r[0].plot()[:, :, ::-1].copy())
```

`plot()` devuelve la imagen en BGR; `[:, :, ::-1]` la pasa a RGB para que los colores se vean bien.

## Antes de cerrar

- La máquina de Colab se borra cuando queda inactiva y, en la versión gratuita, dura 12 horas como máximo: descarga
  la carpeta `runs` si quieres conservar los resultados.
- **GPU:** para una foto no hace falta. Para entrenar tu propio modelo, actívala en **Entorno de ejecución > Cambiar tipo
  de entorno de ejecución**, campo **Aceleración por hardware**.
- **Licencia:** Ultralytics YOLO es AGPL-3.0. Para usarlo en un proyecto cerrado necesitas su licencia Enterprise
  (https://www.ultralytics.com/license).

Fuentes, consultadas el 21 de noviembre de 2026: preguntas frecuentes de Colab
(https://research.google.com/colaboratory/faq.html), cuaderno oficial «colab-github-demo» de Google, documentación de
Ultralytics (`docs.ultralytics.com`: inicio rápido, modelos, predicción, COCO y Google Colab), licencia de Ultralytics
(https://www.ultralytics.com/license) y el artículo de YOLO en arXiv (https://arxiv.org/abs/1506.02640).
