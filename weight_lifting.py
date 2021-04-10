import cv2
import mediapipe as mp
import os
import time
import posemodule as pm
import math

def biceps(n):
    pTime = 0
    path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'weight lifting 1.mp4'
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()

    #up3 y500
    # down 1000
    # up15 1100
    #  down 1100
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


    count = 0

    f=0
    while True and count<n:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.getPosition(img, draw= False)
        #print(lmlist[3])
        
        if len(lmlist)!=0:
            cv2.circle(img,(lmlist[17][1],lmlist[17][2]),20,(0,0,255),cv2.FILLED)
            cv2.circle(img,(lmlist[13][1],lmlist[13][2]),20,(0,255,0),cv2.FILLED) 
            y1 = lmlist[17][2]
            y2 = lmlist[13][2]
            
            length = y2-y1
            if length>=0 and f==0:
                f=1
            elif length<0 and f==1:
                f=0
                count=count+1


            print(length)

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            cv2.putText(img,str(int(count)),(70,150),cv2.FONT_HERSHEY_PLAIN,10,
            (60,100,255),3)
            img = cv2.resize(img, (600,600))                    # Resize image
            cv2.imshow("Image",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                break
            
            
            calories = 0.4*count
        
        
        
    return count,calories
