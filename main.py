import cv2
import time
from models import GazeTracker

def main():
    DEBUG = True # Or False

    RIGHT_THRES = 0.5 # TBD
    LEFT_THRES = 0.5 # TBD
    UP_THRES = 0.5 # TBD
    DOWN_THRES = 0.5 # TBD

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
        face = eval_results.face_image
        yaw = eval_results.eye_hor_dir
        pitch = eval_results.eye_ver_dir

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
                
        print('yaw: ', yaw, '    pitch: ', pitch) # 0.0 ~ 1.0 

        if yaw is not None:
            if yaw < LEFT_THRES: # Threshold for left turn
                pass
                # turn left
                # arduino control function()
            elif yaw > RIGHT_THRES: # Threshold for right turn
                pass
                # turn right
                # arduino control function()

        if pitch is not None:
            if pitch < DOWN_THRES:
                pass
                # adjust turn downwards

            elif pitch > UP_THRES:
                pass
                # adjust turn upwards

if __name__ == '__main__':
    main()


        

        
