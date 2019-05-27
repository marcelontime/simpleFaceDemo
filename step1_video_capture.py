import cv2

cam = cv2.VideoCapture(0)

while True :
    _ , frame = cam.read()
    cv2.imshow("Camera" , frame)
    if 27 == (cv2.waitKey(1) & 0xff):
        break