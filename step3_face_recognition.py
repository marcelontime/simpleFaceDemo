import cv2
import face_recognition
from imutils import paths
import os
import numpy as np

cam = cv2.VideoCapture(0)

imagePaths = list(paths.list_images("./images"))
known_faces_encodings = []
known_faces_names = []

# carrega imagens do diretorio ./images extrai os encoding e nomes
for img_path in imagePaths:
    name = img_path.split(os.path.sep)[-1].split(".")[0]
    img = cv2.imread(img_path)
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    known_faces_encodings.append(face_encodings[0])
    known_faces_names.append(name)


while True :
    name = "???"
    _ , frame = cam.read()

    # procura todos os face locations e face encodings no frame do video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # para cada rosto encontrado desenha um quadrado e mostra no video
    for (top, right, bottom, left),face_encoding in zip(face_locations,face_encodings):
        # compara o encoding da face da camera com faces conhecidas
        # essa funcao retorna um float entre 0.0 e 1.0 quanto menor o numero ,
        # mais similiar a face eh .
        face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)

        # pega a face que teve a menor distancia pois ser a face mais similar.
        match_index = np.argmin(face_distances)
        # O threshold abaixo de 0.6 indica que a pessoa eh similar a da foto
        if face_distances[match_index] < 0.65:
            print(known_faces_names[match_index])
            name = known_faces_names[match_index]
        else :
            name = "???"

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)


    cv2.imshow("Camera", frame)
    if 27 == (cv2.waitKey(1) & 0xff):
         break