import cv2
import mediapipe as mp
import os
import time


class poseDetector():
    def __init__(self,mode= False, upBody =False,smooth = True,detectionCon = 0.5,trackCon=0.5):
            

                self.mode = mode
                self.upBody = upBody
                self.smooth = smooth
                self.detectionCon = detectionCon
                self.trackCon = trackCon

                self.mpDraw = mp.solutions.drawing_utils

                self.mpPose = mp.solutions.pose
                self.pose = self.mpPose.Pose()
                


    def findPose(self,img,draw = True):
    
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img
        

    def getPosition(self,img,draw =True):
        lmlist = []
        if self.results.pose_landmarks:

            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h, w ,c = img.shape
                cx,cy = int(lm.x*w) ,int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
            

        return lmlist


    

def main():
    pTime = 0
    path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'video1.mp4'
    cap = cv2.VideoCapture(path)
    detector = poseDetector()
    
    

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.getPosition(img,draw=False)
        if(len(lmlist)!=0):
        print(lmlist[14])
        cv2.circle(img,(lmlist[14][1],lmlist[14][2]),10,(0,0,255),cv2.FILLED)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
        (255,0,0),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
