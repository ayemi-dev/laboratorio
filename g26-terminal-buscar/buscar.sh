#!/bin/bash
bash crear-practica.sh
cd proyecto
find . -type f
find . -name "*.py"
find . -name "saludo*"
find . -mtime +7
grep -rn saludar
grep -rn -C 1 "def saludar" src
grep -rni pendiente
grep -rl saludar
find . -name "*.py" | xargs grep -c saludar
grep -rn "saludar(" | grep -v "def "
