#!/bin/bash
# Crea la carpeta de práctica de G26: un proyecto pequeño con cinco archivos.
# Uno de ellos lleva fecha de hace diez días para probar find -mtime.
if [ -e proyecto ]; then
  echo "ya existe proyecto/: bórrala o usa otra carpeta"
  exit 1
fi
mkdir -p proyecto/src proyecto/docs proyecto/viejo
cd proyecto || exit 1
printf '%s\n' 'from src.saludo import saludar' 'print(saludar("mundo"))' > app.py
printf '%s\n' 'def saludar(n):' '    return "Hola, " + n' > src/saludo.py
printf '%s\n' 'from .saludo import saludar' '' 'def bienvenida(n):' '    return saludar(n) + "."' > src/correo.py
printf '%s\n' '# Notas' 'Pendiente: pruebas de saludar' > docs/notas.md
printf '%s\n' 'def saludar(n):' '    print("Hola", n)' > viejo/saludo_v1.py
touch -d "10 days ago" viejo/saludo_v1.py
echo "proyecto de práctica: 5 archivos"
