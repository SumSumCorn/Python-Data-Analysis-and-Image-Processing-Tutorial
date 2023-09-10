# Mediapipe를 통해 몸의 포즈를 잡아내는 기본 프로그램
# https://www.youtube.com/watch?v=CvuwMqhFtbc 댄스영상으로 테스트 

import cv2
import mediapipe as mp   # py -m pip install mediapipe
import time

mpDraw = mp.solutions.drawing_utils  # 랜드마크와 연결선 그리기
mpPose = mp.solutions.pose           # 포즈 잡아내기 클래스
pose = mpPose.Pose()                 # 포즈를 잡아내기 위한 함수

cap = cv2.VideoCapture(0)           ###### 영상 획득 기본 코드 ######

pTime =0

while True:
    success, img = cap.read()       ###### 영상 획득 기본 코드 ######
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR을 RGB로 변환
    results = pose.process(imgRGB)  # RGB이미지로 포즈를 잡아냄
    # print(results.pose_landmarks)
    if results.pose_landmarks:  # 포즈 랜드마크가 잡히면 랜드마크와 연결선 표시
        mpDraw.draw_landmarks(img, results.pose_landmarks,
                                mpPose.POSE_CONNECTIONS)
    
    # 아래쪽 4줄은 FPS연산 및 표시를 위한 코드
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN,
                                                     3, (255,0,0), 3)

    cv2.imshow("Image", img)        ###### 영상 획득 기본 코드 ######
    if cv2.waitKey(1) & 0xFF ==ord('q'): # 키보드의 q 키가 입력되면 정지
        break