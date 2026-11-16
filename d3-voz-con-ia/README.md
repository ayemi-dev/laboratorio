# La voz de un cantante con IA: cómo se hace (y regla de permiso)

Guía breve con los comandos verificados para separar la voz de una pista de audio con Demucs (Python) y las referencias oficiales sobre conversión de voz y divulgación de contenido generado con IA.

## Requisitos

- Python 3.10 o más reciente.
- FFmpeg disponible para lectura y mezcla de audio.

## Comandos para separar la voz con Demucs

1. Instala Demucs en un entorno virtual de Python:

```bash
python -m pip install -U demucs
```

2. Separa la pista vocal del resto del acompañamiento en CPU:

```bash
demucs --two-stems=vocals -d cpu mezcla-d3.mp3
```

Los archivos resultantes se guardan en `separated/htdemucs/<nombre-de-pista>/` (`vocals.wav` y `no_vocals.wav`).

## Regla de permiso y divulgación

- Usa estas herramientas **solo con tu propia voz o con el permiso explícito** de la persona titular de la voz y del audio original.
- Al publicar contenido sintético o alterado que parezca realista, **márcalo como generado o alterado con IA** en cada plataforma (YouTube, TikTok, Instagram, Facebook y X).

## Fuentes oficiales

| Recurso | Enlace |
|---|---|
| Demucs (repositorio mantenido) | https://github.com/adefossez/demucs |
| RVC (documentación en inglés) | https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/docs/en/README.en.md |
| YouTube · Divulgación de contenido sintético | https://support.google.com/youtube/answer/14328491?hl=es-419 |
| TikTok · Normas de contenido editado y con IA | https://www.tiktok.com/community-guidelines/en/integrity-authenticity |

---
Guía: CC BY-SA 4.0 · ¿Tienes una tarea que repites cada semana? La automatizamos: https://ayemi.org/enlaces
