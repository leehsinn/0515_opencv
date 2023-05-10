import cv2

def show_circle(center,color):
    img = cv2.imread("pic/Lenna.jpg") #圖片放在pic資料夾
    originImg = img.copy() #畫圖前先copy
    radius = 10
    cv2.circle(img,center,radius,color,-1) #厚度
    cv2.imshow("draw",img)
    cv2.imshow("draw0",originImg) #copy的原版
    cv2.waitKey(0)

setcenter = (160,180) #先欄column 再列row
setcolor = (255,0,0)
show_circle(setcenter,setcolor)


