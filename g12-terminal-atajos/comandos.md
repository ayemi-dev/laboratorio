# La terminal, nivel 3 · alias, historial y atajos

Guía del video. Cada comando va en su propia línea y se copia tal cual. Primero va Windows (PowerShell) y luego Git Bash y Linux; al final, lo que cambia en Mac.

## 1. Prepara la carpeta de práctica

Usa la carpeta `mi-pagina` de los videos anteriores, con su `notas.txt`. Si no la tienes, crea en tu carpeta de usuario una carpeta `mi-pagina` y adentro un archivo `notas.txt` con estas tres líneas, sin acentos:

```text
falta: probar el sensor
listo: comprar cables
falta: subir el programa
```

En el video, `mi-pagina` está en la carpeta de usuario: así, al abrir una terminal nueva, basta `cd mi-pagina`.

## 2. Un alias permanente

Un alias que escribes directo en la terminal se borra al cerrarla. Para tenerlo siempre, va en el archivo que la terminal lee al abrir.

### Git Bash y Linux: `~/.bashrc`

Agrega el alias al final de `~/.bashrc` (si el archivo no existe, se crea):

```sh
echo "alias falta='cat notas.txt | grep falta'" >> ~/.bashrc
```

Para usarlo en la terminal que ya tienes abierta, carga el archivo otra vez:

```sh
source ~/.bashrc
```

Pruébalo dentro de la carpeta:

```sh
cd ~/mi-pagina
falta
```

```text
falta: probar el sensor
falta: subir el programa
```

Para ver todos tus alias, escribe `alias` solo. Para quitar este, borra su línea de `~/.bashrc`.

### Windows PowerShell: tu perfil

En PowerShell, un alias no puede llevar un comando con sus parámetros, así que se escribe como **función**. Va en tu **perfil**, un script que PowerShell corre cada vez que abre. PowerShell no crea el perfil por ti; si no existe, este bloque lo crea (cópialo completo):

```powershell
if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
```

Ábrelo en el Bloc de notas:

```powershell
notepad $PROFILE
```

Pega estas tres líneas al final y guarda:

```powershell
function falta {
  cat notas.txt | sls falta
}
```

Para usarla en la terminal que ya tienes abierta, carga el perfil (un punto, un espacio y `$PROFILE`):

```powershell
. $PROFILE
```

Pruébala dentro de la carpeta:

```powershell
cd ~\mi-pagina
falta
```

Verás las dos líneas que dicen `falta` (Windows PowerShell 5.1 pone algunas líneas en blanco alrededor). En PowerShell, `sls` es el nombre corto de `Select-String` y `cat` el de `Get-Content`, como en el video anterior.

### Comprueba que es permanente

Cierra la terminal, abre una nueva, entra a la carpeta y escribe `falta`. Si salen las dos líneas, el alias ya es tuyo.

## 3. Ctrl+R: busca en tu historial

En una terminal nueva, presiona **Ctrl+R** y escribe unas letras de un comando que ya usaste, por ejemplo `pag`. Aparece el comando más reciente que las contiene:

- en Git Bash: `(reverse-i-search)`pag': cd mi-pagina`
- en Windows PowerShell: el comando en la línea y, debajo, `bck-i-search: pag`

Presiona **Enter** para correrlo. Bash guarda el historial al cerrar la terminal (en `~/.bash_history`) y lo lee al abrir otra: por eso Ctrl+R encuentra lo que escribiste en una ventana anterior. Windows PowerShell también guarda su historial en un archivo.

## 4. Tab: completa nombres

Escribe el principio de un nombre y presiona **Tab**:

```text
cat no
```

Tab lo completa a `cat notas.txt` en Git Bash y a `cat .\notas.txt` en Windows PowerShell. Si hay varios nombres que empiezan igual, en PowerShell cada Tab muestra el siguiente.

## 5. `!!`: repite el comando anterior

En Git Bash y Linux, `!!` es el comando anterior. Lo puedes repetir tal cual o sumarle algo:

```sh
cat notas.txt
!! | grep listo
```

El segundo corre `cat notas.txt | grep listo`:

```text
listo: comprar cables
```

En PowerShell no existe `!!`. Su par es `r`, que repite el último comando tal cual:

```powershell
cat .\notas.txt
r
```

## 6. Si no funciona

- **Git Bash no reconoce `falta` en una terminal nueva.** Git Bash puede abrir como terminal de inicio de sesión, que lee `~/.bash_profile` en lugar de `~/.bashrc`. Si tienes un `~/.bash_profile` y no carga tu `~/.bashrc`, agrégale al final esta línea, la que recomienda el manual de Bash:

  ```sh
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

- **PowerShell muestra un error al abrir que habla de la directiva de ejecución («execution policy»).** El perfil es un script, y Windows bloquea los scripts hasta que les das permiso. El permiso está en la [guía del video anterior](../g9-terminal-scripts/comandos.md#4-si-windows-no-te-deja-correr-el-script).
- **`falta` dice que no encuentra `notas.txt`.** El alias usa `notas.txt` de la carpeta en la que estás: entra primero a `mi-pagina`.

## 7. En Mac

La Terminal de Mac usa zsh (desde macOS 10.15). El alias se escribe igual, pero va en `~/.zshrc`:

```sh
echo "alias falta='cat notas.txt | grep falta'" >> ~/.zshrc
source ~/.zshrc
```

Fuentes: manual de GNU Bash 5.3 (Aliases, Bash Startup Files, Bash History Facilities, Commands For Manipulating The History, Letting Readline Type For You, Event Designators y los comandos `alias`, `source` y `.`), documentación de PowerShell en Microsoft Learn (about_Aliases, about_Profiles, about_Functions, about_Scripts, about_Tab_Expansion, about_PSReadLine, about_PSReadLine_Functions e Invoke-History), guía de la Terminal de Apple, soporte de Apple (zsh en macOS) y manual de zsh (Files), consultados el 21 de noviembre de 2026.
