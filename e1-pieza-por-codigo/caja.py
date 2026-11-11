from build123d import *

largo, ancho, alto = 80, 60, 30  # mm
pared = 2.5
poste = alto - 8
z = pared - alto / 2 + poste / 2
hueco = Mode.SUBTRACT

with BuildPart() as caja:
    Box(largo, ancho, alto)
    tapa = caja.faces().sort_by(Axis.Z)[-1]
    offset(amount=-pared, openings=tapa)
    puntos = (largo - 14, ancho - 14, 2, 2)
    with Locations((0, 0, z)):
        with GridLocations(*puntos):
            Cylinder(4, poste)
            Cylinder(1.5, poste, mode=hueco)

export_stl(caja.part, "caja.stl")
export_step(caja.part, "caja.step")
