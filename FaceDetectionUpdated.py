import cv2
import winsound
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
_,img =cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3,4)
for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
      if (cv2.rectangle!=(0,0)):
          cv2.imshow('webcam', img)
          k = cv2.waitKey(30) & 0xff
      else:
            winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
cap.release()