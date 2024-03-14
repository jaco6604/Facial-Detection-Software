import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(1)

while True:
    # This is for capturing frames
    ret, frame = video_capture.read()
    # This is to convert into grayscale to make processing easier
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # This is to detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # This is to draw circles around faces
    for (x, y, w, h) in faces:
        center_coordinates = x + w // 2, y + h // 2
        radius = h // 2  # or can be h / 2 or can be anything based on your requirements
        cv2.circle(frame, center_coordinates, radius, (0, 0, 100), 3)


    # This is to display frames from the camera
    cv2.imshow('Video', frame)

    #  This is to break the loop with the 'w' key
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

video_capture.release()
cv2.destroyAllWindows()