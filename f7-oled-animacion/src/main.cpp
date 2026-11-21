#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "cuadros.h"

Adafruit_SSD1306 oled(128, 64, &Wire, -1);
uint8_t n = 0;

void setup() {
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
}

void loop() {
  oled.clearDisplay();
  oled.drawBitmap(0, 0, cuadros[n], 128, 64, SSD1306_WHITE);
  oled.display();
  n = (n + 1) % NUM_CUADROS;
  delay(80);
}
