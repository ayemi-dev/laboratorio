# Un gabinete de dos piezas creado con código (build123d)

Base y tapa para una placa de desarrollo, escritas en Python con [build123d](https://build123d.readthedocs.io/en/latest/). La base trae esquinas redondeadas, cuatro postes para tornillos y un hueco para el cable USB; la tapa trae una ceja que entra en la base y una rejilla de ventilación. Todo sale de las medidas de tu placa.

## Instalar

1. Python 3.11 o más reciente: https://www.python.org/downloads/
2. La librería:

```bash
pip install -r requirements.txt
```

## Usar

1. **Mide tu placa** y edita las medidas al inicio de [`gabinete.py`](gabinete.py) (en milímetros). Las que trae son de ejemplo:
   - `placa_x`, `placa_y`: largo y ancho de la placa.
   - `holgura`, `pared`: espacio alrededor de la placa y grosor de las paredes.
   - `alto`, `tapa_z`: alto de la base y grosor de la tapa.
   - `usb_w`, `usb_h`, `usb_z`: ancho, alto y altura del centro del hueco del USB.
2. Corre:

```bash
python gabinete.py
```

3. Obtienes `base.stl` y `tapa.stl` (para imprimir en 3D) y `gabinete.step` con las dos piezas (para abrir en otro programa de CAD).

## Notas

- La tapa se modela en su lugar, encima de la base. Para imprimirla, voltéala en tu programa de laminado, con la cara plana hacia la cama.
- La ceja queda 0.2 mm por lado más chica que el hueco de la base. Si tu impresora deja las piezas más gruesas, súbelo a 0.3.
- Los postes quedan a 3 mm de las orillas de la placa, con un barreno de 2.4 mm de diámetro que atraviesa el piso: ajústalo a tus tornillos. Ajusta `placa_x - 6` y `placa_y - 6` a los barrenos de tu placa.
- El hueco del USB está en la pared izquierda (eje X negativo). Mídelo en tu placa: su altura depende de los postes y del conector.
- build123d es software libre (licencia Apache 2.0) y usa el núcleo geométrico Open Cascade.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| build123d (documentación) | https://build123d.readthedocs.io/en/latest/ |
| build123d en PyPI | https://pypi.org/project/build123d/ |
| Python | https://www.python.org/downloads/ |
| Video anterior: una caja con cuatro postes | [`../e1-pieza-por-codigo/`](../e1-pieza-por-codigo/) |

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
