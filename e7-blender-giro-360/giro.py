# Un giro de 360° de tu modelo, sin abrir la interfaz de Blender.
#   blender -b -P giro.py           da giro.mp4 (4 s, 96 cuadros)
import math
import os

import bpy
from mathutils import Vector

MODELO = "pieza.stl"    # tu STL, en milímetros
CIAN = "#0BC5EA"        # Cian 500 de Ayemi
GRAFITO = "#0E1217"     # Grafito 900 de Ayemi
CUADROS = 96            # 4 segundos a 24 cuadros por segundo
ALEJAR, ALTURA = 3.5, 0.8   # cámara, en tamaños de la pieza


def lineal(hexa):
    """Color sRGB de la marca al espacio lineal de Blender."""
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return tuple(x / 12.92 if min(x, 0.04045) == x else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


def nodo(dueno, tipo):
    """Primer nodo de un tipo en el árbol de un material o un mundo."""
    if dueno.node_tree is None:
        dueno.use_nodes = True
    return next(n for n in dueno.node_tree.nodes if n.type == tipo)


def apuntar(objeto, posicion):
    objeto.location = posicion
    objeto.rotation_euler = (centro - posicion).to_track_quat("-Z", "Y").to_euler()


bpy.ops.wm.read_factory_settings(use_empty=True)
escena = bpy.context.scene

# 1. El modelo: el STL, centrado y apoyado en el piso
antes = set(bpy.data.objects)
bpy.ops.wm.stl_import(filepath=os.path.abspath(MODELO), global_scale=0.001)
pieza = (set(bpy.data.objects) - antes).pop()
pieza.data.shade_smooth()
bpy.context.view_layer.objects.active = pieza
pieza.select_set(True)
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
pieza.location = (0, 0, pieza.dimensions.z / 2)
bpy.context.view_layer.update()
print("Medidas (mm): {} x {} x {}".format(*[round(d * 1000, 1) for d in pieza.dimensions]))
centro = Vector((0, 0, pieza.dimensions.z / 2))
tam = max(pieza.dimensions)

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

# 4. Luz de área y cámara fija
luz = bpy.data.objects.new("luz", bpy.data.lights.new("luz", "AREA"))
luz.data.energy = 600 * tam ** 2
luz.data.size = 3 * tam
escena.collection.objects.link(luz)
apuntar(luz, centro + Vector((-3.0, -3.6, 4.2)) * tam)

camara = bpy.data.objects.new("camara", bpy.data.cameras.new("camara"))
camara.data.lens = 70
escena.collection.objects.link(camara)
escena.camera = camara
apuntar(camara, centro + Vector((0, -ALEJAR, ALTURA)) * tam)

# 5. Una vuelta completa: dos fotogramas clave
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
escena.render.fps = 24
escena.frame_start = 1
escena.frame_end = CUADROS
pieza.rotation_euler.z = 0
pieza.keyframe_insert("rotation_euler", index=2, frame=1)
pieza.rotation_euler.z = math.radians(360)
pieza.keyframe_insert("rotation_euler", index=2, frame=CUADROS + 1)

# 6. Render con Cycles, en el procesador, directo a MP4
escena.render.engine = "CYCLES"
escena.cycles.device = "CPU"
escena.cycles.samples = 16
escena.cycles.use_denoising = True
escena.view_settings.view_transform = "Standard"
escena.render.resolution_x = 824
escena.render.resolution_y = 900
escena.render.resolution_percentage = 100
escena.render.image_settings.media_type = "VIDEO"
escena.render.image_settings.file_format = "FFMPEG"
escena.render.ffmpeg.format = "MPEG4"
escena.render.ffmpeg.codec = "H264"
escena.render.ffmpeg.constant_rate_factor = "PERC_LOSSLESS"
escena.render.filepath = os.path.abspath("giro.mp4")
bpy.ops.render.render(animation=True)
