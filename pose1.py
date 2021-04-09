import cv2
import mediapipe as mp
import os
import time
import posemodule as pm

pTime = 0
path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'video1.mp4'
cap = cv2.VideoCapture(path)
detector = pm.poseDetector()



while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist = detector.getPosition(img,draw=False)
    print(lmlist[14])
    cv2.circle(img,(lmlist[14][1],lmlist[14][2]),10,(0,0,255),cv2.FILLED)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)