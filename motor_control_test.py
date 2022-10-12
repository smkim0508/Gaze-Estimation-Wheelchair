import serial

print(serial.__version__)

PORT = "COM4"
SERIAL = 9600

ser = serial.Serial(PORT, SERIAL)

def test():
    user_input = input("\n Command Motor forward / backward / quit : ")

    if user_input == forward:
        print("Turning motor forwards")
        time.sleep(0.1)
        ser.write(b'H')
        test()

    elif user_input == backward:
        print("Turning motor backwards")
        time.sleep(0.1)
        ser.write(b'H')
        test()

    elif user_input == "q" or user input == "quit":
        print("Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.close()
    
    else:
        print("Invalid input")
        test()

time.sleep(2) # allow arduino connections to calibrate

test()
