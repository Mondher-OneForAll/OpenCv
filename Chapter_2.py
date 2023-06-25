import cv2
import numpy as np

img = cv2.imread("Resources/bird.jpeg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("GrayScale", imgGray)
cv2.imshow("BlurScale", imgBlur)
cv2.imshow("CannyScale", imgCanny)
cv2.imshow("DialationScale", imgDialation)
cv2.imshow("ErodedScale", imgEroded)

while True:
    if cv2.waitKey(1) == ord('q'):
        break
