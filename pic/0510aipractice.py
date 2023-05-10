import cv2
a = [[123,34,57,62,"cat"],[12,85,145,32,"dog"]]
img = cv2.imread("pic/Lenna.jpg")

def show_result(img,a):
    for turn in range(len(a)):
        point1 = (a[turn][0],a[turn][1])
        point2 = (a[turn][2],a[turn][3])
        thickness = 1
        color = (0,255,0)
        cv2.rectangle(img,point1,point2,color,thickness) #厚度
    cv2.imshow("draw",img)
    cv2.waitKey(0)

show_result(img,a)