# De tu circuito a una placa real con KiCad

[KiCad](https://www.kicad.org/) es software libre y de código abierto (GPL v3) para diseñar placas electrónicas. Funciona en Windows, macOS y Linux.

## Los 5 pasos del video

1. **Esquemático** (*Schematic Editor*): los componentes y cómo se conectan. El revisor eléctrico (*ERC*) avisa si algo quedó suelto.
2. **Placa** (*PCB Editor*): importas el esquemático (*Update PCB from Schematic*), acomodas las huellas y trazas las pistas.
3. **Reglas de diseño** (*DRC*): confirma que la placa se pueda fabricar.
4. **Visor 3D**: ves cómo quedará antes de mandarla a hacer.
5. **Fabricación**: exportas los Gerber (*Plot*) y los taladros (*Generate Drill Files*), que es lo que pide el fabricante.

## La placa del video

Es **RoyalBlue54L Feather**, uno de los proyectos de ejemplo que se instalan con KiCad 10 (carpeta `demos`), con licencia CERN-OHL-P. Las imágenes se generaron con la línea de comandos de KiCad, por ejemplo:

```bash
kicad-cli sch export svg -o sch RoyalBlue54L-Feather.kicad_sch
kicad-cli pcb render -o placa.png --rotate "-45,0,45" --quality high RoyalBlue54L-Feather.kicad_pcb
kicad-cli pcb export gerbers -o gerber/ RoyalBlue54L-Feather.kicad_pcb
kicad-cli pcb export drill -o gerber/ RoyalBlue54L-Feather.kicad_pcb
```

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Descarga de KiCad | https://www.kicad.org/download/ |
| Guía oficial para empezar (KiCad 10) | https://docs.kicad.org/10.0/en/getting_started_in_kicad/getting_started_in_kicad.html |
| Licencias de KiCad | https://www.kicad.org/about/licenses/ |

Datos verificados el 11 de noviembre de 2026 en kicad.org (KiCad 10.0.8). Ayemi no tiene relación con KiCad.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tu prototipo necesita su propia placa? Lo construimos: https://ayemi.org/enlaces
