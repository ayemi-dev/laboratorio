"""Bloquea el commit si un archivo preparado contiene un término de la lista local.

La lista vive fuera del repositorio, en ~/.ayemi/bloqueados.txt (una expresión
regular por línea; las líneas con # son comentarios). No se publica: así el
repositorio no revela lo que protege. Si la lista no existe, el commit se bloquea.
"""
import re
import subprocess
import sys
from pathlib import Path

LISTA = Path.home() / ".ayemi" / "bloqueados.txt"


def main() -> int:
    if not LISTA.exists():
        print(f"revisar_nombres: no existe {LISTA}; commit bloqueado.", file=sys.stderr)
        return 1
    patrones = [re.compile(l.strip(), re.I) for l in LISTA.read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.lstrip().startswith("#")]
    archivos = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
                              capture_output=True, text=True, check=True).stdout.split()
    hallazgos = 0
    for nombre in archivos + [""]:
        if not nombre:
            continue
        contenido = subprocess.run(["git", "show", f":{nombre}"], capture_output=True).stdout
        texto = nombre + "\n" + contenido.decode("utf-8", errors="ignore")
        for n, linea in enumerate(texto.splitlines()):
            for p in patrones:
                if p.search(linea):
                    donde = "nombre del archivo" if n == 0 else f"línea {n}"
                    print(f"revisar_nombres: {nombre} ({donde}) contiene un término bloqueado.",
                          file=sys.stderr)
                    hallazgos += 1
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())
