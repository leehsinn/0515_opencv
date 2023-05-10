import cv2

a = [[123,34,57,62,"cat"],[12,85,145,32,"dog"]]
img = cv2.imread("pic/Lenna.jpg")

def draw_rectangle(turn,img):
    point1 = (turn[0],turn[1])
    point2 = (turn[2],turn[3])
    thickness = 1
    color = (255,0,0)
    cv2.rectangle(img,point1,point2,color,thickness) 

def draw_text(w,name,img):
    newString = str(w)+name
    position = (w*50,w*50)
    size = 1
    color = (0,255,255)
    lineWidth = 1
    cv2.putText(img,newString, position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth,cv2.LINE_AA)

def show_result(img,a,isSave):
    w=0
    for turn in a:
        w+=1
        if isSave:
            draw_rectangle(turn,img)
            draw_text(w,turn[4],img)
            cv2.imshow("draw",img) #for一次就顯示一次
            cv2.waitKey(0)
            if isSave:  
                cv2.imwrite(str(w)+".jpg",img)

isSave = input("True or False")
show_result(img,a,isSave)