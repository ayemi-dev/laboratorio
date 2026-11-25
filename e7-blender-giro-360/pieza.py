# Pieza de práctica: la cabeza de mono que trae Blender, suavizada.
#   blender -b -P pieza.py          da pieza.stl (en milímetros)
import os

import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)

bpy.ops.mesh.primitive_monkey_add(size=0.05)
pieza = bpy.context.active_object
pieza.modifiers.new("suave", "SUBSURF").levels = 2
bpy.ops.object.modifier_apply(modifier="suave")

bpy.ops.wm.stl_export(filepath=os.path.abspath("pieza.stl"), global_scale=1000)
print("Medidas (mm): {} x {} x {}".format(*[round(d * 1000, 1) for d in pieza.dimensions]))
