import cv2
import numpy as np


cap = cv2.VideoCapture(0)


myColors = [[102, 58, 126, 136, 255, 253],
            [0, 113, 90, 179, 255, 255]]

myColorsValues = [[255, 0, 0],
                  [0, 0, 255]]      ##BGR
                  

myPoints = [] ## [x, y, myColorsValues_Id]

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    i = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContour(mask)
        cv2.circle(imgResult, (x, y), 10, myColorsValues[i], cv2.FILLED)
        #cv2.imshow("Mask Webcam", mask)
      
        if x != 0 and y != 0:
            newPoints.append([x, y, i])

        i += 1
    return newPoints

def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValues[point[2]], cv2.FILLED)


while True:
    _, img = cap.read()
    imgResult = img.copy()

    newPoints = findColor(img)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints)

    cv2.imshow("Webcam", imgResult)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()