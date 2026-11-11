# Una pieza 3D creada solo con código (build123d)

Un gabinete paramétrico con cuatro postes para tornillos, escrito en Python con [build123d](https://build123d.readthedocs.io/en/latest/). Cambias las medidas y el script genera otra versión.

## Instalar

1. Python 3.11 o más reciente: https://www.python.org/downloads/
2. La librería:

```bash
pip install -r requirements.txt
```

## Usar

1. Edita las medidas al inicio de [`caja.py`](caja.py) (en milímetros): `largo`, `ancho`, `alto` y `pared`.
2. Corre:

```bash
python caja.py
```

3. Obtienes `caja.stl` (para imprimir en 3D) y `caja.step` (para abrir en otro programa de CAD).

## Notas

- Los postes quedan a 7 mm de cada esquina exterior, con un barreno de 3 mm. Ajusta `largo - 14` y `ancho - 14` si tu placa tiene otra separación.
- Para ver la pieza mientras la editas, build123d recomienda el visor `ocp_vscode` para VS Code.
- build123d es software libre (licencia Apache 2.0) y usa el núcleo geométrico Open Cascade.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| build123d (documentación) | https://build123d.readthedocs.io/en/latest/ |
| build123d en PyPI | https://pypi.org/project/build123d/ |
| Python | https://www.python.org/downloads/ |

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
