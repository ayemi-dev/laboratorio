// STM32 Blue Pill: ADC de 12 bits,
// PWM e I2C, simulado en Wokwi.
#include <Wire.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 oled(128, 64, &Wire);
const int POT = PA0;  // ADC
const int LED = PA8;  // PWM (TIM1)

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);  // 0 a 4095
  pinMode(LED, OUTPUT);
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
}

void loop() {
  int v = analogRead(POT);
  float volts = v * 3.3 / 4095;
  analogWrite(LED, v / 16);  // 0 a 255
  Serial.println(v);

  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.setTextSize(1);
  oled.setCursor(0, 0);
  oled.print("STM32  ADC 12 bits");
  oled.setTextSize(3);
  oled.setCursor(0, 12);
  oled.print(v);
  oled.setTextSize(2);
  oled.setCursor(0, 38);
  oled.print(volts, 2);
  oled.print(" V");
  int ancho = map(v, 0, 4095, 0, 124);
  oled.drawRect(0, 54, 128, 10, SSD1306_WHITE);
  oled.fillRect(2, 56, ancho, 6, SSD1306_WHITE);
  oled.display();
  delay(50);
}
