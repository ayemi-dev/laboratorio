# Un giro de 360° de tu modelo · guía y comandos

## 1. Ten Blender a la mano

Descarga Blender 5.3 (descarga directa, sin cuenta): https://download.blender.org/release/Blender5.3/

Comprueba que responde:

```bash
blender --version
```

La primera línea debe decir `Blender 5.3.0`. Si la terminal dice que no encuentra `blender`, usa la ruta completa de tu
`blender.exe` (la carpeta donde instalaste o descomprimiste Blender) en lugar de la palabra `blender`, o agrega esa
carpeta al `PATH` de tu terminal.

## 2. La pieza de práctica

En una carpeta con [`pieza.py`](pieza.py) y [`giro.py`](giro.py):

```bash
blender -b -P pieza.py
```

Salida (la línea que imprime el script; los números son los de nuestra corrida):

```text
Medidas (mm): 66.4 x 40.0 x 47.8
```

Deja `pieza.stl` en la carpeta: la cabeza de mono que Blender trae como figura básica, con `size=0.05` (las medidas
reales las imprime el script), suavizada con un modificador de subdivisión (`SUBSURF`, nivel 2) y exportada en milímetros
(`global_scale=1000`). Es solo para practicar el giro; no comprobamos que se pueda imprimir.

## 3. El giro

```bash
blender -b -P giro.py
```

Imprime las mismas medidas y, al terminar, deja `giro.mp4`: 4 segundos, 96 cuadros a 24 por segundo, 824 × 900, H.264.
Cycles renderiza con el procesador; puede tardar varios minutos según tu equipo.

## Qué hace cada bloque de `giro.py`

1. **El modelo:** importa el STL en milímetros (`global_scale=0.001`, porque Blender trabaja en metros), suaviza su
   sombreado, lo centra y lo apoya en el piso, e imprime sus medidas.
2. **Material:** cian `#0BC5EA`, de sRGB a espacio lineal, con rugosidad `0.45`.
3. **Piso y fondo:** grafito `#0E1217`.
4. **Luz de área y cámara fija:** se colocan en función del tamaño de la pieza (`tam`), así sirven para modelos chicos y
   grandes. La cámara mira de frente con una lente de 70 mm.
5. **Una vuelta completa:** dos fotogramas clave en la rotación z: 0° en el cuadro 1 y 360° en el cuadro 97. Como se
   renderizan los cuadros 1 a 96, el último no repite el primero y el video se puede repetir sin salto. La interpolación
   es lineal (`LINEAR`) para que gire parejo; la que Blender usa por omisión es Bézier.
6. **Render:** Cycles en el procesador, 16 muestras con eliminación de ruido, salida de video (`media_type = "VIDEO"`,
   `FFMPEG`) en contenedor MPEG-4 con H.264, y `render(animation=True)` para todo el rango.

## Usa tu propio modelo

- Copia tu STL a la carpeta y cambia `MODELO = "pieza.stl"` en `giro.py` por su nombre. El STL debe estar en milímetros.
- Si la pieza queda muy chica o se sale del cuadro, cambia `ALEJAR` (más grande, más lejos) y `ALTURA`.
- Si sale muy brillante u oscura, cambia el `600` de `luz.data.energy`.
- Para un giro más lento, sube `CUADROS` (por ejemplo `144` son 6 segundos).
- Para otro color, cambia `CIAN` y `GRAFITO` (hexadecimal sRGB).

Fuentes: manual de Blender 5.3 (línea de comandos, figuras básicas, fotogramas clave, salida de video, Cycles) y
referencia de Python 5.3 (`bpy.ops.mesh.primitive_monkey_add`, `bpy.ops.wm.stl_export` y `stl_import`,
`bpy.types.bpy_struct.keyframe_insert`, `PreferencesEdit.keyframe_new_interpolation_type`, `ImageFormatSettings`,
`FFmpegSettings`, `bpy.ops.render.render`), consultados el 24 de noviembre de 2026.
