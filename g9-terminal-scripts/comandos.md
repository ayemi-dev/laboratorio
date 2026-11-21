# La terminal, nivel 2 · tuberías, redirecciones y tu primer script

Guía del video. Cada comando va en su propia línea y se copia tal cual. Primero va Windows (PowerShell) y luego Linux y Mac: hacen lo mismo.

## 1. Prepara la carpeta de práctica

Usa la carpeta `mi-pagina` del video anterior, o crea una carpeta nueva para no tocar tus archivos. Adentro, crea un archivo de texto llamado `notas.txt` con estas tres líneas (con el Bloc de notas, VS Code o el editor que uses):

```text
falta: probar el sensor
listo: comprar cables
falta: subir el programa
```

Escríbelas sin acentos: Windows PowerShell 5.1 puede mostrar mal los acentos de algunos archivos de texto.

Abre la terminal en esa carpeta:

- **Windows:** abre **Windows PowerShell** (viene con Windows) y entra a la carpeta con `cd`.
- **Mac:** abre la app **Terminal**.
- **Linux:** abre la terminal de tu sistema.

## 2. Los comandos, paso a paso

### La tubería `|`: une dos comandos

Windows PowerShell:

```powershell
cat notas.txt
cat notas.txt | sls falta
```

Linux y Mac:

```sh
cat notas.txt
cat notas.txt | grep falta
```

El primero muestra las tres líneas. El segundo pasa esas líneas, por la tubería, a un comando que deja solo las que dicen `falta`:

```text
falta: probar el sensor
falta: subir el programa
```

`grep` busca un texto en las líneas que recibe. En PowerShell, su par es `Select-String`, y `sls` es su nombre corto. `cat`, en PowerShell de Windows, es el nombre corto de `Get-Content`.

### Un signo `>`: guarda la salida en un archivo

Windows PowerShell:

```powershell
Get-Date > hoy.txt
```

Linux y Mac:

```sh
date > hoy.txt
```

No muestra nada en pantalla: la fecha y la hora se fueron al archivo `hoy.txt`. Si `hoy.txt` no existía, se crea; **si ya existía, se reemplaza sin avisar.**

### Dos signos `>>`: agrega al final

Windows PowerShell:

```powershell
cat notas.txt | sls falta >> hoy.txt
cat hoy.txt
```

Linux y Mac:

```sh
cat notas.txt | grep falta >> hoy.txt
cat hoy.txt
```

`>>` agrega lo que falta debajo de la fecha, sin borrar lo que había. `cat hoy.txt` te muestra la lista (la fecha sale en el idioma y el formato de tu sistema; en PowerShell verás además algunas líneas en blanco):

```text
<la fecha y la hora de hoy>
falta: probar el sensor
falta: subir el programa
```

## 3. Tu primer script

Un script es un archivo de texto con comandos. Crea, en la misma carpeta, el de tu sistema con estas dos líneas:

`hoy.ps1` (Windows PowerShell):

```powershell
Get-Date > hoy.txt
cat notas.txt | sls falta >> hoy.txt
```

`hoy.sh` (Linux y Mac):

```sh
date > hoy.txt
cat notas.txt | grep falta >> hoy.txt
```

Como la primera línea usa `>`, cada vez que lo corres empieza un `hoy.txt` nuevo con la fecha del día: no crece sin fin.

Córrelo:

Windows PowerShell:

```powershell
.\hoy.ps1
cat hoy.txt
```

Linux y Mac:

```sh
sh hoy.sh
cat hoy.txt
```

En PowerShell, el `.\` del principio le dice que el script está en la carpeta actual. En Mac, la Terminal abre la shell zsh; `sh hoy.sh` funciona igual.

## 4. Si Windows no te deja correr el script

En Windows, PowerShell bloquea los scripts hasta que les das permiso. Si al correr `.\hoy.ps1` ves un error que habla de la directiva de ejecución («execution policy»), da permiso, una sola vez, a los scripts escritos en tu computadora:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Si te pide confirmar, responde que sí. Luego corre otra vez `.\hoy.ps1`. Con `RemoteSigned`, los scripts que escribes tú en tu computadora no necesitan firma; los descargados de internet sí. Fuera de Windows, PowerShell no tiene este bloqueo.

En el video se vio el error real de Windows PowerShell 5.1; el texto exacto depende del idioma de tu Windows.

Fuentes: documentación de PowerShell en Microsoft Learn (about_Pipelines, about_Redirection, about_Scripts, about_Execution_Policies, Select-String, Get-Content, Get-Date y What is Windows PowerShell), manual de GNU Bash (Pipelines y Redirections), estándar POSIX de The Open Group (sh y Shell Command Language), páginas de manual de `grep`, `cat` y `date` en man7.org y guía de la Terminal de Apple (redirección, scripts y shell predeterminada), consultadas el 20 de noviembre de 2026.
