import torch
import cv2
import time
# from models import GazeTracker

# print(torch.__version__)

def main():
    # webcam set up
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # gaze tracker
    # gaze = GazeTracker()

    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame,1) #horizontal flip
        # gaze.refresh(frame)
        # vis, left_eye, right_eye = gaze.annotated_frame()

        cv2.imshow('window', frame)
        key = cv2.waitKey(33)
if __name__ == '__main__':
    main()