def gazeDetection(eye):
    import cv2
    import numpy as np
    frame = cv2.imread('test.png')
    # cap = cv2.VideoCapture(0)
    cv2.imshow('image', frame)
    # cv2.setMouseCallback('image', click_event)
    # print("main function x and y is ",x,y)
    cv2.waitKey(10)
    while True:
        # ret, frame = cap.read()

        # roi = frame[168: 193, 523: 567]
        roi = frame[171: 201, 118: 177]

        rows, cols, _ = roi.shape
        print("rows are ", rows)
        print("cols are ", cols)

        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)
        # for (ex)
        _, threshold = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            #    cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
            break

        cv2.imshow("Threshold", threshold)
        cv2.imshow("gray roi", gray_roi)
        cv2.imshow("Roi", roi)
        key = cv2.waitKey(0)
        if key == 27:
            break
    cv2.destroyAllWindows()
