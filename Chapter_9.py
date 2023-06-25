import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#img = cv2.imread("Resources/face.jpg")
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = imgGray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eyeCascade.detectMultiScale(roi_gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    cv2.imshow("Face Image", img)
    if cv2.waitKey(1) == ord('q'):
        break