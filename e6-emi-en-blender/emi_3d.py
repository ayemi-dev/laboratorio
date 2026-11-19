# Emi en 3D con Blender, sin interfaz.
#   blender -b -P emi_3d.py          da emi.stl, emi.glb y emi.png
#   blender -b -P emi_3d.py -- giro  da giro/00.png ... giro/47.png
import math
import os
import re
import sys

import bpy
from mathutils import Vector

ALTO = 80.0     # alto de Emi, en milímetros
RELIEVE = 2.0   # lo que sobresale Emi de la placa, en milímetros
PLACA = 2.0     # grosor de la placa, en milímetros
MARGEN = 10.0   # borde de la placa: más que el área de protección de Emi (9.2 mm)
MM = 0.001      # Blender trabaja en metros

CARCASA = "#F4F7FA"   # Grafito 050 de Ayemi: la carcasa de Emi
GRAFITO = "#0E1217"   # Grafito 900 de Ayemi: la placa
FONDO = "#24282E"     # Grafito 700 de Ayemi: piso y fondo


def lineal(hexa):
    """Color sRGB de la marca al espacio lineal de Blender."""
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return tuple(x / 12.92 if min(x, 0.04045) == x else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


def nodo(dueno, tipo):
    """Primer nodo de un tipo en el árbol de un material o un mundo."""
    if dueno.node_tree is None:
        dueno.use_nodes = True
    return next(n for n in dueno.node_tree.nodes if n.type == tipo)


def material(nombre, hexa, rugosidad):
    mat = bpy.data.materials.new(nombre)
    bsdf = nodo(mat, "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = lineal(hexa)
    bsdf.inputs["Roughness"].default_value = rugosidad
    return mat


def solido(nombre, anillos, z0, grueso, mat):
    """Curva 2D rellena (los contornos de adentro quedan huecos), extruida y vuelta malla."""
    curva = bpy.data.curves.new(nombre, "CURVE")
    curva.dimensions = "2D"
    curva.fill_mode = "BOTH"
    curva.fill_solver = "CDT"
    curva.fill_rule = "EVEN_ODD"
    curva.extrude = grueso / 2
    for anillo in anillos:
        tramo = curva.splines.new("POLY")
        tramo.points.add(len(anillo) - 1)
        for punto, (x, y) in zip(tramo.points, anillo):
            punto.co = (x, y, 0, 1)
        tramo.use_cyclic_u = True
    curva.materials.append(mat)
    objeto = bpy.data.objects.new(nombre, curva)
    objeto.location.z = z0 + grueso / 2
    bpy.context.scene.collection.objects.link(objeto)
    bpy.context.view_layer.objects.active = objeto
    objeto.select_set(True)
    bpy.ops.object.convert(target="MESH")
    objeto.select_set(False)
    return objeto


bpy.ops.wm.read_factory_settings(use_empty=True)
escena = bpy.context.scene

# 1. Emi: su versión de una tinta, del manual de marca de Ayemi
svg = open("emi-serigrafia-blanco.svg", encoding="utf-8").read()
ancho, alto = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
k = ALTO / alto * MM
anillos = []
for ruta in re.findall(r"M ([^MZ]+) Z", re.search(r' d="([^"]+)"', svg).group(1)):
    v = [float(n) for n in ruta.replace("L", " ").split()]
    anillos.append([((x - ancho / 2) * k, (alto / 2 - y) * k) for x, y in zip(v[0::2], v[1::2])])
print(f"Contornos: {len(anillos)}")

# 2. La placa: un rectángulo con esquinas redondas alrededor de Emi
mx, my, r = ancho / 2 * k + MARGEN * MM, alto / 2 * k + MARGEN * MM, MARGEN * MM
esquinas = [(mx - r, my - r, 0), (r - mx, my - r, 90), (r - mx, r - my, 180), (mx - r, r - my, 270)]
borde = [(cx + r * math.cos(math.radians(a + 10 * i)), cy + r * math.sin(math.radians(a + 10 * i)))
         for cx, cy, a in esquinas for i in range(10)]
placa = solido("placa", [borde], 0, PLACA * MM, material("placa", GRAFITO, 0.6))
emi = solido("emi", anillos, PLACA * MM, RELIEVE * MM, material("carcasa", CARCASA, 0.5))

# 3. Una sola pieza, acostada: el STL para imprimir, en milímetros
placa.select_set(True)
emi.select_set(True)
bpy.context.view_layer.objects.active = placa
bpy.ops.object.join()
pieza = placa
pieza.name = "emi"
bpy.context.view_layer.update()
print("Medidas (mm): {} x {} x {}".format(*[round(d / MM, 1) for d in pieza.dimensions]))
bpy.ops.wm.stl_export(filepath=os.path.abspath("emi.stl"), export_selected_objects=True, global_scale=1000)

# 4. De pie y de frente: el GLB, con su color
pieza.rotation_euler.x = math.radians(90)
pieza.location.z = my
bpy.context.view_layer.update()
bpy.ops.export_scene.gltf(filepath=os.path.abspath("emi.glb"), export_format="GLB", use_selection=True)

# 5. Piso y fondo
malla = bpy.data.meshes.new("piso")
malla.from_pydata([(-2, -2, 0), (2, -2, 0), (2, 2, 0), (-2, 2, 0)], [], [(0, 1, 2, 3)])
piso = bpy.data.objects.new("piso", malla)
escena.collection.objects.link(piso)
malla.materials.append(material("piso", FONDO, 0.8))
escena.world = bpy.data.worlds.new("fondo")
nodo(escena.world, "BACKGROUND").inputs["Color"].default_value = lineal(FONDO)
centro = Vector((0, 0, my))


def apuntar(objeto, posicion):
    objeto.location = posicion
    objeto.rotation_euler = (centro - posicion).to_track_quat("-Z", "Y").to_euler()


# 6. Luz de área y cámara
luz = bpy.data.objects.new("luz", bpy.data.lights.new("luz", "AREA"))
luz.data.energy = 2
luz.data.size = 0.25
escena.collection.objects.link(luz)
apuntar(luz, centro + Vector((-0.25, -0.30, 0.20)))

camara = bpy.data.objects.new("camara", bpy.data.cameras.new("camara"))
camara.data.lens = 70
escena.collection.objects.link(camara)
escena.camera = camara
RADIO, ALTURA = 0.28, 0.04
FRENTE = -math.pi / 2


def camara_en(angulo):
    apuntar(camara, centro + Vector((RADIO * math.cos(angulo), RADIO * math.sin(angulo), ALTURA)))


# 7. Render con Cycles, en el procesador
escena.render.engine = "CYCLES"
escena.cycles.device = "CPU"
escena.cycles.use_denoising = True
escena.view_settings.view_transform = "Standard"
escena.render.resolution_x = 824
escena.render.resolution_y = 900
escena.render.resolution_percentage = 100

argumentos = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if "giro" in argumentos:
    escena.cycles.samples = 32
    for i in range(48):
        camara_en(FRENTE + math.radians(35) * math.sin(2 * math.pi * i / 48))
        escena.render.filepath = os.path.abspath(f"giro/{i:02d}.png")
        bpy.ops.render.render(write_still=True)
else:
    escena.cycles.samples = 64
    camara_en(FRENTE + math.radians(20))
    escena.render.filepath = os.path.abspath("emi.png")
    bpy.ops.render.render(write_still=True)
