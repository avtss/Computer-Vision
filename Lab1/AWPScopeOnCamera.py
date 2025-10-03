import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    x, y = w // 2, h // 2
    r = 200

    Y, X = np.ogrid[:h, :w]
    mask = (X- x) ** 2 + (Y - y) ** 2 >= r ** 2

    frame[mask] = 0
    cv2.circle(frame, (x, y), r, (0, 0, 0), 2)

    cv2.line(frame, (0, y), (w, y), (0, 0, 0), 2)
    cv2.line(frame, (x, 0), (x, h), (0, 0, 0), 2)

    cv2.imshow("Sniper Scope", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
