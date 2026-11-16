# D4 · Subtítulos traducidos con Python (Whisper y ffmpeg)

Ejemplo real de cómo generar subtítulos con tiempos usando **Whisper** (`openai-whisper`), traducirlos al español sin mover los tiempos y quemarlos en un video con **ffmpeg**.

## Comandos

```text
python -m pip install -U openai-whisper
whisper hotaru.ogg --language Japanese -f srt
ffmpeg -i hotaru.mp4 -vf subtitles=es.srt final.mp4
```

- `python -m pip install -U openai-whisper`: instala Whisper (requiere tener `ffmpeg` instalado en el sistema).
- `whisper hotaru.ogg --language Japanese -f srt`: transcribe la canción en japonés y genera `hotaru.srt` con sus tiempos (usa el modelo `turbo` por defecto; `turbo` no traduce).
- `ffmpeg -i hotaru.mp4 -vf subtitles=es.srt final.mp4`: quema los subtítulos traducidos (`es.srt`) en el video.

## Archivos incluidos

- `hotaru.srt`: transcripción original generada por Whisper sobre la grabación de dominio público.
- `es.srt`: traducción al español línea por línea, respetando los mismos tiempos de `hotaru.srt` y partiendo de la letra corregida a mano.

*(No se incluyen archivos de audio ni de video.)*

## Aviso de derechos de autor

Las canciones tienen derechos de autor: usa música tuya, de la Biblioteca de audio de YouTube o con permiso. Ponerle subtítulos a una canción ajena no te da permiso de usarla.

## Crédito de la grabación de prueba

- **Grabación de «Hotaru no Hikari»:** Wikimedia Commons, dominio público (versión original de 2008):
  https://commons.wikimedia.org/wiki/File:Hotaru_no_Hikari(Auld_lang_syne_in_Japan).ogg

## Fuentes

- Whisper (repositorio oficial): https://github.com/openai/whisper
- YouTube · Derechos de autor: https://support.google.com/youtube/answer/2797466?hl=es-419
- YouTube · Biblioteca de audio: https://support.google.com/youtube/answer/3376882?hl=es-419
- Meta · Pautas de música: https://www.facebook.com/legal/music_guidelines
- Wikimedia Commons · Archivo de audio (dominio público): https://commons.wikimedia.org/wiki/File:Hotaru_no_Hikari(Auld_lang_syne_in_Japan).ogg
