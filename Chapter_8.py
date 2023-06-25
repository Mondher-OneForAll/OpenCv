import cv2
import numpy as np
import utils as ut

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        print(len(approx))


        objCor = len(approx)
        x, y , w, h = cv2.boundingRect(approx)
        objectType = "None"
        if objCor == 3: 
            objectType = "Triangle"
        elif objCor == 4:
            aspRatio = w / float(h)
            if aspRatio > 0.95 and aspRatio < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif objCor == 5:
            objectType = "Pentagon"
        elif objCor == 6: 
            objectType = "Hexagon"
        elif objCor == 8: 
            objectType = "Circle"
        elif objCor == 12:
            objectType = "Star"

        
        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(imgContour, objectType, (x + (w // 2) - 20, y + (h // 2) - 5), 
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        


img = cv2.imread("Resources/2d-shapes.png")
img = cv2.resize(img, (640, 480))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur,50, 50)
imgBlank = np.zeros_like(img)
imgContour = img.copy()

getContours(imgCanny)

imgStack = ut.stackImages(0.65, ([img, imgGray, imgBlur],
                                [imgCanny, imgContour, imgBlank]))


cv2.imshow("Stacked Images", imgStack)
while True:
    if cv2.waitKey(1) == ord('q'):
        break