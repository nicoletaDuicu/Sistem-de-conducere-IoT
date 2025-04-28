#define LED_PIN 9  // <-- Aceasta linie este esențială!

void setup() {
  Serial.begin(9600);         
  pinMode(LED_PIN, OUTPUT);   // Setăm pinul ca OUTPUT
  Serial.println("Trimite 'A' pentru aprindere, 'S' pentru stingere");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'A') {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED aprins");
    }
    else if (command == 'S') {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED stins");
    }
    else {
      Serial.println("Comanda necunoscuta");
    }
  }
}
