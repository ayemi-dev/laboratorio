from build123d import *

largo, ancho, alto = 80, 60, 30  # mm
pared = 2.5
abajo = (Align.CENTER, Align.CENTER, Align.MIN)

with BuildPart() as caja:
    Box(largo, ancho, alto)
    tapa = caja.faces().sort_by(Axis.Z)[-1]
    offset(amount=-pared, openings=tapa)
    with Locations((0, 0, -alto / 2 + pared)):
        with GridLocations(largo - 14, ancho - 14, 2, 2):
            Cylinder(4, alto - 8, align=abajo)
            Cylinder(1.5, alto - 8, align=abajo, mode=Mode.SUBTRACT)

export_stl(caja.part, "caja.stl")
export_step(caja.part, "caja.step")
