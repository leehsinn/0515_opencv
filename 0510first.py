import cv2
import numpy as np

def show_rectangle():
    img = cv2.imread("pic/Lenna.jpg")
    point1 = (180,160)
    point2 = (20,50)
    thickness = 1
    color = (0,255,0)

    cv2.rectangle(img,point1,point2,color,thickness) #厚度
    cv2.imshow("draw",img)
    cv2.waitKey(0)

def show_word():
    img = cv2.imread("pic/Lenna.jpg")
    position = (10,40)
    size = 1
    color = (0,255,255)
    lineWidth = 1
    cv2.putText(img,"HELLO", position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth,cv2.LINE_AA)
    cv2.imshow("draw",img)
    cv2.waitKey(0)
    
show_rectangle()
show_word()



