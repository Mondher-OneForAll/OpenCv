import cv2
import numpy as np 

width, height = 250, 350

img = cv2.imread("Resources/cards.jpg")

pts1 = np.float32([[475, 105], [623, 167], [368, 289], [547, 388]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgPerspective = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Image", imgPerspective)

while True:
    if cv2.waitKey(1) == ord('q'):
        break