import serial
import time

print(serial.__version__)

PORT = "/dev/tty.usbmodem142101"

SERIAL = 9600

ser = serial.Serial(PORT, SERIAL)

def test():
    user_input = input("\n Command Motor left / right / forward / backward / stop / quit : ")

    if user_input == "left":
        print("Turning left")
        # time.sleep(0.1)
        ser.write(b'L')
        test()

    if user_input == "right":
        print("Turning right")
        # time.sleep(0.1)
        ser.write(b'R')
        test()

    if user_input == "forward":
        print("Turning motor forwards")
        # time.sleep(0.1)
        ser.write(b'U')
        test()

    elif user_input == "backward":
        print("Turning motor backwards")
        # time.sleep(0.1)
        ser.write(b'D')
        test()
    
    elif user_input == "stop":
        print("Stopping motor")
        # time.sleep(0.1)
        ser.write(b'Q')
        test()

    elif user_input == "q" or user_input == "quit":
        print("Exiting Program")
        # time.sleep(0.1)
        ser.write(b'Q')
        ser.close()
    
    else:
        print("Invalid input")
        test()

time.sleep(2) # allow arduino connections to calibrate

test()
