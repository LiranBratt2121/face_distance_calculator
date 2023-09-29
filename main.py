import cv2
from utils import distance_finder

cap = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier(
    r'cascades\haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(frame, f'Distance: {distance_finder(x+w):.2f} cm',
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
