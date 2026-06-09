const int SENSOR_PIN = A0;
const unsigned long SAMPLE_INTERVAL_US = 2000; // Sampling interval: 2000 µs = 2 ms = 500 Hz (samples/second)

unsigned long lastSample = 0;

void setup() {
  Serial.begin(500000);
  delay(3000);
}

void loop() {
  unsigned long now = micros();

  if (now - lastSample >= SAMPLE_INTERVAL_US) {
    lastSample += SAMPLE_INTERVAL_US;

    int raw = analogRead(SENSOR_PIN);
    Serial.println(raw);
  }
}
