#include <Wire.h>

#define SENDER_ADDR 8 // Address of the sender ESP32

float receivedDistance = 0.0;

void setup() {
  Wire.begin(21, 22); // Initialize I2C communication as slave with SDA on GPIO 21 and SCL on GPIO 22
  Wire.onReceive(receiveEvent); // Register the receive event
  Serial.begin(115200); // Initialize serial communication
}

void loop() {
  // Your code here if you need to do something in the loop
}

void receiveEvent(int numBytes) {
  while (Wire.available() > 0) {
    Wire.readBytes((uint8_t*)&receivedDistance, sizeof(receivedDistance)); // Read the distance data sent by the sender ESP32
  }
  Serial.print("Received Distance: ");
  Serial.print(receivedDistance);
  Serial.println(" cm");
}

