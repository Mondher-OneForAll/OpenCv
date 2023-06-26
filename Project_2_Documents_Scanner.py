import cv2
import numpy as np
import utils as ut

imgWidth = 480
imgHeight = 640

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def imgProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 100, 200)  # Threshold choice very important
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=2)
    imgErode = cv2.erode(imgDilate, kernel, iterations=1)

    return imgErode


def getContour(img):
    bigEst = np.array([])
    maxArea = 0
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if area > maxArea and len(approx) == 4:
                bigEst = approx
                maxArea = area
    # cv2.drawContours(imgContour, bigEst, -1, (255, 0, 0), 20)
    return bigEst


def reOrder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myNewPoints = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    myNewPoints[0] = myPoints[np.argmin(add)]
    myNewPoints[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myNewPoints[1] = myPoints[np.argmin(diff)]
    myNewPoints[2] = myPoints[np.argmax(diff)]

    return myNewPoints


def getWarp(img, bigEst):
    # print(bigEst.shape)
    bigEst = reOrder(bigEst)
    pts1 = np.float32(bigEst)
    pts2 = np.float32([[0, 0], [imgWidth, 0], [0, imgHeight], [imgWidth, imgHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (imgWidth, imgHeight))

    # imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20] # Too much Croppe
    imgCropped = cv2.resize(imgOutput, (imgWidth, imgHeight))

    return imgCropped


while True:
    _, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight))
    imgContour = img.copy()
    imgThreshold = imgProcessing(img)
    bigEst = getContour(imgThreshold)
    if bigEst.size != 0:
        imgWarped = getWarp(img, bigEst)
        cv2.imshow("ImageWarped", imgWarped)
        imgArray = ([img, imgThreshold],
                    [imgContour, imgWarped])
    else:
        imgArray = ([img, imgThreshold],
                    [img, img])

    stackedImages = ut.stackImages(0.5, imgArray)

    cv2.imshow("WorkFlow", stackedImages)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
