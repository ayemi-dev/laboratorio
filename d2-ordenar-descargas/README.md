# Ordena tu carpeta de Descargas con Python

Un script corto que manda cada archivo de una carpeta (por ejemplo, Descargas) a una subcarpeta según su tipo: Documentos, Imágenes, Instaladores, Comprimidos, Audio y video, y Otros. Solo usa la biblioteca estándar de Python: no hay nada que instalar.

## Instalar

Instala Python 3.9 o más reciente: https://www.python.org/downloads/

## Usar

1. Guarda `ordenar.py` **fuera** de la carpeta que vas a ordenar (si no, también se movería a «Otros»).
2. Primero, en modo de prueba. Solo muestra lo que haría, sin mover nada:

```bash
python ordenar.py "C:\Users\tu-usuario\Downloads" --simular
```

3. Si te convence, córrelo de verdad:

```bash
python ordenar.py "C:\Users\tu-usuario\Downloads"
```

En macOS o Linux la ruta es `~/Downloads`.

## Qué hace y qué no

- **Nunca sobrescribe.** Si en el destino ya existe un archivo con el mismo nombre, el nuevo queda como `nombre (1).pdf`, `nombre (2).pdf`… (`shutil.move` sí podría sobrescribir, por eso el script busca un nombre libre antes).
- **Solo mueve archivos de la carpeta principal.** No entra a subcarpetas ni mueve carpetas, y se salta los archivos ocultos (los que empiezan con punto).
- **Las extensiones** se comparan en minúsculas (`.PNG` y `.png` van a Imágenes). Lo que no está en la lista va a «Otros».
- **Para agregar tipos**, edita el diccionario `TIPOS` al inicio del script. Por ejemplo: `"Código": [".py", ".js", ".html"]`.
- Si tienes una descarga a medias (Chrome las nombra `.crdownload`), espera a que termine antes de correrlo.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Python | https://www.python.org/downloads/ |
| pathlib (documentación) | https://docs.python.org/3/library/pathlib.html |
| shutil.move (documentación) | https://docs.python.org/3/library/shutil.html#shutil.move |

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tienes una tarea que repites cada semana? La automatizamos: https://ayemi.org/enlaces
