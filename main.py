import cv2
import time
from models import GazeTracker

def main():
    DEBUG = True #False

    # webcam set up
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    # gaze tracker
    tracker = GazeTracker()

    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame,1) #horizontal flip

        # inference
        eval_results = tracker.refresh(frame)
        face = eval_result.face_image
        yaw - eval_result.eye_hor_dir

        if DEBUG:
            vis = tracker.annotated_frame()

            if face is not None:
                cv2.imshow('face', face)
            
            vis = cv2.putText(vis, str(yaw), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            cv2.imshow('window', vis)

            key = cv2.waitKey(33) 
            if key == ord('q'):
                break
                
        print(yaw)

        

        
