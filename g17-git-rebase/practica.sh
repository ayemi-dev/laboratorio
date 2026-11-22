#!/usr/bin/env bash
# Arma el repositorio de práctica del video «Git nivel 5: rebase o merge» en ./practica-rebase
# Úsalo en Git Bash (Windows) o en la Terminal (Mac y Linux):  bash practica.sh
# No toca tu configuración global: el nombre y el correo de práctica quedan solo en este repositorio.
set -e

if [ -e practica-rebase ]; then
  echo "Ya existe la carpeta practica-rebase. Bórrala o corre el script en otra carpeta."
  exit 1
fi

mkdir practica-rebase
cd practica-rebase
git init -q -b main
git config user.name "Ayemi Laboratorio"
git config user.email "laboratorio@ayemi.invalid"
git config log.decorate short

echo "<h1>Hola</h1>" > index.html
git add index.html
git commit -q -m "Primera versión"

git switch -q -c nueva-portada
echo "<h1>Bienvenidos</h1>" > index.html
git commit -q -am "Nueva portada"

git switch -q main
echo "<p>Contacto</p>" > contacto.html
git add contacto.html
git commit -q -m "Agrega contacto"

git switch -q nueva-portada

echo "Listo. Ahora:"
echo "  cd practica-rebase"
echo "  git log --oneline --graph --all"
