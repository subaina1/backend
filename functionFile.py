import cv2
def displayVideo():
    capture = cv2.VideoCapture(0)
    _, img = capture.read()
    cv2.imshow("Camera feed", img)
    cv2.waitKey(0)
    capture.release()
    cv2.destroyAllWindows()

def getVideo():

    cap = cv2.VideoCapture(0)
    while(True):
        ret, img = cap.read()
        if ret== False:
            print("Failed")
        else:
            pass
            #print("success")
        cv2.imshow("Output", img)
        if cv2.waitKey(10) == -1:
            #print("-1 is ok capture more frames")
            pass
        else:
            print("Some other key press so stop capturing ")
            cap.release()
            break
# cv2.destroyAllWindows()


def minusOneDetector(word):
    if word == -1:
        print("passed")
    else:
        print("failed")

def evenodd(word):
    check = 10
    if (type(word)== type(check)):
     if word % 2==0:
        print(word,"is an even number")
        i = word
        while i > 0 :
            print(i)
            i -= 2
     else :
        print (word,"is an odd number")
        i = word
        while i > 0 :
            print(i)
            i -= 2
    else:
        print("this is an invalid input!")








def displayImage():
    img = cv2.imread("test.png" , cv2.IMREAD_GRAYSCALE)
    cv2.imshow("screen", img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

def readFile():
    fr = open("read.txt","r")
    print(fr.read())

def writeFile():
    fw = open("write.txt","w+")
    fw.write("hey there")
    fw.close()

def subaddfunction (a,b):
    return (a+b,a-b)

def divide(a,b):
    if b== 0:
        return False, 0
    else:
        return True, a/b

def testingFunctionParameters(a,b):
    mul = a+b
    return mul









