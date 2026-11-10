import noisereduce as nr
import soundfile as sf

audio, tasa = sf.read("grabacion.wav")
ruido = audio[: 2 * tasa]  # 2 s de solo ruido
limpio = nr.reduce_noise(y=audio, sr=tasa, y_noise=ruido)
sf.write("grabacion-limpia.wav", limpio, tasa)
