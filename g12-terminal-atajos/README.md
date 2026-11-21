# La terminal, nivel 3: alias, historial y atajos que te ahorran horas

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y tercera parte de la terminal, después de [la terminal sin miedo](../g4-terminal-sin-miedo/) y [tuberías, redirecciones y tu primer script](../g9-terminal-scripts/). Allá escribiste `cat notas.txt | grep falta`. Aquí lo escribes con una palabra, y dejas que la terminal recuerde y complete por ti. Lo mismo en Windows (PowerShell) y en Git Bash o Linux; en Mac, casi igual.

- **Alias**: un nombre corto para un comando largo. Si lo escribes en tu archivo de inicio, sigue ahí cada vez que abres la terminal.
- **Ctrl+R**: busca hacia atrás en tu historial mientras escribes.
- **Tab**: completa nombres de archivos y comandos.
- **`!!`**: repite el comando anterior, y le puedes sumar algo. En PowerShell, el par es **`r`**.

## Los comandos del video

| Windows PowerShell | Git Bash y Linux | Qué hace |
|---|---|---|
| `function falta { cat notas.txt \| sls falta }` en tu perfil | `alias falta='cat notas.txt \| grep falta'` en `~/.bashrc` | Crea `falta`, que muestra solo las líneas que dicen `falta` |
| `falta` | `falta` | Lo usa, en cualquier terminal nueva, dentro de la carpeta |
| Ctrl+R y unas letras | Ctrl+R y unas letras | Busca un comando que ya escribiste |
| `cat no` y Tab | `cat no` y Tab | Completa el nombre: `notas.txt` |
| `r` | `!!` | Repite el comando anterior |
| — | `!! \| grep listo` | Repite el anterior y le suma algo |

En PowerShell, un alias no puede llevar un comando con sus parámetros: por eso se escribe como función.

La guía completa, con cómo crear tu perfil de PowerShell, dónde va el alias en cada sistema y qué hacer si no funciona, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Alias en Bash | https://www.gnu.org/software/bash/manual/bash.html#Aliases |
| Archivos de inicio de Bash (`~/.bashrc`, `~/.bash_profile`) | https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files |
| Ctrl+R en Bash (historial) | https://www.gnu.org/software/bash/manual/bash.html#Commands-For-History |
| Tab en Bash (completar) | https://www.gnu.org/software/bash/manual/bash.html#Commands-For-Completion |
| `!!` en Bash | https://www.gnu.org/software/bash/manual/bash.html#Event-Designators |
| Alias en PowerShell (about_Aliases) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_aliases?view=powershell-5.1 |
| Perfil de PowerShell (about_Profiles) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-5.1 |
| Atajos de PSReadLine (Ctrl+R, Tab) | https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline_functions?view=powershell-5.1 |
| `r` (Invoke-History) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-history?view=powershell-5.1 |
| Archivos de inicio de zsh (Mac) | https://zsh.sourceforge.io/Doc/Release/Files.html |
| Video anterior: tuberías, redirecciones y tu primer script | [`../g9-terminal-scripts/`](../g9-terminal-scripts/) |

Datos verificados el 21 de noviembre de 2026 en el manual de Bash de GNU, la documentación de PowerShell de Microsoft, la guía de la Terminal de Apple y el manual de zsh. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
