"""Ordena una carpeta (por ejemplo, Descargas) en subcarpetas por tipo.

    python ordenar.py ~/Downloads --simular   # solo muestra lo que haría
    python ordenar.py ~/Downloads             # mueve de verdad

Solo usa la biblioteca estándar (Python 3.9 o más). Nunca sobrescribe:
si el nombre ya existe en el destino, agrega « (1)», « (2)»…
"""
import argparse
import shutil
from pathlib import Path

TIPOS = {
    "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Instaladores": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Audio y video": [".mp3", ".wav", ".mp4", ".mov"],
}


def carpeta_de(archivo):
    ext = archivo.suffix.lower()
    for carpeta, exts in TIPOS.items():
        if ext in exts:
            return carpeta
    return "Otros"


def nombre_libre(destino):
    libre, n = destino, 1
    while libre.exists():
        libre = destino.with_stem(f"{destino.stem} ({n})")
        n += 1
    return libre


def main():
    p = argparse.ArgumentParser()
    p.add_argument("carpeta", type=Path)
    p.add_argument("--simular", action="store_true")
    args = p.parse_args()

    archivos = [a for a in args.carpeta.iterdir()
                if a.is_file() and not a.name.startswith(".")]
    for archivo in archivos:
        carpeta = args.carpeta / carpeta_de(archivo)
        destino = nombre_libre(carpeta / archivo.name)
        print(f"{archivo.name} -> {carpeta.name}/{destino.name}")
        if not args.simular:
            carpeta.mkdir(exist_ok=True)
            shutil.move(archivo, destino)

    hecho = "se moverían" if args.simular else "movidos"
    print(f"{len(archivos)} archivos {hecho}")


if __name__ == "__main__":
    main()
