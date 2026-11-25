#!/usr/bin/env bash
# Arma el repositorio de práctica del video «Encuentra el commit que rompió todo con git bisect» en ./practica-bisect
# Úsalo en Git Bash (Windows) o en la Terminal (Mac y Linux):  bash practica.sh
# Veinte commits sobre calc.sh, una suma de dos números. Uno de ellos rompe la suma: encuéntralo con git bisect.
# No toca tu configuración global: el autor de práctica («Práctica») queda solo en estos commits.
# Las fechas son fijas: así los hashes salen iguales que en el video.
set -e

if [ -e practica-bisect ]; then
  echo "Ya existe la carpeta practica-bisect. Bórrala o corre el script en otra carpeta."
  exit 1
fi

n=0
# guardar FECHA MENSAJE: guarda todo lo cambiado en un commit con autor y fecha de práctica
guardar() {
  n=$((n + 1))
  git add -A
  GIT_AUTHOR_NAME="Práctica" GIT_AUTHOR_EMAIL="practica@ayemi.invalid" GIT_AUTHOR_DATE="$1" \
  GIT_COMMITTER_NAME="Práctica" GIT_COMMITTER_EMAIL="practica@ayemi.invalid" GIT_COMMITTER_DATE="$1" \
    git commit -q -m "$2"
}

mkdir practica-bisect
cd practica-bisect
git init -q -b main
git config core.autocrlf false

printf '#!/usr/bin/env bash\n# Suma dos números: bash calc.sh 2 3\necho $(( $1 + $2 ))\n' > calc.sh
guardar "2026-11-01T09:00:00-06:00" "Primera versión de calc.sh"
git tag v1.0

printf '# Calculadora\n' > README.md
guardar "2026-11-02T09:00:00-06:00" "Agrega el README"

printf 'Uso: bash calc.sh 2 3\n' >> README.md
guardar "2026-11-03T09:00:00-06:00" "Explica cómo se usa"

printf 'Lunes: primera prueba\n' > notas.txt
guardar "2026-11-04T09:00:00-06:00" "Agrega notas"

printf 'Suma dos números enteros.\n' >> README.md
guardar "2026-11-05T09:00:00-06:00" "Describe la calculadora"

printf '2 + 3 = 5\n' > ejemplos.txt
guardar "2026-11-06T09:00:00-06:00" "Agrega ejemplos"

printf 'Martes: más ejemplos\n' >> notas.txt
guardar "2026-11-07T09:00:00-06:00" "Actualiza notas"

printf '10 + 5 = 15\n' >> ejemplos.txt
guardar "2026-11-08T09:00:00-06:00" "Agrega otro ejemplo"

printf 'Pendiente: probar con ceros\n' > pendientes.txt
guardar "2026-11-09T09:00:00-06:00" "Anota pendientes"

printf '0 + 0 = 0\n' >> ejemplos.txt
guardar "2026-11-10T09:00:00-06:00" "Prueba con ceros"

printf 'Miércoles: todo bien\n' >> notas.txt
guardar "2026-11-11T09:00:00-06:00" "Actualiza notas"

printf 'Pendiente: números negativos\n' >> pendientes.txt
guardar "2026-11-12T09:00:00-06:00" "Suma un pendiente"

# El error: al «ordenar» calc.sh, la suma se volvió resta
printf '#!/usr/bin/env bash\n# Suma dos números: bash calc.sh 2 3\n\necho $(( $1 - $2 ))\n' > calc.sh
guardar "2026-11-13T09:00:00-06:00" "Ordena calc.sh"

printf 'Jueves: limpieza\n' >> notas.txt
guardar "2026-11-14T09:00:00-06:00" "Actualiza notas"

printf 'Licencia: CC BY-SA 4.0\n' >> README.md
guardar "2026-11-15T09:00:00-06:00" "Agrega la licencia"

printf '7 + 1 = 8\n' >> ejemplos.txt
guardar "2026-11-16T09:00:00-06:00" "Agrega un ejemplo"

printf 'Viernes: revisión\n' >> notas.txt
guardar "2026-11-17T09:00:00-06:00" "Actualiza notas"

printf 'Pendiente: restar\n' >> pendientes.txt
guardar "2026-11-18T09:00:00-06:00" "Anota otro pendiente"

printf '# Calculadora de práctica\nUso: bash calc.sh 2 3\nSuma dos números enteros.\nLicencia: CC BY-SA 4.0\n' > README.md
guardar "2026-11-19T09:00:00-06:00" "Cambia el título del README"

printf 'Sábado: lista para publicar\n' >> notas.txt
guardar "2026-11-20T09:00:00-06:00" "Prepara la publicación"

# La prueba va FUERA del repositorio, junto a este script (como recomienda la documentación de git bisect):
# así ningún salto entre commits la toca. Sale con 0 si la suma da 5 (bueno) y con 1 si no (malo).
# git bisect run la corre desde la raíz del repositorio, por eso llama a calc.sh sin ruta.
printf '#!/usr/bin/env bash\n# Sale con 0 si la suma está bien y con 1 si está mal\n[ "$(bash calc.sh 2 3)" = "5" ]\n' > ../prueba.sh

echo "Listo: $n commits en practica-bisect"
