import cv2
from playsound import playsound
def faceDetection(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.3, 4)
    AllFaces = []
    face = None
    for (x, y, w, h) in faces:
        cv2.circle(img,(x,y),5,(255,0,0),5)
        cv2.circle(img,(x+w,y+h),5,(0,0,255),5)
        face = img[y:y + h,x:x + w,  :]
        AllFaces.append(face)
        facex, facey, _ = face.shape
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if len(faces) == 1:
            return face
    cv2.imshow('webcam', img)
    #cv2.waitKey(10)
    # print("length of faces is ",len(faces))
    if len(faces) == 1:
        pass
    elif len(faces)>1:
        print("More than one person detected")






