# Del STL al G-code con PrusaSlicer

Convierte el archivo `soporte.stl` del video anterior ([`../e3-openscad/`](../e3-openscad/)) en instrucciones G-code listas para imprimir en PLA con [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) 2.9.7 (AGPL v3, Windows, macOS y Linux, sin cuenta).

## Instalar

Descarga PrusaSlicer 2.9.7: https://github.com/prusa3d/PrusaSlicer/releases/latest

En Windows puedes instalarlo desde la terminal con:

```bash
winget install --id=Prusa3D.PrusaSlicer -e
```

Si `prusa-slicer-console` no queda en el `PATH` del sistema, llámalo con la ruta completa a `prusa-slicer-console.exe` dentro de la carpeta donde se instaló o extrajo PrusaSlicer (por ejemplo `"C:\Program Files\Prusa3D\PrusaSlicer\prusa-slicer-console.exe"` o la ruta del paquete portátil).

## Usar

Coloca [`pla.ini`](pla.ini) y `soporte.stl` (de [`../e3-openscad/`](../e3-openscad/)) en la misma carpeta y ejecuta:

```bash
prusa-slicer-console -g --load pla.ini soporte.stl
```

Esto genera `soporte.gcode` (405 capas, sin material de soporte porque la pieza apoya sobre su base y nada empieza en el aire).

Para probar cómo se generan soportes cuando una parte queda en el aire (volteando la pieza 180° en X):

```bash
prusa-slicer-console -g --load pla.ini --rotate-x 180 -o volteado.gcode soporte.stl
```

## Qué hace cada línea de `pla.ini`

- `nozzle_diameter = 0.4` y `filament_diameter = 1.75`: diámetro estándar de boquilla y filamento.
- `layer_height = 0.2` y `first_layer_height = 0.2`: grosor de cada capa (la base de conocimiento de Prusa recomienda mantenerse por debajo del 80 % del diámetro de boquilla).
- `perimeters = 2`: dos líneas exteriores que forman la pared de la pieza.
- `fill_density = 15%` y `fill_pattern = gyroid`: 15 % de relleno interno con patrón giroide (rara vez hace falta más del 30 %).
- `support_material = 1` y `support_material_auto = 1`: activa los soportes automáticos solo si alguna parte de la pieza empieza en el aire.
- `first_layer_temperature = 215` y `temperature = 210`: temperatura de boquilla en °C para PLA (puede variar según la marca de filamento).
- `first_layer_bed_temperature = 60` y `bed_temperature = 60`: temperatura de la cama en °C.

### Cómo ajustar altura de capa o relleno

- Para más detalle (a costa de mayor tiempo de impresión), baja `layer_height` a `0.1` o `0.15`; para acortar el tiempo, súbela (siempre por debajo del 80 % de `nozzle_diameter`).
- Para una pieza más rígida, sube `fill_density` (por ejemplo a `20%` o `25%`).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| STL del soporte (video anterior) | [`../e3-openscad/`](../e3-openscad/) |
| PrusaSlicer (descargas) | https://github.com/prusa3d/PrusaSlicer/releases/latest |
| Capas y perímetros (Prusa KB) | https://help.prusa3d.com/article/layers-and-perimeters_1748 |
| Relleno (Prusa KB) | https://help.prusa3d.com/article/infill_42 |
| Soportes (Prusa KB) | https://help.prusa3d.com/article/support-material_1698 |
| OrcaSlicer (alternativa libre, AGPL v3) | https://github.com/SoftFever/OrcaSlicer |

---
Datos verificados el 16 de noviembre de 2026. Ayemi no tiene relación con Prusa Research ni con OrcaSlicer.  
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
