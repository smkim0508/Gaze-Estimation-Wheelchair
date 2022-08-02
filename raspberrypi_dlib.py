import time
from models import GazeTracker

def draw_eye(frame, eye, left=True):
    EYE_HEIGHT = 60
    EYE_WIDTH = EYE_HEIGHT * 2

    eye = cv2.cvtColor(eye, cv2.COLOR_GRAY2BGR)
    eye = cv2.resize(eye, (EYE_WIDTH, EYE_HEIGHT))

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

    #gaze tracker
    tracker = GazeTracker()

    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame, 1) #horizontal flip

        #inference
        eval_result = tracker.refresh(frame)
        vis = tracker.annotated_frame()

        l_eye = eval_result.left_eye_image
        r_eye = eval_result.right_eye_image
        face = eval_result.face_image

        if l_eye is not None:
            cv2.imshow('l_eye', l_eye)
        if r_eye is not None:
            cv2.imshow('r_eye', r_eye)
        if face is not None: 
            cv2.imshow('face', face)
        
        cv2.imshow('window', vis)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
        
if __name__ == '__main__':
    main()

    