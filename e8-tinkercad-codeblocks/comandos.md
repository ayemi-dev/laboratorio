# Diseña una pieza 3D con bloques de código en Tinkercad · guía paso a paso

Los nombres de los bloques son los de la interfaz en español. Si tu Tinkercad está en otro idioma, cámbialo en el selector
de idioma del pie de la página.

## 1. Un diseño nuevo de Codeblocks

En tinkercad.com, con tu sesión iniciada: **Crear** → **Codeblocks** → diseño **en blanco** (no una plantilla). Ponle de
nombre `organizador`. Tinkercad lo guarda solo.

## 2. Las variables

En la categoría de variables, **crear variable** tres veces: `huecos`, `diametro` y `x` (sin acento, para copiarlas sin
problema). Arriba de la pila:

```text
fijar huecos a 6
fijar diametro a 10
fijar x a 0
```

`huecos` es cuántos huecos lleva el organizador y `diametro`, su diámetro en milímetros. `x` es la posición de la
siguiente celda.

## 3. El bucle

Debajo, un bloque **repetir** (categoría de control) con la variable `huecos` en el número de veces. Dentro, en este
orden:

| Bloque | Valores | Qué hace |
|---|---|---|
| **caja**, sólida | ancho = `diametro + 6`, largo = `22`, alto = `30` (abre los parámetros con la flecha del bloque) | El cuerpo de una celda |
| **mover** | x = `x`, y = `0`, z = `0` | La lleva a su lugar en la fila |
| **cilindro**, hueco (botón de hueco del bloque) | radio = `diametro / 2`, alto = `25`, lados = `64` | El hueco donde entra la broca |
| **mover** | x = `x`, y = `0`, z = `10` | Lo centra en la celda y lo sube 10 mm: queda abierto por arriba y con piso |
| **cambiar x por** | `diametro + 6` | Avanza a la siguiente celda |

Las sumas y divisiones son bloques de matemáticas: van en cualquier lugar donde va un número.

## 4. Crear grupo

Debajo del bucle (fuera de él), **crear grupo** (categoría de modificar). Une las celdas en una sola pieza y resta los
cilindros huecos.

## 5. Ejecutar

Botón de reproducir: Tinkercad arma la pieza bloque por bloque y resalta el bloque que corre. El primer botón de los
controles avanza un bloque a la vez.

## 6. Cambiar una variable

Cambia el `6` de `fijar huecos a` por `8` y ejecuta otra vez: la fila crece a 8 huecos con los mismos bloques. Para
brocas más gruesas, sube `diametro` (la celda crece con él: `diametro + 6`).

## 7. Exportar a STL

En la barra de Codeblocks, **Exportar** → **STL**. Guarda la de 6 huecos como `organizador-6.stl` y la de 8 como
`organizador-8.stl`. Codeblocks también exporta a OBJ, GLTF y SVG.

## 8. Medir los STL

Copia [`medir_stl.py`](medir_stl.py) a la carpeta de los dos STL:

```bash
python medir_stl.py organizador-6.stl organizador-8.stl
```

Salida (la de nuestra corrida):

```text
organizador-6.stl: 96.0 x 22.0 x 30.0 mm, 1568 caras
organizador-8.stl: 128.0 x 22.0 x 30.0 mm, 2088 caras
```

Cada celda mide `diametro + 6` = 16 mm de largo: 6 celdas son 96 mm y 8 celdas, 128 mm.

## Notas

- Holgura: si tus brocas entran muy justas, sube `diametro` medio milímetro.
- Tus diseños son privados hasta que cambies su privacidad.
- No mostramos el registro ni el inicio de sesión: la cuenta de Tinkercad es gratuita y se crea en tinkercad.com.

Fuentes: tinkercad.com, centro de ayuda de Tinkercad (Codeblocks: bloques, variables, reproducir un programa; crear una
cuenta) y blog oficial (guía de Codeblocks, 25 de marzo de 2022; opciones de exportación, 6 de junio de 2022),
consultados el 25 de noviembre de 2026.
