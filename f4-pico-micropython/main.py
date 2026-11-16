# Raspberry Pi Pico con MicroPython, simulada en Wokwi.
from machine import ADC, Pin, PWM
import time

perilla = ADC(Pin(26))           # GP26: entrada analógica
led = PWM(Pin(15), freq=1000)    # GP15: brillo por PWM

while True:
    valor = perilla.read_u16()   # de 0 a 65535
    led.duty_u16(valor)          # mismo rango: 0 a 65535
    print(valor, round(valor * 3.3 / 65535, 2), "V")
    time.sleep(0.2)
