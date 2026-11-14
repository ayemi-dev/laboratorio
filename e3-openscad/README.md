# Un soporte para celular creado con código (OpenSCAD)

Un soporte de escritorio para tu celular, escrito en [OpenSCAD](https://openscad.org/): un programa de CAD libre en el que no se dibuja con el ratón, sino que se escribe un script y OpenSCAD lo convierte en un sólido. Lo ajustas a tu celular cambiando tres números.

## Instalar

OpenSCAD 2021.01 (la versión estable): https://openscad.org/downloads.html

En Windows también se instala con:

```bash
winget install --id=OpenSCAD.OpenSCAD -e
```

## Usar

1. Abre [`soporte.scad`](soporte.scad) en OpenSCAD.
2. Cambia los parámetros del inicio (en milímetros y grados), en el código o en el panel **Customizer**, que los muestra como controles (si no lo ves, desmarca *Window › Hide Customizer*):
   - `grosor_cel`: grosor de tu celular **con funda**, de 6 a 16 mm.
   - `ancho`: ancho del soporte, de 50 a 100 mm.
   - `angulo`: inclinación del respaldo respecto a la mesa, de 50 a 80 grados.
   - `ranura_cable`: deja o quita la ranura del cable de carga.
3. Pulsa **Render** (F6) y exporta a STL (F7) para imprimir.

Desde la terminal, sin abrir la ventana:

```bash
openscad -o soporte.stl soporte.scad
openscad -o soporte.stl -D angulo=50 -D grosor_cel=15 soporte.scad
```

## Cómo está hecho

- `perfil()` dibuja el perfil en 2D: base, labio del frente, respaldo inclinado y un apoyo. `offset()` redondea las esquinas e `intersection()` recorta lo que quedaría bajo el piso.
- `linear_extrude()` lo extruye al ancho y `difference()` le resta la ranura del cable.
- Con los valores del archivo mide 65 × 70 × 81 mm.

## Notas

- Imprímelo acostado sobre un costado (el perfil sobre la cama): así no necesita soportes y las capas corren a lo largo del respaldo.
- Si tu celular entra muy justo, suma medio milímetro a `grosor_cel`.
- OpenSCAD exporta a STL, 3MF, OFF y otros formatos, pero no a STEP. Si necesitas STEP para otro programa de CAD, mira el gabinete del video anterior, hecho en Python con build123d.
- OpenSCAD es software libre con licencia GPL v2. Ayemi no tiene relación con OpenSCAD.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| OpenSCAD (descargas) | https://openscad.org/downloads.html |
| Manual del Customizer | https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Customizer |
| Video anterior: un gabinete con build123d | [`../e2-gabinete-por-codigo/`](../e2-gabinete-por-codigo/) |

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
