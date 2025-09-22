import cv2

cap = cv2.VideoCapture("Videos/vid1.mp4", cv2.CAP_ANY)

while (True):
    ret, frame = cap.read()
    if not(ret):
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap = cv2.VideoCapture("Videos/vid2.gif", cv2.CAP_ANY)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not(ret):
        break
    cv2.imshow('frame', gray)
    if cv2.waitKey(15) & 0xFF == 27:
        break