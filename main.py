import os
import cv2
import time
import serial
from models import GazeTracker

# Constants for connection to serial port

PORT = "/dev/tty.usbmodem14201"
SERIAL = 9600

ser = serial.Serial(PORT, SERIAL)

# Thresholds for motor control

RIGHT_THRES = 0.76
LEFT_THRES = 0.38
UP_THRES = 0.69 # TBD
DOWN_THRES = 0.85 # TBD

PRINT_CYCLE = 15 # Controls arduino every 15 frames

# arduino motor control adjustment

def control_arduino_yaw(yaw):
    if yaw is None:
        return

    if yaw < LEFT_THRES:
        # os.system('turn left') #text to speech for testing movement
        print('Turn left')
        time.sleep(0.1)
        ser.write(b'L')

    elif yaw > RIGHT_THRES:
        # os.system('turn right')
        print('Turn right')
        time.sleep(0.1)
        ser.write(b'R')

    return # receive feedback from arduino

def control_arduino_pitch(pitch):
    if pitch is None:
        return

    if pitch < DOWN_THRES:
        # os.system('move down') #text to speech for testing movement
        print('Move down')
        time.sleep(0.1)
        ser.write(b'D')

    elif pitch > UP_THRES:
        # os.system('move up')
        print('Move up')
        time.sleep(0.1)
        ser.write(b'U')

    return

def main():
    DEBUG = True # Or False

    # webcam set up
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    # gaze tracker
    tracker = GazeTracker()

    frame_cnt = 0

    while True:
        frame_cnt += 1 #increases index for frame refresh

        _, frame = webcam.read()
        frame = cv2.flip(frame,1) #horizontal flip

        # inference
        eval_results = tracker.refresh(frame)
        face = eval_results.face_image
        yaw = eval_results.eye_hor_dir
        pitch = eval_results.eye_ver_dir

        # Arduino control
        if frame_cnt % PRINT_CYCLE == 0: # adjusts rate for arduino control
            arduino_res_yaw = control_arduino_yaw(yaw) # call on left-right control function based on yaw value
            arduino_res_pitch = control_arduino_pitch(pitch) # call on up-down control function based on pitch value
            
        if DEBUG:
            vis = tracker.annotated_frame()

            if face is not None:
                cv2.imshow('face', face)
            
            vis = cv2.putText(vis, str(yaw), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            vis = cv2.putText(vis, str(pitch), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            cv2.imshow('window', vis)

            key = cv2.waitKey(33) 
            if key == ord('q'):
                break
                
        print('yaw: ', yaw, '    pitch: ', pitch) # within a range of 0.0 ~ 1.0 

if __name__ == '__main__':
    main()


        

        
