# ¿Fue la IA? No: fue un archivo

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Una parodia de noticiero: se cayeron 8.5 millones de computadoras con Windows (julio de 2024) y Estados Unidos pausó todas sus salidas de vuelos nacionales (enero de 2023). Según los informes oficiales, en las dos el problema fue **un archivo**. La lección: **un archivo se revisa antes de subirlo.** En Git Bash (Windows), Linux y Mac.

- **`python -m json.tool config.json`** valida un JSON: si está bien, lo imprime con formato; si está mal, te dice qué falta, en qué línea y en qué columna.
- **`echo $?`** muestra el código de salida del último comando: **0** es que todo salió bien; **1**, que hubo un error.
- Ese código es lo que usa un despliegue automático (por ejemplo, GitHub Actions) para frenar: si un paso sale con algo distinto de 0, falla y los siguientes no corren. El archivo roto no llega a producción.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `cat config.json` | Muestra el archivo de práctica (le falta una coma) |
| `python -m json.tool config.json` | Lo valida: qué falta, en qué línea y en qué columna |
| `echo $?` | Código de salida del último comando: 1 error, 0 bien |
| `sed -i 's/true$/true,/' config.json` | Agrega la coma que faltaba al final de la línea que termina en `true` |

La guía completa, paso por paso, con lo que debe salir y **el comando que revisa todos los JSON de tu proyecto de una vez**, está en [`comandos.md`](comandos.md).

## Lo que dicen los informes oficiales

| Caída | Qué pasó, según su informe | Fuente |
|---|---|---|
| Windows, 19 de julio de 2024 | Una actualización de configuración del sensor de CrowdStrike (el «Channel File 291») provocó la pantalla azul en 8.5 millones de equipos, menos del 1 % de los equipos con Windows. No fue un ciberataque | [Microsoft](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/) · [CrowdStrike](https://www.crowdstrike.com/en-us/blog/falcon-update-for-windows-hosts-technical-details/) |
| Vuelos en Estados Unidos, 11 de enero de 2023 | La FAA pausó todas las salidas nacionales. Su revisión rastreó la falla hasta un archivo de base de datos dañado, sin señales de ciberataque; después dijo que personal de un contratista borró archivos sin querer | [FAA](https://www.faa.gov/newsroom/faa-notam-statement) |
| Cloudflare, 18 de noviembre de 2025 | Un «archivo de características» duplicó su tamaño. No fue un ataque | [Cloudflare](https://blog.cloudflare.com/18-november-2025-outage/) |

El «audio del ingeniero» del video es una **recreación nuestra** y es broma.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| `json.tool` (Python) | https://docs.python.org/3/library/json.html#module-json.tool |
| `sys.exit` y códigos de salida (Python) | https://docs.python.org/3/library/sys.html#sys.exit |
| Códigos de salida en GitHub Actions | https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes |
| GNU sed | https://www.gnu.org/software/sed/manual/sed.html |
| Git for Windows (Git Bash) | https://gitforwindows.org/ |
| Video anterior de la serie | [`../g14-github-actions/`](../g14-github-actions/) |

Datos verificados el 22 de noviembre de 2026 en los informes oficiales de Microsoft, CrowdStrike, la FAA y Cloudflare, y en la documentación de Python, GNU sed y GitHub. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · Código: MIT · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
