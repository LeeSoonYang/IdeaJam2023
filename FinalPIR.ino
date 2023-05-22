const int pirPin = 8;       // PIR sensor connected to digital pin 2
unsigned int counter = 0;   // Counter to track the number of detections

void setup() {
  Serial.begin(9600);      // Initialize serial communication
  pinMode(pirPin, INPUT);  // Set PIR sensor pin as input
}

void loop() {
  if (digitalRead(pirPin) == HIGH) {  // If motion is detected by PIR sensor
    counter++;                       // Increment the counter
    Serial.print("Counter: ");
    Serial.println(counter);
    delay(5000);                     // Wait for 5 seconds
  }
}

