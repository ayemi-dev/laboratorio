#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include <Adafruit_SSD1306.h>

// Temperatura actual de la CDMX
const char* URL =
  "http://api.open-meteo.com/v1/forecast"
  "?latitude=19.43&longitude=-99.13"
  "&current=temperature_2m";

DHT dht(15, DHT22);
Adafruit_SSD1306 oled(128, 64, &Wire);

float cdmx() {
  HTTPClient http;
  http.begin(URL);
  float t = NAN;
  if (http.GET() == 200) {
    String r = http.getString();
    int i = r.lastIndexOf("_2m\":");
    t = r.substring(i + 5).toFloat();
  }
  http.end();
  return t;
}

void mostrar(const char* donde, float t) {
  oled.print(donde);
  oled.print(t, 1);
  oled.println("C");
}

void setup() {
  Serial.begin(115200);
  WiFi.begin("Wokwi-GUEST", "", 6);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
  }
  Serial.println("Wi-Fi conectado");
  dht.begin();
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  oled.setTextColor(WHITE);
  oled.setTextSize(2);
}

void loop() {
  float aqui = dht.readTemperature();
  float afuera = cdmx();
  Serial.printf("Aqui %.1f C | CDMX %.1f C\n",
                aqui, afuera);
  oled.clearDisplay();
  oled.setCursor(0, 8);
  mostrar("Aqui ", aqui);
  oled.setCursor(0, 40);
  mostrar("CDMX ", afuera);
  oled.display();
  delay(10000);
}
