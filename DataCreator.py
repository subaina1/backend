import cv2
cap = cv2.VideoCapture(0)
frameCounter = 0
personName = "Noor"
while True:

	ret, frame = cap.read()
	frameCounter = frameCounter+1

	name = personName + "_"+str(frameCounter)+".png"
	cv2.imwrite(name,frame)
	print("processed frame is ",frameCounter)
	cv2.imshow("picture",frame)
	cv2.waitKey(1500)
