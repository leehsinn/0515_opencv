import cv2
x=int(input())
img = cv2.imread("pic/Lenna.jpg")

if x==1:
    newimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

elif x==2:
    newimg = img

elif x==3:
    newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  

cv2.imwrite(str(x)+"result.jpg",newimg)
cv2.imshow(str(x)+"result.jpg",newimg)
cv2.waitKey(0)