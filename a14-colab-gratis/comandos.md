# Colab gratis · la celda del video

Pega esto en una celda de código de Colab y ejecútala (botón ▶ o `Ctrl+Enter`):

```text
!nproc
!free -h
!df -h /
!nvidia-smi
```

En un cuaderno, una línea que empieza con `!` se manda tal cual al sistema operativo de la máquina (IPython, «System
shell access»).

| Línea | Qué hace | Qué mirar en el resultado |
|---|---|---|
| `!nproc` | Imprime cuántos procesadores tiene disponibles la máquina | El número |
| `!free -h` | Muestra la memoria libre y usada, en unidades legibles (`-h`) | Fila `Mem`: `total` y `available` |
| `!df -h /` | Muestra el espacio del disco de la raíz `/`, en unidades legibles (`-h`) | `Size` (tamaño) y `Avail` (libre) |
| `!nvidia-smi` | Muestra la GPU de NVIDIA, si tienes una | Nombre de la GPU y su memoria |

## Si `!nvidia-smi` da error

Es normal: tu entorno de ejecución no tiene GPU. Para pedirla, cambia el tipo de entorno de ejecución, elige una GPU y
vuelve a ejecutar la celda. En la versión gratuita el acceso a las GPU está muy restringido, así que puede que no
haya. Cuando ya no la uses, regresa el tipo a ninguno: la FAQ lo pide cuando Colab avisa que la GPU no se está usando.

## Por qué cambia el resultado

Google no publica estos límites: según su FAQ, los límites de uso, el tiempo de inactividad, la vida máxima de la
máquina y los tipos de GPU cambian con el tiempo. Lo que veas hoy puede ser distinto mañana.

## Sugerencia

Copia tu resultado a un archivo en Drive si lo quieres conservar: la máquina virtual se elimina cuando pasa un tiempo
inactiva.

Fuentes: FAQ oficial de Colab (`https://research.google.com/colaboratory/intl/es/faq.html` y
`https://research.google.com/colaboratory/faq.html`), referencia de IPython
(`https://ipython.readthedocs.io/en/stable/interactive/reference.html`), páginas de manual de `nproc`, `free` y `df` en
man7.org y documentación de `nvidia-smi` de NVIDIA (`https://docs.nvidia.com/deploy/nvidia-smi/index.html`),
consultadas el 20 de noviembre de 2026.
