# La terminal, nivel 2: tuberías, redirecciones y tu primer script

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi y segunda parte de [la terminal sin miedo](../g4-terminal-sin-miedo/). Allá aprendiste diez comandos para moverte. Aquí los pones a trabajar por ti: unes comandos con una tubería, guardas lo que sale en un archivo y juntas todo en un script que cada día arma tu lista de pendientes con fecha. Lo mismo en Windows (PowerShell) y en Linux o Mac.

- **Tubería `|`**: lo que sale de un comando entra al siguiente.
- **`>`**: manda la salida a un archivo; si ya existía, lo reemplaza.
- **`>>`**: agrega la salida al final del archivo, sin borrar lo que había.
- **Script**: un archivo de texto con comandos que corres con uno solo.

## Los comandos del video

| Windows PowerShell | Linux y Mac | Qué hace |
|---|---|---|
| `cat notas.txt` | `cat notas.txt` | Muestra el archivo de notas |
| `cat notas.txt \| sls falta` | `cat notas.txt \| grep falta` | Deja solo las líneas que dicen `falta` |
| `Get-Date > hoy.txt` | `date > hoy.txt` | Escribe la fecha en `hoy.txt` (si existía, lo reemplaza) |
| `cat notas.txt \| sls falta >> hoy.txt` | `cat notas.txt \| grep falta >> hoy.txt` | Agrega lo que falta al final de `hoy.txt` |
| `cat hoy.txt` | `cat hoy.txt` | Muestra la lista: la fecha y debajo lo que falta |
| `.\hoy.ps1` | `sh hoy.sh` | Corre tu script |

En PowerShell, `sls` es el nombre corto de `Select-String`, que hace lo mismo que `grep`. Y `cat` es el nombre corto de `Get-Content` en Windows.

La guía completa, con cómo preparar la práctica, los dos scripts y el permiso que pide Windows, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Tuberías en PowerShell (about_Pipelines) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines |
| Redirecciones en PowerShell (about_Redirection) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection |
| Scripts en PowerShell (about_Scripts) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_scripts |
| Permiso para los scripts (about_Execution_Policies) | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies |
| `Select-String` | https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string |
| Tuberías en Bash | https://www.gnu.org/software/bash/manual/html_node/Pipelines.html |
| Redirecciones en Bash | https://www.gnu.org/software/bash/manual/html_node/Redirections.html |
| Redirigir en la Terminal de Mac | https://support.apple.com/guide/terminal/redirect-terminal-input-and-output-apd1dbe647b-7e11-49dc-aa76-89aa7e53ce36/mac |
| Scripts en la Terminal de Mac | https://support.apple.com/guide/terminal/intro-to-shell-scripts-apd53500956-7c5b-496b-a362-2845f2aab4bc/mac |
| `grep` | https://man7.org/linux/man-pages/man1/grep.1.html |
| Video anterior: la terminal sin miedo | [`../g4-terminal-sin-miedo/`](../g4-terminal-sin-miedo/) |

Datos verificados el 20 de noviembre de 2026 en la documentación oficial de Microsoft, Apple, GNU y The Open Group. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
