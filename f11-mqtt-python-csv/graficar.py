# Lee lecturas.csv y dibuja la temperatura
# y la humedad en grafica.png.
import csv
import matplotlib.pyplot as plt

horas, temperaturas, humedades = [], [], []
with open("lecturas.csv", newline="") as f:
    for fila in csv.DictReader(f):
        horas.append(fila["hora"])
        temperaturas.append(float(fila["temperatura"]))
        humedades.append(float(fila["humedad"]))

fig, (arriba, abajo) = plt.subplots(2, 1, sharex=True)
arriba.plot(horas, temperaturas, marker="o", color="r")
arriba.set_ylabel("Temperatura (°C)")
abajo.plot(horas, humedades, marker="o", color="b")
abajo.set_ylabel("Humedad (%)")
abajo.tick_params(axis="x", labelrotation=45)
fig.tight_layout()
fig.savefig("grafica.png", dpi=150)
print("Guardada grafica.png con", len(horas), "lecturas")
