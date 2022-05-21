import cv2
import dlib
import gazeTest as gaze
detector = dlib.get_frontal_face_detector()

# Capture frames continuously

def faceDetection(frame):

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)
	gaze.gaze(frame,gray,faces)
	#gaze.gazeFunction(faces)
	face = frame[0:0,0:0]
	if len(faces)== 1:
		# Iterator to count faces
		i = 0
		for face in faces:

			# Get the coordinates of faces
			x, y = face.left(), face.top()
			x1, y1 = face.right(), face.bottom()
			cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

			face = frame[ y:y1,x:x1]
			#cv2.imshow("face ",face)
			# Increment iterator for each face in faces
			i = i+1

			# Display the box and faces
			cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			#print(face, i)
			return face, 0
	else:

		return face, -1





