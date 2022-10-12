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
    // if user input is "forward", turn servo in positive direction
    if (incomingByte == 'F') {
      curr = 0;
//      Serial.print("F \n");
//      Serial.print(incomingByte);
//      Serial.print('\n');
    }
    // if user input is "backward", turn servo in negative direction
    if (incomingByte == 'B') {
      curr = 180;
      Serial.print("B \n");
    }
    // if user input is "quit", set servo to stop
    if (incomingByte == 'Q') {
      curr = 90;
      Serial.print("Q \n");
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
