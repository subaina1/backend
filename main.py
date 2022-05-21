# Import required libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import cv2
import faceDetectionDlib as FDD
import eyeDetection as EDD
import gazeFunction as GDD
from playsound import playsound
MonitoringSignal = False
#Set up Flask:
app = Flask(__name__)
#Set up Flask to bypass CORS:
cors = CORS(app)
#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
	data = request.get_json()
	#print("data from the json is ",data)
	global MonitoringSignal

	MonitoringSignal = MonitoringSignal is False
	if MonitoringSignal:
		print("FaceDetection is Enabled By teacher")
	else:
		print("FaceDetection is Disabled by Teacher")
	data = jsonify(data)
	return data
threading.Thread(target=lambda : app.run(debug=False)).start()
# Connects to your computer's default camera
cap = cv2.VideoCapture(0)
frameCounter = 0
eyesaver = 0
missingFaceThreshold = 20
while True:

	if MonitoringSignal:
		ret, frame = cap.read()
		frameCounter = frameCounter+1
		print("processed frame is ",frameCounter)
		face, error = FDD.faceDetection(frame)
		if error ==0:
			eyes = EDD.eyeDetection(face)

			for eye in eyes:
				file = "eyes/"+str(eyesaver)+".png"

				eyesaver = eyesaver+1
				#cv2.imwrite(file,eye)
				GDD.gazeFunction(eye)

		else:
			print("lenght of faces is ",len(face))
			missingFaceThreshold = missingFaceThreshold -1
			if missingFaceThreshold ==0:
				playsound("beep.wav", False)
				missingFaceThreshold = 20
		cv2.imshow('frame', frame)
		if cv2.waitKey(50) & 0xFF == ord('q'):
			break
	else:
		cv2.destroyAllWindows()
cap.release()

# Detect the coordinates
