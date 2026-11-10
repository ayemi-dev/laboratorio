# Limpia el ruido de tu audio con Python

Quita el ruido de fondo constante (ventilador, zumbido o aire acondicionado) de una grabación con 6 líneas de Python y la librería [noisereduce](https://github.com/timsainb/noisereduce).

## Instalar

1. Instala Python 3.10 o más reciente: https://www.python.org/downloads/
2. Instala las librerías:

```bash
pip install -r requirements.txt
```

## Usar

1. Graba tu audio dejando **2 segundos de silencio al inicio**: el script aprende de ahí cómo suena el ruido.
2. Guárdalo como `grabacion.wav` junto a `limpiar_audio.py`.
3. Corre:

```bash
python limpiar_audio.py
```

4. El resultado queda en `grabacion-limpia.wav`.

## Notas

- **Estéreo:** el script está pensado para audio mono. Si tu archivo es estéreo, conviértelo a mono antes, por ejemplo con `audio = audio.mean(axis=1)` después de leerlo.
- **Otros formatos:** si tienes MP3 o M4A, conviértelo primero a WAV, por ejemplo con `ffmpeg -i grabacion.mp3 grabacion.wav`.
- **Ruido que cambia** (voces de fondo, tráfico): `noisereduce` también tiene un modo no estacionario. Revisa su documentación.

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Python | https://www.python.org/downloads/ |
| noisereduce | https://pypi.org/project/noisereduce/ |
| soundfile | https://pypi.org/project/soundfile/ |

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Tienes una tarea que repites cada semana? La automatizamos: https://ayemi.org/enlaces
