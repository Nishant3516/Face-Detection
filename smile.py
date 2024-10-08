import cv2

face_casscade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_casscade = cv2.CascadeClassifier("haarcascade_smile.xml")
smile_casscade = cv2.CascadeClassifier("haarcascade_smile.xml")


def detect(gray, frame):
    faces = face_casscade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_frame = frame[y : y + h, x : x + w]
        eyes = eye_casscade.detectMultiScale(roi_gray, 1.1, 3)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        smiles = smile_casscade.detectMultiScale(roi_gray, 1.7, 22)
        for sx, sy, sw, sh in smiles:
            cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
    return frame


video_capt = cv2.VideoCapture(0)
while True:
    _, frame = video_capt.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow("Video", canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capt.release()
cv2.destroyAllWindows()
