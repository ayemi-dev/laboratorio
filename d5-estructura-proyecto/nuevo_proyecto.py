"""Crea un proyecto nuevo con las carpetas y archivos de estructura.txt.

Uso:  python nuevo_proyecto.py mi-app
"""
import sys
import venv
from pathlib import Path

SANGRIA = 4  # espacios por nivel en estructura.txt


def leer_estructura(archivo):
    """Devuelve (ruta, es_carpeta) por cada línea. Las carpetas terminan en «/»."""
    rutas, padres = [], []
    for linea in archivo.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        nivel = (len(linea) - len(linea.lstrip(" "))) // SANGRIA
        del padres[nivel:]
        nombre = linea.strip()
        es_carpeta = nombre.endswith("/")
        nombre = nombre.rstrip("/")
        rutas.append((Path(*padres, nombre), es_carpeta))
        if es_carpeta:
            padres.append(nombre)
    return rutas


def crear(nombre):
    raiz = Path(nombre)
    if raiz.exists():
        sys.exit(f"Ya existe «{raiz}»: no se toca nada.")
    plantilla = Path(__file__).with_name("estructura.txt")
    for ruta, es_carpeta in leer_estructura(plantilla):
        destino = raiz / ruta
        if es_carpeta:
            destino.mkdir(parents=True, exist_ok=True)
        else:
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.touch()
        print("  +", ruta.as_posix() + ("/" if es_carpeta else ""))
    (raiz / "README.md").write_text(f"# {raiz.name}\n", encoding="utf-8")
    print("  + .venv/  (entorno virtual)")
    venv.create(raiz / ".venv", with_pip=True)
    print(f"Listo: {raiz}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python nuevo_proyecto.py nombre-del-proyecto")
    crear(sys.argv[1])
