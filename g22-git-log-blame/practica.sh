#!/usr/bin/env bash
# Arma el repositorio de práctica del video «Git: quién cambió esta línea y por qué» en ./practica-blame
# Úsalo en Git Bash (Windows) o en la Terminal (Mac y Linux):  bash practica.sh
# No toca tu configuración global: los autores de práctica («Textos» y «Diseño») quedan solo en estos commits.
# Las fechas son fijas: así los hashes salen iguales que en el video.
set -e

if [ -e practica-blame ]; then
  echo "Ya existe la carpeta practica-blame. Bórrala o corre el script en otra carpeta."
  exit 1
fi

# guardar AUTOR CORREO FECHA -m MENSAJE [-m PÁRRAFO]
guardar() {
  local autor="$1" correo="$2" fecha="$3"
  shift 3
  GIT_AUTHOR_NAME="$autor" GIT_AUTHOR_EMAIL="$correo" GIT_AUTHOR_DATE="$fecha" \
  GIT_COMMITTER_NAME="$autor" GIT_COMMITTER_EMAIL="$correo" GIT_COMMITTER_DATE="$fecha" \
    git commit -q "$@"
}

mkdir practica-blame
cd practica-blame
git init -q -b main
git config core.autocrlf false

printf '<h1>Hola</h1>\n<p>Contacto</p>\n' > index.html
git add index.html
guardar "Textos" "textos@ayemi.invalid" "2026-11-02T09:00:00-06:00" -m "Primera versión"

printf '<h1>Hola</h1>\n<p>Horario: 9 a 18</p>\n<p>Contacto</p>\n' > index.html
git add index.html
guardar "Textos" "textos@ayemi.invalid" "2026-11-03T10:30:00-06:00" -m "Agrega el horario"

printf '<h1>Bienvenidos</h1>\n<p>Horario: 9 a 18</p>\n<p>Contacto</p>\n' > index.html
git add index.html
guardar "Diseño" "diseno@ayemi.invalid" "2026-11-05T16:00:00-06:00" -m "Cambia el título" -m "Hola se veía informal en la portada."

echo "Listo. Ahora:"
echo "  cd practica-blame"
echo "  git blame --date=short index.html"
