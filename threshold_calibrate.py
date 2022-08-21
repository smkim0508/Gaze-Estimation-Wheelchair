import cv2
import time
from models import GazeTracker

# optimized for calibrating threshold for motor control

def main():

    # debug true by default

    RIGHT_THRES = 0.5 # TBD
    LEFT_THRES = 0.5 # TBD
    UP_THRES = 0.5 # TBD
    DOWN_THRES = 0.5 # TBD

    # webcam set up
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1040)
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

        vis = tracker.annotated_frame()
        save = tracker.annotated_frame()

        if face is not None:
            cv2.imshow('face', face)

        if yaw and pitch is not None:
            str_yaw = '%.3f' % (yaw)
            str_pitch = '%.3f' % (pitch)
            vis = cv2.putText(vis, str_yaw, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            vis = cv2.putText(vis, str_yaw, (850, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            vis = cv2.putText(vis, str_pitch, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            vis = cv2.putText(vis, str_pitch, (850, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

            save_key = cv2.waitKey(33)
            if save_key == ord('s'):
                save = cv2.putText(save, str_yaw, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
                save = cv2.putText(save, str_pitch, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

        cv2.imshow('window', vis)
        cv2.imshow('calibration window', save)

        key = cv2.waitKey(33) 
        if key == ord('q'):
            break
                
        print('yaw: ', yaw, '    pitch: ', pitch) # 0.0 ~ 1.0 


if __name__ == '__main__':
    main()


        

        
