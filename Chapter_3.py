import cv2

img = cv2.imread("Resources/bird.jpeg")
print(img.shape)

imgResize = cv2.resize(img, (640, 480))
print(imgResize.shape)

imgCropped = imgResize[0:229, 175:345]

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

while True:
    if cv2.waitKey(1) == ord('q'):
        break