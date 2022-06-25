import torch
import cv2
import time
from models import GazeTracker

# print(torch.__version__)

def draw_eye(frame, eye, left=True)
    EYE_HEIGHT = 60
    EYE_WIDTH = EYE_HEIGHT * 2

    eye = cv2.cvtColor(eye, cv2.COLOR_GRAY2BGR)
    eye = cv2.resize(eye,(EYE_WIDTH, EYE_HEIGFHT))

    if left:
        frame[0:EYE_HEIGHT, 0:EYE_WIDTH, :] = eye
    else: #right
        frame[0:EYE_HEIGHT, EYE_WIDTH:2*EYE_WIDTH, :] = eye
    
    return frame

def main():
    # webcam set up
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # gaze tracker
    gaze = GazeTracker()

    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame,1) #horizontal flip
        gaze.refresh(frame)
        vis, left_eye, right_eye = gaze.annotated_frame()

        if left_eye is not None:
            frame = draw_eye(vis, left_eye, left=True)
        if right_eye is not None:
            frame = draw_eye(frame, right_eye, left=False)

        cv2.imshow('window', frame)
        key = cv2.waitKey(33)

        if key == ord('q'):
            break

if __name__ == '__main__':
    main()