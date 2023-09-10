import cv2
import mediapipe as mp # 손과 손가락 마디를 인식하기 위한 라이브러리

cap = cv2.VideoCapture(0) # 카메라를 통해 영상을 불러옵니다
mpHands = mp.solutions.hands # Mediapipe를 통한 손 검출
hands = mpHands.Hands() # Hands()함수 안의 내용을 가져옵니다
mpDraw = mp.solutions.drawing_utils # 영상위에 그림을 그리기 위한 모듈입니다

while True:
    success, img = cap.read() # 영상을 img에 저장합니다
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 영상을 RGB로 변환합니다
    results = hands.process(imgRGB) # RGB영상으로 hand모듈을 실행합니다

    if results.multi_hand_landmarks: # 손이 인식되면 실행합니다
        for handLMS in results.multi_hand_landmarks: # 마디와 선을 연결합니다
            mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)
            #각 손가락 마디를 표시하고 선을 연결합니다

        cv2.imshow("IMAGE", img) # 영상을 보여줍니다
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # "q" 키가 눌리면 종료합니다