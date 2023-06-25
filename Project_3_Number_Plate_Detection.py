import cv2
import numpy as np

numberPlatesCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)
count = 0

cap = cv2.VideoCapture("http://192.168.0.23:8080/video")

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = numberPlatesCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

            imgRoi = img[y: y + h, x: x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("Resources/ScannedRussianCarsPlates/NumberPlates_" + str(count) +".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Webcam", img)
        cv2.waitKey(500)
        count += 1

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()