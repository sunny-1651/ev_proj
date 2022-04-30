import imp
import cv2
import time
from ev.lib2 import check, speak, improcess, position
from ev.dbval import dbvalue
# from d.drowsines import sleepcheck



def essence():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    while True:
        mpx = mpy = 0
        success, img = cap.read()
        # status = sleepcheck(img)
        results, img, h, w = improcess(img)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    if id ==  9:
                        mpx = cx
                        mpy = cy
                        cv2.circle(img, (cx,cy), 10, (255,0,100), cv2.FILLED)
                    
            b1 = check(0,0,w,h,mpx,mpy)
            b2 = check(w,0,0,h,mpx,mpy)
            pos = position(b1, b2)
            print(pos)
            speak(pos)
            dbvalue(pos)
        else:
            speak("No legible input")
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        img = cv2.flip(img, 1)
        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        # cv2.putText(img, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0),3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)