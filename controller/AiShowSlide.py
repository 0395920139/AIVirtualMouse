import cv2
import mediapipe as mp
import time
import math
import numpy as np
import autopy
from controller.HandTrackingModule import handDetector
import matplotlib.pyplot as plt
import globalVariable


def virtualMouse():
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
    # autopy.mouse
    cap = cv2.VideoCapture(0)
    pTime = 0
    while True:
        # Bước 1 : tìm các điểm mốc
        success, img = cap.read()
        img = delecter.findHands(img)
        lmList, bbox = delecter.findPosition(img)
        if len(lmList) != 0:
            # Bước 2 : lấy đầu ngón trỏ và ngón giữa
            x1,y1 = lmList[8][1:]
            x2,y2 = lmList[12][1:]
            x4,y4 = lmList[20][1:]
            x5,y5 = lmList[4][1:]
            # Bước 3 : kiểm tra ngón tay đang ở trên hay ở dưới
            finger = delecter.fingerUp()
            # print(finger)
                # tạo khung màn hình
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)
            # Bước 4 : chỉ ngón trỏ và chế độ di chuyển
            if finger[1] == 1 and finger[2] == 0:
                # Bước 5 : chuyển tọa độ
                x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

                # Bước 6 : xử lý các giá trị
                # global clocX,clocY,plocX,plocY
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                # Bước 7 : di chuyển chuột
                autopy.mouse.move(wScr - clocX,clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX,plocY = clocX,clocY
            # Bước 8 : chế độ nhấp chuột
            if finger[1] == 1 and finger[2] == 1 and finger[3] == 0 and finger[4] == 0 :
                # Bước 9 : tìm khoảng cách giữa các ngón tay
                length , img, lineInfo = delecter.findDistance(8,12,img)
                # Bước 10 : nhấp chuột nếu khoảng cách ngắn
                if length < 20:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click(autopy.mouse.Button.LEFT)
                    # time.sleep(0.5)
            if finger[1] == 1 and finger[2] == 0 and finger[3] == 0 and finger[4] == 1:
                autopy.mouse.click(autopy.mouse.Button.RIGHT)
                cv2.circle(img, (x5, y5), 15, (255, 0, 255), cv2.FILLED)  
                time.sleep(0.5)  
            if finger[1] == 1 and finger[2] == 1 and finger[3] == 0 and finger[4] == 1 :
                autopy.mouse.click(autopy.mouse.Button.MIDDLE)
                # autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
                cv2.circle(img, (x4, y4), 15, (255, 0, 255), cv2.FILLED)
                time.sleep(0.5)
            if finger[1] == 1 and finger[2] == 1 and finger[3] == 1 and finger[4] == 0 :
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
                cv2.circle(img, (x4, y4), 15, (255, 0, 255), cv2.FILLED)
                time.sleep(0.5)
            # if finger[1] == 1 and finger[1] == 1 and finger[2] == 1 and finger[3] == 1 and finger[4] == 1 :
            #     return "hello"    

        #fps
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # show fps on windown
        cv2.putText(img, str(int(fps)), (28,58), cv2.FONT_HERSHEY_PLAIN, 3, (255,8,8), 3)
        cv2.imshow("Migor",img)
        # globalVariable.imgShow = img
        # print(globalVariable.imgShow)
        # no se thoat thoi vong lap  vo tan
        # hien thi khung hinh 1ms va an phim b de ket thuc
        if cv2.getWindowProperty('Migor',cv2.WND_PROP_VISIBLE) < 1:  
            cv2.destroyAllWindows()      
            break 