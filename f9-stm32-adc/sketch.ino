// STM32 Blue Pill: lee un potenciometro con el ADC
// y muestra el valor y el porcentaje en el monitor serie.
const int POT = PA0;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);  // 0 a 4095
}

void loop() {
  int valor = analogRead(POT);
  int porcentaje = map(valor, 0, 4095, 0, 100);
  Serial.print(valor);
  Serial.print("  ");
  Serial.print(porcentaje);
  Serial.println(" %");
  delay(250);
}
