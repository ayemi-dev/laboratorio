# La estructura de tu proyecto en un solo comando (con Python)

Script de Python de 51 líneas que crea las carpetas, los archivos iniciales y el entorno virtual (`.venv` con `pip`) de un proyecto nuevo a partir de `estructura.txt`, usando solo la biblioteca estándar (`pathlib` y `venv`).

## Cómo usarlo

1. Define tu árbol en `estructura.txt` (4 espacios por nivel; las carpetas terminan en `/`).
2. Ejecuta en la carpeta donde están `nuevo_proyecto.py` y `estructura.txt`:

```text
python nuevo_proyecto.py mi-app
```

Si `mi-app` ya existe, el script se detiene sin modificar ni borrar nada.

## Activar el entorno virtual (Windows)

- **cmd.exe:**

```cmd
mi-app\.venv\Scripts\activate.bat
```

- **PowerShell:**

```powershell
mi-app\.venv\Scripts\Activate.ps1
```

## Fuentes oficiales de Python

- Módulo `venv`: https://docs.python.org/3/library/venv.html
- Tutorial de entornos virtuales y paquetes: https://docs.python.org/3/tutorial/venv.html
- Módulo `pathlib`: https://docs.python.org/3/library/pathlib.html
