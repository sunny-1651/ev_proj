
import imp
import cv2
import numpy as np
import dlib
# from d.drowsines import compute, blinked
from imutils import face_utils



cap = cv2.VideoCapture(0)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/hemant/ev_proj/d/shape_predictor_68_face_landmarks.dat")


sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)

def compute(ptA,ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

def blinked(a,b,c,d,e,f):
    up = compute(b,d) + compute(c,e)
    down = compute(a,f)
    ratio = up/(2.0*down)

    
    if(ratio>0.25):
        return 2
    elif(ratio>0.21 and ratio<=0.25):
        return 1
    else:
        return 0

def sleepcheck(frame):
    if frame == None:
        pass
    else:
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            #The numbers are actually the landmarks which will show eye
            left_blink = blinked(landmarks[36],landmarks[37], 
                landmarks[38], landmarks[41], landmarks[40], landmarks[39])
            right_blink = blinked(landmarks[42],landmarks[43], 
                landmarks[44], landmarks[47], landmarks[46], landmarks[45])
            
            #Now judge what to do for the eye blinks
            if(left_blink==0 or right_blink==0):
                sleep+=1 
                drowsy=0
                active=0
                if(sleep>6):
                    return "SLEEPING !!!"

            elif(left_blink==1 or right_blink==1):
                sleep=0
                active=0
                drowsy+=1
                if(drowsy>6):
                    return "Drowsy !"

            else:
                drowsy=0
                sleep=0
                active+=1
                if(active>6):
                    return "Active"
