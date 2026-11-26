# Mide un STL sin instalar nada: medidas de la caja que lo envuelve y número de caras (triángulos).
#   python medir_stl.py organizador-6.stl organizador-8.stl
# Sirve para STL binario (el que exporta Tinkercad) y de texto.
import struct
import sys


def vertices(datos):
    """Los vértices del STL, sea binario o de texto."""
    if len(datos) >= 84:
        n = struct.unpack("<I", datos[80:84])[0]
        if len(datos) == 84 + 50 * n:
            for i in range(n):
                base = 84 + 50 * i + 12
                for k in range(3):
                    yield struct.unpack("<3f", datos[base + 12 * k:base + 12 * k + 12])
            return
    for linea in datos.decode("utf-8", "replace").splitlines():
        partes = linea.split()
        if partes[:1] == ["vertex"]:
            yield tuple(float(v) for v in partes[1:4])


for ruta in sys.argv[1:]:
    with open(ruta, "rb") as archivo:
        puntos = list(vertices(archivo.read()))
    if not puntos:
        print(f"{ruta}: no tiene triángulos")
        continue
    medidas = [max(p[e] for p in puntos) - min(p[e] for p in puntos) for e in range(3)]
    print(f"{ruta}: {medidas[0]:.1f} x {medidas[1]:.1f} x {medidas[2]:.1f} mm, {len(puntos) // 3} caras")
