#include <Servo.h> // servo library

Servo servo;
const int pin = 4; // declare pin number
int incomingByte; // variable to read incoming serial data
int curr = 90;

void setup() {
  Serial.begin(9600);
  servo.attach(pin); // attach servo to pin
}

void loop() {
  // check to see if there is incoming serial data:
  if (Serial.available() > 0) {
//    Serial.print(Serial.available());
    // read the oldest byte in serial buffer:
    incomingByte = Serial.read();
    // if user input is "left", turn left
    if (incomingByte == 'L') {
      curr = 0;
//      Serial.print("L \n");
    }
    // if user input is "right", turn right
    if (incomingByte == 'R') {
      curr = 180;
//      Serial.print("R \n");
    }
    // if user input is "U", move up
    if (incomingByte == 'U') {
      curr = 90;
//      Serial.print("U \n");
    }
     // if user input is "D", move down
    if (incomingByte == 'D') {
      curr = 45;
//      Serial.print("D \n");
    }
//    Serial.println(incomingByte);
  }
  else {
//    Serial.print("no serial available");
//    Serial.print('\n'); 
      Serial.print(curr);
      Serial.print('\n');
  }
  servo.write(curr);
}
