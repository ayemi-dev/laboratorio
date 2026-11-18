"""Junta el árbol y los archivos clave de un proyecto
en un solo texto para pegarlo en el chat de una IA.

Uso:  python contexto_ia.py mi-app
"""
import sys
from pathlib import Path

SALTAR = {".venv", "venv", "node_modules",
          "__pycache__", ".git"}
CLAVE = {".py", ".md", ".txt", ".json", ".toml",
         ".js", ".jsx", ".html", ".css"}
LIMITE = 20_000  # bytes; si un archivo pasa, se omite


def recorrer(carpeta, nivel, arbol, archivos):
    """Anota el árbol y los archivos clave."""
    for ruta in sorted(carpeta.iterdir()):
        if ruta.name in SALTAR:
            continue
        if ruta.name.startswith(".env"):  # secretos
            continue
        sangria = "    " * nivel
        if ruta.is_dir():
            arbol.append(f"{sangria}{ruta.name}/")
            recorrer(ruta, nivel + 1, arbol, archivos)
        else:
            arbol.append(f"{sangria}{ruta.name}")
            if ruta.suffix in CLAVE:
                archivos.append(ruta)


def juntar(nombre):
    raiz = Path(nombre)
    if not raiz.is_dir():
        sys.exit(f"No existe la carpeta «{raiz}».")
    arbol, archivos = [], []
    recorrer(raiz, 0, arbol, archivos)
    texto = [f"# Proyecto: {raiz.name}", "",
             "## Estructura", "", "````text",
             *arbol, "````"]
    for ruta in archivos:
        relativa = ruta.relative_to(raiz).as_posix()
        texto += ["", f"## {relativa}", ""]
        if ruta.stat().st_size > LIMITE:
            texto.append("(omitido: pasa del límite)")
        else:
            leido = ruta.read_text(encoding="utf-8",
                                   errors="replace")
            leido = leido.rstrip() or "(vacío)"
            texto += ["````", leido, "````"]
        print("  +", relativa)
    salida = Path(f"contexto-{raiz.name}.md")
    completo = "\n".join(texto) + "\n"
    salida.write_text(completo, encoding="utf-8")
    n = len(completo)
    print(f"Listo: {salida}, {n} caracteres")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python contexto_ia.py carpeta")
    juntar(sys.argv[1])
