# Emi en 3D con Blender, y te lo regalamos

Parte de la versión de una tinta de Emi ([`emi-serigrafia-blanco.svg`](emi-serigrafia-blanco.svg)) en [Blender](https://docs.blender.org/manual/en/latest/getting_started/about/index.html) 5.3.0 (licencia GPL; lo que creas con Blender no queda bajo la GPL; Windows, macOS y Linux, sin cuenta) y genera una placa con Emi en relieve en [`emi.stl`](emi.stl) (para imprimir), [`emi.glb`](emi.glb) (glTF 2.0 binario con color) y [`emi.png`](emi.png) (render con Cycles desde la terminal, sin abrir la interfaz gráfica y usando el procesador `CPU`).

![Render de muestra de Emi en Blender](emi.png)

## Instalar

Descarga Blender 5.3.0 (descarga directa, sin cuenta): https://download.blender.org/release/Blender5.3/

En Windows puedes instalarlo desde la terminal con:

```bash
winget install --id=BlenderFoundation.Blender -e
```

Si `blender` no queda en el `PATH` del sistema, llámalo con la ruta completa a `blender.exe` dentro de la carpeta donde se instaló o extrajo Blender (por ejemplo `"C:\Program Files\Blender Foundation\Blender 5.3\blender.exe"` o la ruta de tu paquete portátil).

## Usar

Coloca [`emi_3d.py`](emi_3d.py) y [`emi-serigrafia-blanco.svg`](emi-serigrafia-blanco.svg) en la misma carpeta y ejecuta:

```bash
blender -b -P emi_3d.py
```

Esto genera `emi.stl`, `emi.glb` y `emi.png` (824 × 900, 64 muestras en Cycles sobre CPU), e imprime el número de contornos (`Contornos: 12`) y las medidas reales de la pieza (`Medidas (mm): 70.1 x 100.0 x 4.0`).

Para renderizar el vaivén de 48 cuadros de lado a lado en la carpeta `giro/` (`giro/00.png` a `giro/47.png`, 32 muestras):

```bash
blender -b -P emi_3d.py -- giro
```

## Qué hace cada bloque de `emi_3d.py`

1. **Emi (`# 1. Emi: su versión de una tinta, del manual de marca de Ayemi`):** limpia la escena inicial, lee el `viewBox` y los 12 contornos del SVG (`M ... Z`) y los escala a milímetros para que Emi mida `ALTO = 80.0` mm.
2. **La placa (`# 2. La placa: un rectángulo con esquinas redondas alrededor de Emi`):** construye la placa base con esquinas redondeadas dejando `MARGEN = 10.0` mm alrededor de Emi y convierte tanto la placa (`PLACA = 2.0` mm) como a Emi (`RELIEVE = 2.0` mm) en mallas extruyendo curvas 2D con regla par-impar (`fill_rule = "EVEN_ODD"`, para que pantalla, visera, sensor, auriculares y núcleo queden huecos).
3. **STL para imprimir (`# 3. Una sola pieza, acostada: el STL para imprimir, en milímetros`):** une placa y relieve en un solo objeto, imprime `Medidas (mm)` y exporta `emi.stl` en milímetros (`global_scale=1000`).
4. **GLB con color (`# 4. De pie y de frente: el GLB, con su color`):** levanta la pieza 90 grados sobre X y exporta `emi.glb` en formato binario glTF 2.0.
5. **Piso y fondo (`# 5. Piso y fondo`):** agrega el plano de piso y el mundo en grafito `#24282E`.
6. **Luz de área y cámara (`# 6. Luz de área y cámara`):** coloca una luz `AREA` (`energy = 2`, `size = 0.25`) y una cámara de `70` mm (`RADIO = 0.28` m, `ALTURA = 0.04` m) apuntando al centro de Emi.
7. **Render con Cycles (`# 7. Render con Cycles, en el procesador`):** configura `CYCLES` en `CPU` con denoising activado, resolución 824 × 900 y lee los argumentos después de `--` para renderizar `emi.png` (64 muestras) o los 48 cuadros en `giro/` (32 muestras).

### Cómo cambiar las medidas, la luz o la cámara

- **Medidas de la pieza:** ajusta las constantes `ALTO` (alto de Emi en mm), `RELIEVE` (altura del relieve en mm), `PLACA` (grosor de la placa en mm) y `MARGEN` (borde de la placa en mm) al inicio del script.
- **Colores:** cambia `CARCASA`, `GRAFITO` y `FONDO` (en formato hexadecimal sRGB).
- **Luz:** ajusta `luz.data.energy` (intensidad) o `luz.data.size` (suavidad de la sombra).
- **Cámara:** cambia `camara.data.lens` (distancia focal en mm), `RADIO` (distancia horizontal al centro en metros) y `ALTURA` (altura en metros).

### Sugerencia para imprimir en dos colores

Si tu impresora lo permite, puedes imprimir la placa en dos colores cambiando el filamento al llegar a los **2 mm** de altura (donde termina la placa base y empieza el relieve de Emi).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Blender 5.3 (descargas directas) | https://download.blender.org/release/Blender5.3/ |
| Manual de Blender: línea de comandos | https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html |
| API de Python: `bpy.types.Curve` | https://docs.blender.org/api/current/bpy.types.Curve.html |
| API de Python: `bpy.ops.wm` (`stl_export`) | https://docs.blender.org/api/current/bpy.ops.wm.html |
| API de Python: `bpy.ops.export_scene` (`gltf`) | https://docs.blender.org/api/current/bpy.ops.export_scene.html |
| Cycles y render en CPU/GPU | https://docs.blender.org/manual/en/latest/render/cycles/index.html |
| Licencia CC BY-NC-ND 4.0 | https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es |

## Licencia de Emi

Los archivos de Emi (`emi.stl`, `emi.glb`, `emi.png` y `emi-serigrafia-blanco.svg`) se publican bajo **CC BY-NC-ND 4.0** (uso personal, con atribución, sin fines comerciales y sin distribuir versiones modificadas). Consulta [`LICENCIA-EMI.md`](LICENCIA-EMI.md) para ver los detalles completos y la atribución sugerida.

El script [`emi_3d.py`](emi_3d.py) se publica bajo la licencia **MIT** ([`../LICENSE`](../LICENSE)).

---
Datos verificados el 19 de noviembre de 2026 en la referencia de Python, el manual, las notas de versión y el servidor de descargas de Blender, y en la página de la licencia de Creative Commons. Ayemi no tiene relación con la Fundación Blender ni con Creative Commons.  
¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
