// Termómetro con ESP32: DHT22 en el pin 15 y pantalla OLED SSD1306 por I2C (SDA 21, SCL 22).
// Laboratorio Ayemi · c-termometro-oled · Código MIT.
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHTesp.h>

Adafruit_SSD1306 oled(128, 64, &Wire, -1);
DHTesp dht;

void setup() {
  Serial.begin(115200);
  dht.setup(15, DHTesp::DHT22);
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  oled.setTextColor(SSD1306_WHITE);
  Serial.println("Termometro listo: DHT22 y OLED");
}

void loop() {
  TempAndHumidity d = dht.getTempAndHumidity();
  if (dht.getStatus() != 0) {
    Serial.println(dht.getStatusString());
  } else {
    Serial.printf("Temperatura: %.1f C, humedad: %.1f %%\n", d.temperature, d.humidity);
    oled.clearDisplay();
    oled.setTextSize(1);
    oled.setCursor(0, 0);
    oled.print("Temperatura");
    oled.setTextSize(2);
    oled.setCursor(0, 12);
    oled.print(d.temperature, 1);
    oled.print(" C");
    oled.setTextSize(1);
    oled.setCursor(0, 36);
    oled.print("Humedad");
    oled.setTextSize(2);
    oled.setCursor(0, 48);
    oled.print(d.humidity, 1);
    oled.print(" %");
    oled.display();
  }
  delay(dht.getMinimumSamplingPeriod());
}
