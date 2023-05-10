import cv2

def show_rectangle():
    img = cv2.imread("pic/Lenna.jpg")
    point1 = (180,160)
    point2 = (20,50)
    thickness = 1
    color = (0,255,0)

    cv2.rectangle(img,point1,point2,color,thickness) #厚度
    cv2.imshow("draw",img)
    cv2.waitKey(0)

show_rectangle()


