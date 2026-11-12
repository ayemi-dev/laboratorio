from build123d import *

# Mide tu placa (mm). Estas son de ejemplo.
placa_x, placa_y = 52, 28
holgura, pared = 2, 2
alto, tapa_z = 16, 2
usb_w, usb_h, usb_z = 12, 7, 8
poste = pared + 4
hueco = Mode.SUBTRACT
abajo = (Align.CENTER, Align.CENTER, Align.MIN)
largo = placa_x + 2 * (holgura + pared)
ancho = placa_y + 2 * (holgura + pared)
postes = (placa_x - 6, placa_y - 6, 2, 2)

with BuildPart() as base:
    Box(largo, ancho, alto, align=abajo)
    fillet(base.edges().filter_by(Axis.Z), 3)
    arriba = base.faces().sort_by(Axis.Z)[-1]
    offset(amount=-pared, openings=arriba)
    with Locations((0, 0, poste / 2)):
        with GridLocations(*postes):
            Cylinder(3, poste)
            Cylinder(1.2, poste, mode=hueco)
    with Locations((-largo / 2, 0, usb_z)):
        Box(pared * 3, usb_w, usb_h, mode=hueco)

with BuildPart() as tapa:
    with Locations((0, 0, alto)):
        Box(largo, ancho, tapa_z, align=abajo)
    fillet(tapa.edges().filter_by(Axis.Z), 3)
    ceja_x = largo - 2 * (pared + 0.2)
    ceja_y = ancho - 2 * (pared + 0.2)
    with BuildSketch(Plane.XY.offset(alto - 3)):
        RectangleRounded(ceja_x, ceja_y, 1)
        offset(amount=-1.5, mode=hueco)
    extrude(amount=3)
    with Locations((0, 0, alto)):
        with GridLocations(4, 0, 9, 1):
            Box(2, ancho / 2, 10, mode=hueco)

gabinete = Compound([base.part, tapa.part])
export_stl(base.part, "base.stl")
export_stl(tapa.part, "tapa.stl")
export_step(gabinete, "gabinete.step")
