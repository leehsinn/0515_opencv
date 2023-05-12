import cv2

img = cv2.imread("pic/Lenna.jpg")
h,w,c = img.shape
print("w is "+str(w)+",h is "+str(h)+",c is "+str(c))
#w是長 h是寬 c是RGB

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img[30][30]) #取該PIXEL的RGB