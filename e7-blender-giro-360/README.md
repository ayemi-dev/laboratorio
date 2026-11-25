# Un giro de 360° de tu modelo con un script de Python

Séptimo video de la saga **E · Modelado 3D con código** del Laboratorio Ayemi. En [E5](../e5-blender/) y
[E6](../e6-emi-en-blender/) el giro eran 48 imágenes que el script renderizaba una por una. Aquí Blender anima la vuelta
solo, con **dos fotogramas clave**, y la guarda **directo en un MP4**. Todo desde la terminal, sin abrir la interfaz.

![Primer cuadro del giro](giro.png)

## Los dos comandos

En una carpeta con [`pieza.py`](pieza.py) y [`giro.py`](giro.py):

```bash
blender -b -P pieza.py
blender -b -P giro.py
```

| Comando | Qué hace |
|---|---|
| `blender -b -P pieza.py` | Crea la pieza de práctica (la cabeza de mono que trae Blender), la suaviza y la guarda en `pieza.stl`, en milímetros |
| `blender -b -P giro.py` | Importa `pieza.stl`, le pone material, luz y cámara, anima una vuelta de 360° y la renderiza en `giro.mp4` (4 s, 96 cuadros, 824 × 900) |

`-b` corre Blender sin interfaz y `-P` ejecuta el script de Python. La guía paso a paso, qué hace cada bloque y cómo usar
tu propio modelo están en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Blender 5.3 (descargas directas, sin cuenta) | https://download.blender.org/release/Blender5.3/ |
| Manual de Blender: línea de comandos | https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html |
| Manual de Blender: fotogramas clave | https://docs.blender.org/manual/en/latest/animation/keyframes/introduction.html |
| Manual de Blender: salida de video | https://docs.blender.org/manual/en/latest/render/output/properties/output.html |
| API de Python: `keyframe_insert` | https://docs.blender.org/api/current/bpy.types.bpy_struct.html |
| API de Python: `stl_import` y `stl_export` | https://docs.blender.org/api/current/bpy.ops.wm.html |
| API de Python: video con FFmpeg | https://docs.blender.org/api/current/bpy.types.FFmpegSettings.html |
| Video anterior: E6, Emi en 3D con Blender | [`../e6-emi-en-blender/`](../e6-emi-en-blender/) |

---
Datos verificados el 24 de noviembre de 2026 en el manual, la referencia de Python, las notas de versión y el servidor de
descargas de Blender (versión 5.3). Ayemi no tiene relación con la Fundación Blender.  
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
