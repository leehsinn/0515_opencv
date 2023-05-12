import cv2
def print_1():
    print("1")

def show_img():
    img = cv2.imread("pic/Lenna.jpg")
    cv2.imshow("win.jpg",img)
    cv2.waitKey(0)

def print_hello():
    print("hello")

def null():
    print("wrong")

def tryit():
    x = int(input("set number0~5"))

    selectionLists = []
    for i in range(6):
        selectionLists.append(null)
    selectionLists[1] = print_1
    selectionLists[3] = show_img
    selectionLists[5] = print_hello
    try: 
        selectionLists[x]()
    except IndexError: 
        print("set number0~5")

if __name__ == "__main__": #這個py檔要執行的部分
    tryit()