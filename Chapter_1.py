import cv2

"""
#Image
img = cv2.imread("Resources/bird.jpeg")
cv2.imshow("Image", img)
cv2.waitKey(0)
"""

"""
#Video
cap = cv2.VideoCapture("Resources/ocean.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(3, 480)  # height
cap.set(10, 10)  # Brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

