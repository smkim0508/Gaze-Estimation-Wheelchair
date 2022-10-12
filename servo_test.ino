#include <Servo.h> // servo library

Servo servo;

void setup() {
  servo.attach(4); // attach servo to this pin on the arduino
}

void loop() {
  servo.write(180);

  delay(100);
   
  

}
