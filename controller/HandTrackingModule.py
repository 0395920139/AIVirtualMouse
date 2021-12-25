# import libary
import cv2
import mediapipe as mp
import time
import math


class handDetector():
    def __init__(self,mode=False, maxHands=2 ,modelComplex=1,detectionCon=0.5,trackCon=0.5) -> None:
        ''' Hàm mặc định để ta có thể nhập các thông số cơ bản   '''
        """Initializes a MediaPipe Hand object.
    Args:
      static_image_mode: Whether to treat the input images as a batch of static
        and possibly unrelated images, or a video stream. See details in
        https://solutions.mediapipe.dev/hands#static_image_mode.
      max_num_hands: Maximum number of hands to detect. See details in
        https://solutions.mediapipe.dev/hands#max_num_hands.
      model_complexity: Complexity of the hand landmark model: 0 or 1.
        Landmark accuracy as well as inference latency generally go up with the
        model complexity. See details in
        https://solutions.mediapipe.dev/hands#model_complexity.
      min_detection_confidence: Minimum confidence value ([0.0, 1.0]) for hand
        detection to be considered successful. See details in
        https://solutions.mediapipe.dev/hands#min_detection_confidence.
      min_tracking_confidence: Minimum confidence value ([0.0, 1.0]) for the
        hand landmarks to be considered tracked successfully. See details in
        https://solutions.mediapipe.dev/hands#min_tracking_confidence.
    """
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.mediapipe.python.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        # https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/hands.py
        self.mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils
        # https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/drawing_utils.py
        self.tipIds = [4,8,12,16,20]
        # hand mold 4.THUMB_TIP( đầu Ngón cái) 8.INDEX_FINGER_TIP(đầu ngón trỏ)
        # 12.MIDDLE_FINGER_TIP(đàu ngón giữa), 16.RING_FINGER_TIP , 20.PINKY_TIP

    def findHands(self, img , Draw=True):
        ''' ở đây ta cần tìm kiếm bàn tay trong hình ảnh kết quả sẽ trả về thông tin của bàn tay '''
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # cv2.cvtColor() method is used to convert an image from one color space to another
        self.results = self.hands.process(imgRGB)
        # you have to create an object of mp_hands.Hands to get results
        # alternatively you could do: results = mp_hands.Hands().process(imgRGB)
        # ''' results.multi_hand_landmarks return True '''
        if self.results.multi_hand_landmarks:
          for handLms in self.results.multi_hand_landmarks:
            # check  hands dot  
            if Draw:
              self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
              # self.mpDraw.draw_landmarks  paint (handLms paint red color) (self.mpHands.HAND_CONNECTIONS vẽ dòng kẻ)
        return img

    # find Hands => find Position
    # 
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        # self.results.
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
              h, w, c = img.shape
              cx, cy = int(lm.x * w), int(lm.y * h)
              xList.append(cx)
              yList.append(cy)
              # print(id, cx, cy)
              self.lmList.append([id, cx, cy])
              if draw:
                  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            # hiện khung tay nè
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)
        return self.lmList, bbox
    
    # dot finger Up
    # check dau ngon tay nếu khớp cuối của ngon mà ngắn hơn khớp 2 của từng ngón thì tắt còn k thì là mở 
    def fingerUp(self):
      fingers =[]
    # Thumb
      if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
          fingers.append(1)
      else :
          fingers.append(0)
    # Fingers
      for id in range(1,5):
        if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
          fingers.append(1)
        else :
          fingers.append(0)
      return fingers
    # check khoang cach giua 2 ngon 
    def findDistance(self, p1, p2, img ,draw =True,r=15,t=3):
      x1,y1 = self.lmList[p1][1:]
      x2,y2 = self.lmList[p2][1:]
      cx,cy =(x1+x2)//2,(y1+y2)//2
      if draw:
          cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
          cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
          cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
          cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
      length = math.hypot(x2-x1,y2-y1)
      # print(length)
      return length , img, [x1,x2,y1,y2,cx,cy]
