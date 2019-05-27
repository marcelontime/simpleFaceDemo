import cv2
import face_recognition

cam = cv2.VideoCapture(0)

while True :
    name = "???"
    _ , frame = cam.read()

    # procura todos os face locations e face encodings no frame do video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    print(face_locations)
    print(face_encodings)

    # para cada rosto encontrado desenha um quadrado e mostra no video
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow("Camera", frame)
    if 27 == (cv2.waitKey(1) & 0xff):
        break