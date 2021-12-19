# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir) 
# from ...mediapipe
import cv2
import mediapipe as mp
import time
import math
import numpy as np
import autopy
from controller.HandTrackingModule import handDetector

wCam, hCam = 640, 480
frameR = 100
smoothening = 7



pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

delecter = handDetector(maxHands=1)
wScr,hScr = autopy.screen.size()


def virtualMouse():
    cap = cv2.VideoCapture(0)
    pTime = 0
    while True:
        # Bước 1 : tìm các điểm mốc
        # Bước 7 : di chuyển chuột
        # Bước 8 : chế độ nhấp chuột
        # Bước 9 : tìm khoảng cách giữa các ngón tay
        # Bước 10 : nhấp chuột nếu khoảng cách ngắn
        success, img = cap.read()
        img = delecter.findHands(img)
        lmList, bbox = delecter.findPosition(img)
        if len(lmList) != 0:
            # Bước 2 : lấy đầu ngón trỏ và ngón giữa
            x1,y1 = lmList[8][1:]
            x2,y2 = lmList[8][1:]
            # Bước 3 : kiểm tra ngón tay đang ở trên hay ở dưới
            finger = delecter.fingerUp()
            print(finger)
                # tạo khung màn hình
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)
            # Bước 4 : chỉ ngón trỏ và chế độ di chuyển
            if finger[1] == 1 and finger[2] == 0:
                # Bước 5 : chuyển tọa độ
                x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

                # Bước 6 : xử lý các giá trị
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening





        #fps
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # show fps on windown
        cv2.putText(img, str(int(fps)), (28,58), cv2.FONT_HERSHEY_PLAIN, 3, (255,8,8), 3)
        cv2.imshow("Migor",img)
        # no se thoat thoi vong lap  vo tan
        # hien thi khung hinh 1ms va an phim b de ket thuc
        if(cv2.waitKey(1) &  0xFF == ord("b")):
            break