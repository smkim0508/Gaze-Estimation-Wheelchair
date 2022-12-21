#include <Servo.h> // servo library

Servo servoL; // declare servos
Servo servoR;
const int servo_l = 4; // declare pin number for servos
const int servo_r = 5;
int incomingByte; // variable to read incoming serial data
int left = 90; // baseline value to remain still
int right = 90;

void setup() {
  Serial.begin(9600);
  servoL.attach(servo_l); // attach servos to designated pins
  servoR.attach(servo_r);
}

void loop() {
  // check to see if there is incoming serial data:
  if (Serial.available() > 0) {
//    Serial.print(Serial.available());
    // read the oldest byte in serial buffer:
    incomingByte = Serial.read();
    // if user input is "left", turn left
    if (incomingByte == 'L') {
      left = 90; 
      right = 0; 
//      Serial.print("L \n");
    }
    // if user input is "right", turn right
    if (incomingByte == 'R') {
      left = 0;
      right = 90;
//      Serial.print("R \n");
    }
    // if user input is "U", move forward
    if (incomingByte == 'U') {
      left = 0;
      right = 0;
//      Serial.print("U \n");
    }
     // if user input is "D", move backwards
    if (incomingByte == 'D') {
      left = 180;
      right = 180;
//      Serial.print("D \n");
    }
    // if user input is "quit", set servo to stop
    if (incomingByte == 'Q') {
      left = 90;
      right = 90;
      Serial.print("Q \n");
    }
  }
  else {
      Serial.print("left servo: ");
      Serial.print(left);
      Serial.print('\n');
      Serial.print("right servo: ");
      Serial.print(right);
      Serial.print('\n');
  }
  servoL.write(left);
  servoR.write(right);
}
