import cv2
import numpy as np

img = cv2.imread("Resources/kings.jpg")
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))
cv2.imshow("Horizenatl Stack", imgHor)
cv2.imshow("Vertical Stack", imgVer)
while True:
    if cv2.waitKey(1) == ord('q'):
        break

    