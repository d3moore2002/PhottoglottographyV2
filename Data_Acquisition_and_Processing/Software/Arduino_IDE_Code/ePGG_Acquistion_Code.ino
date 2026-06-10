const int SENSOR_PIN = A0;
const unsigned long SAMPLE_INTERVAL = 200; // Sampling rate = Samples/sec (Note SAMPLE_INTERVAL in microseconds)

// 1,000,000 microseconds / SAMPLE_INTERVAL in microseconds = _ Samples/second

// CURRENT CODE 
  // 1,000,000 / 200 = 5000 Samples per second

const float VADC = 5.00; //measure the Arduino 5V pin and place the value here.
void setup() {
  // put your setup code here, to run once:
  Serial.begin(1000000); // baud rate = bits/second 

  // 10 bits per character (for Arduinos)
    // 1 Start Bit
    // 1 Character = 8 Bits
    // 1 Stop Bit
    
  // Characters/sec = Baud Rate / 10 
  
  // Current Code
    // 1,000,000 / 10 = 100,000 characters/second.

  // How many Characters are in each sample? It's in the Serial monitor
    // Like 3.22212 is 7 characters in total per sample.

  // 1000 samples/second *10 bits/character * 7 characters/sample = 70,000 Bits/sec

  //For our code
    //5000 samples/second * 10 bits/charcter * 7 characters/sample = 350,000 bits per second.
  analogReference(DEFAULT);
}

void loop() {
  // put your main code here, to run repeatedly:
  static unsigned long nextMicros = micros();
  
  // overflow-safe timing check
  if (micros() >= nextMicros) {
    int adc = analogRead(SENSOR_PIN);

    float voltage = adc * (VADC/ 1023.0f);
    Serial.println(voltage,4);
    nextMicros += SAMPLE_INTERVAL;
  }
}
