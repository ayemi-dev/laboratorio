# Render del soporte de E3 en Blender, sin interfaz.
#   blender -b -P render.py          -> soporte.png
#   blender -b -P render.py -- giro  -> giro/00.png ... giro/47.png
import math
import os
import sys

import bpy
from mathutils import Vector

CIAN = "#0BC5EA"     # Cian 500 de Ayemi
GRAFITO = "#0E1217"  # Grafito 900 de Ayemi


def lineal(hexa):
    """Color sRGB de la marca al espacio lineal de Blender."""
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


def nodo(dueno, tipo):
    """Primer nodo de un tipo en el árbol de un material o un mundo."""
    if dueno.node_tree is None:
        dueno.use_nodes = True
    return next(n for n in dueno.node_tree.nodes if n.type == tipo)


bpy.ops.wm.read_factory_settings(use_empty=True)
escena = bpy.context.scene

# 1. La pieza: el STL de E3, en milímetros
antes = set(bpy.data.objects)
bpy.ops.wm.stl_import(filepath=os.path.abspath("soporte.stl"), global_scale=0.001)
pieza = (set(bpy.data.objects) - antes).pop()
bpy.context.view_layer.update()
medidas = [round(d * 1000, 1) for d in pieza.dimensions]
print("Medidas (mm): {} x {} x {}".format(*medidas))
esquinas = [pieza.matrix_world @ Vector(c) for c in pieza.bound_box]
centro = sum(esquinas, Vector()) / 8

# 2. Material: cian de la marca
material = bpy.data.materials.new("cian")
bsdf = nodo(material, "BSDF_PRINCIPLED")
bsdf.inputs["Base Color"].default_value = lineal(CIAN)
bsdf.inputs["Roughness"].default_value = 0.45
pieza.data.materials.append(material)

# 3. Piso y fondo: grafito
malla = bpy.data.meshes.new("piso")
malla.from_pydata([(-2, -2, 0), (2, -2, 0), (2, 2, 0), (-2, 2, 0)], [], [(0, 1, 2, 3)])
piso = bpy.data.objects.new("piso", malla)
escena.collection.objects.link(piso)
mate = bpy.data.materials.new("grafito")
nodo(mate, "BSDF_PRINCIPLED").inputs["Base Color"].default_value = lineal(GRAFITO)
malla.materials.append(mate)
escena.world = bpy.data.worlds.new("fondo")
nodo(escena.world, "BACKGROUND").inputs["Color"].default_value = lineal(GRAFITO)


def apuntar(objeto, posicion):
    objeto.location = posicion
    objeto.rotation_euler = (centro - posicion).to_track_quat("-Z", "Y").to_euler()


# 4. Luz de área
luz = bpy.data.objects.new("luz", bpy.data.lights.new("luz", "AREA"))
luz.data.energy = 4
luz.data.size = 0.25
escena.collection.objects.link(luz)
apuntar(luz, centro + Vector((-0.25, -0.30, 0.35)))

# 5. Cámara
camara = bpy.data.objects.new("camara", bpy.data.cameras.new("camara"))
camara.data.lens = 70
escena.collection.objects.link(camara)
escena.camera = camara
RADIO, ALTO = 0.354, 0.16
GIRO0 = math.atan2(-0.22, -0.28)


def camara_en(angulo):
    apuntar(camara, centro + Vector((RADIO * math.cos(angulo), RADIO * math.sin(angulo), ALTO)))


# 6. Render con Cycles, en el procesador
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
        camara_en(GIRO0 + 2 * math.pi * i / 48)
        escena.render.filepath = os.path.abspath(f"giro/{i:02d}.png")
        bpy.ops.render.render(write_still=True)
else:
    escena.cycles.samples = 64
    camara_en(GIRO0)
    escena.render.filepath = os.path.abspath("soporte.png")
    bpy.ops.render.render(write_still=True)
