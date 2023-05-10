import cv2
pic=["Lenna.jpg","Dog.jpg"]
x=int(input("輸入0or1"))

img = cv2.imread(pic[x])
cv2.imshow("image",img)
cv2.waitKey(0)



