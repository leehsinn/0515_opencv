import cv2
import numpy as np #要使用numpy套件的array,太長縮寫


img = cv2.imread("pic/Lenna.jpg")
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
# 網路上的人認為是紅色的區域

m = cv2.inRange(hueImage, lowRange, highRange)
cv2.imshow('mask', m)
res = cv2.bitwise_and(img, img, mask=m) #順序3C 3C 1C
cv2.imshow('Input', img)
cv2.imshow('Result', res)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("Input",cv2.WND_PROP_VISIBLE)<=0:
        break