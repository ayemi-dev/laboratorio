#!/usr/bin/env bash
# Arma el repositorio de práctica del video «Git: recupera una rama que borraste con git reflog» en ./practica-reflog
# Úsalo en Git Bash (Windows) o en la Terminal (Mac y Linux):  bash practica.sh
# Tres commits en main y una rama, tema-oscuro, con tres commits más que no están en main.
# Bórrala con git branch -D y recupérala con git reflog.
# No toca tu configuración global: el autor de práctica («Práctica») queda solo en este repositorio.
# Las fechas de los commits son fijas: así los hashes salen iguales que en el video.
set -e

if [ -e practica-reflog ]; then
  echo "Ya existe la carpeta practica-reflog. Bórrala o corre el script en otra carpeta."
  exit 1
fi

# guardar FECHA MENSAJE: guarda todo lo cambiado en un commit con autor y fecha de práctica
guardar() {
  git add -A
  GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" git commit -q -m "$2"
}

mkdir practica-reflog
cd practica-reflog
git init -q -b main
git config core.autocrlf false
# Autor de práctica solo en este repositorio (también firma las entradas del reflog)
git config user.name "Práctica"
git config user.email "practica@ayemi.invalid"

printf '<h1>Mi página</h1>\n' > index.html
guardar "2026-11-01T09:00:00-06:00" "Primera versión"

printf 'body { color: black; }\n' > estilos.css
guardar "2026-11-02T09:00:00-06:00" "Agrega estilos"

printf '<p>Hola</p>\n' >> index.html
guardar "2026-11-03T09:00:00-06:00" "Agrega un saludo"

# La rama que se va a borrar: tres commits que no están en main
git switch -q -c tema-oscuro

printf 'body { background: black; }\n' >> estilos.css
guardar "2026-11-04T09:00:00-06:00" "Fondo negro"

printf 'body { color: white; }\n' >> estilos.css
guardar "2026-11-05T09:00:00-06:00" "Letra blanca"

printf 'a { color: cyan; }\n' >> estilos.css
guardar "2026-11-06T09:00:00-06:00" "Tema listo"

git switch -q main

echo "Listo: rama tema-oscuro con 3 commits"
