"""Dibuja el gatito bailarín de Ayemi y lo convierte en cuadros de bits para una OLED de 128 x 64.

El gatito es un dibujo original hecho solo con código: círculos, triángulos y líneas.
No usa ninguna imagen, GIF ni sprite de nadie.

Uso:
    python cuadros.py              escribe src/cuadros.h
    python cuadros.py --vista 0    además muestra el cuadro 0 en la terminal
    python cuadros.py --png vista  además guarda un PNG por cuadro en la carpeta vista (requiere Pillow)

Solo usa la biblioteca estándar de Python (Pillow solo para --png).
"""

import argparse
import math
from pathlib import Path

ANCHO, ALTO = 128, 64
NUM_CUADROS = 8


# ---------------------------------------------------------------- lienzo de 1 bit

def lienzo():
    return [[0] * ANCHO for _ in range(ALTO)]


def punto(img, x, y, valor=1):
    x, y = int(round(x)), int(round(y))
    if 0 <= x < ANCHO and 0 <= y < ALTO:
        img[y][x] = valor


def elipse(img, cx, cy, rx, ry, valor=1):
    for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                punto(img, x, y, valor)


def circulo(img, cx, cy, r, valor=1):
    elipse(img, cx, cy, r, r, valor)


def triangulo(img, a, b, c, valor=1):
    xs = [a[0], b[0], c[0]]
    ys = [a[1], b[1], c[1]]

    def lado(p, q, x, y):
        return (q[0] - p[0]) * (y - p[1]) - (q[1] - p[1]) * (x - p[0])

    for y in range(int(min(ys)), int(max(ys)) + 1):
        for x in range(int(min(xs)), int(max(xs)) + 1):
            d1, d2, d3 = lado(a, b, x, y), lado(b, c, x, y), lado(c, a, x, y)
            negativo = d1 < 0 or d2 < 0 or d3 < 0
            positivo = d1 > 0 or d2 > 0 or d3 > 0
            if not (negativo and positivo):
                punto(img, x, y, valor)


def linea(img, x0, y0, x1, y1, grosor=1, valor=1):
    pasos = int(max(abs(x1 - x0), abs(y1 - y0))) * 2 + 1
    for i in range(pasos + 1):
        t = i / pasos
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        if grosor <= 1:
            punto(img, x, y, valor)
        else:
            circulo(img, x, y, grosor / 2, valor)


# ---------------------------------------------------------------- el gatito

def gatito(n):
    """Cuadro n del baile: el cuerpo rebota, la cabeza se ladea y las patas se turnan."""
    img = lienzo()
    fase = 2 * math.pi * n / NUM_CUADROS
    rebote = round(2 * abs(math.sin(fase)))      # 0 a 2 puntos hacia arriba
    ladeo = round(3 * math.sin(fase))            # -3 a 3 puntos de lado
    cx = 64 + round(2 * math.sin(fase))          # vaivén de lado a lado
    piso = 60

    # piso: una línea punteada
    for x in range(8, 120, 4):
        punto(img, x, piso + 2)

    # cola: una curva de círculos que se mece
    for i in range(14):
        t = i / 13
        x = cx + 13 + 17 * t
        y = piso - 4 - rebote - 14 * t * t + 4 * math.sin(fase + t * 3) * t
        circulo(img, x, y, 1.6)

    # cuerpo
    cuerpo_y = piso - 12 - rebote
    elipse(img, cx, cuerpo_y, 12, 10)
    elipse(img, cx, cuerpo_y + 2, 6, 6, 0)       # panza hueca
    elipse(img, cx, cuerpo_y + 2, 4, 4)          # panza

    # patas de abajo
    for lado_x in (-6, 6):
        linea(img, cx + lado_x, cuerpo_y + 8, cx + lado_x, piso, grosor=3)
        elipse(img, cx + lado_x, piso, 3, 1.5)

    # brazos: uno arriba y otro abajo, y se turnan
    hombro_y = cuerpo_y - 5
    arriba = math.sin(fase) >= 0
    for signo in (-1, 1):
        levanta = arriba if signo < 0 else not arriba
        hx = cx + signo * 10
        if levanta:
            mx, my = cx + signo * 20, hombro_y - 12
        else:
            mx, my = cx + signo * 15, hombro_y + 10
        linea(img, hx, hombro_y, mx, my, grosor=3)
        circulo(img, mx, my, 2.5)

    # cabeza
    hx, hy = cx + ladeo, cuerpo_y - 19
    circulo(img, hx, hy, 11)
    triangulo(img, (hx - 10, hy - 4), (hx - 9, hy - 17), (hx - 2, hy - 9))   # oreja izquierda
    triangulo(img, (hx + 10, hy - 4), (hx + 9, hy - 17), (hx + 2, hy - 9))   # oreja derecha
    triangulo(img, (hx - 8, hy - 6), (hx - 8, hy - 12), (hx - 4, hy - 8), 0)
    triangulo(img, (hx + 8, hy - 6), (hx + 8, hy - 12), (hx + 4, hy - 8), 0)

    # cara: ojos, nariz, boca y bigotes (en negro sobre la cabeza)
    if n % 4 == 3:                                # parpadeo
        linea(img, hx - 6, hy - 1, hx - 2, hy - 1, valor=0)
        linea(img, hx + 2, hy - 1, hx + 6, hy - 1, valor=0)
    else:
        elipse(img, hx - 4, hy - 1, 2, 3, 0)
        elipse(img, hx + 4, hy - 1, 2, 3, 0)
    triangulo(img, (hx - 1, hy + 3), (hx + 1, hy + 3), (hx, hy + 4), 0)
    punto(img, hx - 1, hy + 6, 0)
    punto(img, hx + 1, hy + 6, 0)
    punto(img, hx, hy + 5, 0)
    for dy in (2, 5):
        linea(img, hx - 10, hy + dy, hx - 5, hy + dy + 1, valor=0)
        linea(img, hx + 5, hy + dy + 1, hx + 10, hy + dy, valor=0)

    # notas musicales que suben de lado y lado
    for k, base_x in enumerate((14, 104)):
        ny = 30 - ((n * 3 + k * 12) % 24)
        circulo(img, base_x, ny + 6, 2.2)
        linea(img, base_x + 2, ny + 6, base_x + 2, ny)
        linea(img, base_x + 2, ny, base_x + 5, ny + 2)

    return img


# ---------------------------------------------------------------- conversión a bits

def a_bytes(img):
    """Cada fila de 128 puntos son 16 bytes; el primer punto de cada byte es su bit más alto."""
    salida = []
    for fila in img:
        for x in range(0, ANCHO, 8):
            byte = 0
            for bit in fila[x:x + 8]:
                byte = (byte << 1) | bit
            salida.append(byte)
    return salida


def escribir_h(cuadros_bytes, ruta):
    lineas = [
        "// Generado por cuadros.py: no lo edites a mano.",
        "// El gatito bailarín de Ayemi, un dibujo original hecho con código.",
        f"// {len(cuadros_bytes)} cuadros de {ANCHO} x {ALTO} puntos, 1 bit por punto: "
        f"{ANCHO * ALTO // 8} bytes por cuadro.",
        "#pragma once",
        "#include <Arduino.h>",
        "",
        f"const uint8_t NUM_CUADROS = {len(cuadros_bytes)};",
        "",
        f"const uint8_t cuadros[NUM_CUADROS][{ANCHO * ALTO // 8}] PROGMEM = {{",
    ]
    for n, datos in enumerate(cuadros_bytes):
        lineas.append(f"  {{ // cuadro {n}")
        for i in range(0, len(datos), 16):
            lineas.append("    " + ", ".join(f"0x{b:02X}" for b in datos[i:i + 16]) + ",")
        lineas.append("  },")
    lineas.append("};")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8", newline="\n")


def vista(img):
    for fila in img:
        print("".join("#" if p else "." for p in fila))


def guardar_png(imagenes, carpeta):
    from PIL import Image

    carpeta.mkdir(parents=True, exist_ok=True)
    for n, img in enumerate(imagenes):
        png = Image.new("1", (ANCHO, ALTO))
        png.putdata([p for fila in img for p in fila])
        png.save(carpeta / f"cuadro-{n}.png")


def main():
    parser = argparse.ArgumentParser(description="Gatito bailarín de Ayemi en cuadros de bits.")
    parser.add_argument("--vista", type=int, metavar="N", help="muestra el cuadro N en la terminal")
    parser.add_argument("--png", metavar="CARPETA", help="guarda un PNG por cuadro (requiere Pillow)")
    args = parser.parse_args()

    imagenes = [gatito(n) for n in range(NUM_CUADROS)]
    cuadros_bytes = [a_bytes(img) for img in imagenes]
    ruta = Path(__file__).parent / "src" / "cuadros.h"
    escribir_h(cuadros_bytes, ruta)

    total = sum(len(c) for c in cuadros_bytes)
    print(f"{NUM_CUADROS} cuadros de {ANCHO} x {ALTO} puntos")
    print(f"{ANCHO * ALTO // 8} bytes por cuadro, {total} en total")
    print(f"escrito: src/cuadros.h")

    if args.vista is not None:
        vista(imagenes[args.vista % NUM_CUADROS])
    if args.png:
        guardar_png(imagenes, Path(args.png))


if __name__ == "__main__":
    main()
