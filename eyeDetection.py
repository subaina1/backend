import cv2
def eyeDetection(Face):
    face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    Alleyes = []

    eyes = face_cascade.detectMultiScale(Face, 1.8, 4)
    for (x, y, w, h) in eyes:
        cv2.rectangle(Face, (x, y), (x + w, y + h), (255, 0, 0), 2)
        eye = Face[y:y + h, x:x + w, :]
        Alleyes.append(eye)
        cv2.imshow('eyes detected', Face)
        #cv2.waitKey(10)

    return Alleyes
