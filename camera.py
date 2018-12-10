import cv2
import numpy as np
cam=cv2.VideoCapture(0)
_,img,=cam.read()


while 1:
       
       _,img=cam.read()
       hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
       bluelow=np.array([99,115,150],np.uint8)
       bluehigh=np.array([110,255,255],np.uint8)
       redlow=np.array([136,87,111],np.uint8)
       redhigh=np.array([180,255,255],np.uint8)
       
       blue=cv2.inRange(hsv,bluelow,bluehigh)
       red=cv2.inRange(hsv,redlow,redhigh)

       kernal=np.ones((5,5),"uint8")

       red=cv2.dilate(red,kernal)
       res=cv2.bitwise_and(img,img,mask=red)

       blue=cv2.dilate(blue,kernal)
       res1=cv2.bitwise_and(img,img,mask=blue)

       
       (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

       for pic ,contour in enumerate(contours):
                                              area=cv2.contourArea(contour)
                                              if(area>300):
                                                          x,y,w,h=cv2.boundingRect(contour)
                                                          img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                                          cv2.putText(img,"RED COLOR",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))

       
       (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

       for pic ,contour in enumerate(contours):
                                              area=cv2.contourArea(contour)
                                              if(area>300):
                                                          x,y,w,h=cv2.boundingRect(contour)
                                                          img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                                          cv2.putText(img,"BLUE COLOR",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0))
       
       cv2.imshow("original",red)
       cv2.imshow("detector",img)
       cv2.imshow("detector1",res)
       
       if cv2.waitKey(1)==27:
                            break
cv2.destroyALLWindows()
cap.release()
