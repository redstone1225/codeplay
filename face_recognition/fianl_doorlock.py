import cv2
import tkinter as tk
from tkinter import messagebox
import serial
import time

# 얼굴 인식 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Tkinter 창 설정
root = tk.Tk()
root.title("Smart Door Lock")

# 아두이노 연결 설정 (포트와 보드레이트는 실제 환경에 맞게 설정)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # 아두이노 초기화 시간 대기

# 비밀번호 설정
correct_password = "1234"
entered_password = ""

# 카메라 피드 업데이트 함수
def update_frame():
    ret, frame = cap.read()
    if not ret:
        lbl_text.config(text="카메라를 찾을 수 없습니다.")
        root.after(1000, update_frame)
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 얼굴이 인식되면 텍스트 출력
    if len(faces) > 0:
        lbl_text.config(text="비밀번호를 입력하시오")
        read_arduino()
    else:
        lbl_text.config(text="")
        reset_door()

    root.after(10, update_frame)

# 아두이노에서 버튼 값 읽기
def read_arduino():
    global entered_password
    if arduino.in_waiting > 0:
        button_value = arduino.readline().decode().strip()
        print(f"Arduino button value: {button_value}")  # 디버깅 출력
        if button_value in [str(i) for i in range(10)] + ['*', '#']:
            on_button_click(button_value)
            lbl_text.config(text=f"버튼 값: {button_value}")  # Tkinter 라벨에 버튼 값 출력

# 버튼 클릭 이벤트
def on_button_click(number):
    global entered_password
    entered_password += str(number)
    lbl_password.config(text=entered_password)
    arduino.write(b'B')  # 피에조 부저 비프음

    if len(entered_password) == 4:
        if entered_password == correct_password:
            lbl_text.config(text="문이 열렸습니다")
            arduino.write(b'S')  # 성공 신호
            arduino.write(b'O')  # 서보모터 열기
        else:
            lbl_text.config(text="비밀번호가 틀렸습니다")
            arduino.write(b'F')  # 실패 신호
        entered_password = ""

# 얼굴이 사라지면 문을 닫고 초기화
def reset_door():
    global entered_password
    time.sleep(3)
    arduino.write(b'C')  # 서보모터 닫기
    lbl_password.config(text="")
    lbl_text.config(text="")
    entered_password = ""

# 카메라 설정
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# Tkinter 위젯 설정
lbl_text = tk.Label(root, text="", font=("Helvetica", 16))
lbl_text.pack()

lbl_password = tk.Label(root, text="", font=("Helvetica", 16))
lbl_password.pack()

# 카메라 피드 업데이트 시작
update_frame()

# Tkinter 이벤트 루프 시작
root.mainloop()

# 카메라 해제
cap.release()
cv2.destroyAllWindows()

# #include <Servo.h>

# // 아날로그 핀 정의
# const int ANALOG_PINS[] = {A0, A1, A2, A3};
# const int NUM_PINS = 4;

# // 버튼 값 임계치 정의
# const int NO_PRESS = 800;      
# const int BTN_10K = 700;        
# const int BTN_1K = 50;        
# const int BTN_DIRECT = 30;    

# // 각 버튼별 출력 문자 정의
# const char PIN_VALUES[4][3] = {
#     {'1', '2', '3'},  
#     {'4', '5', '6'},  
#     {'7', '8', '9'},  
#     {'*', '0', '#'}    
# };

# void setup() {
#     Serial.begin(9600);
#     Serial.println("시스템 시작");
   
#     // 아날로그 핀 풀업저항 활성화
#     for(int i = 0; i < NUM_PINS; i++) {
#         pinMode(ANALOG_PINS[i], INPUT_PULLUP);
#     }
# }

# void loop() {
#     // 각 아날로그 핀 순회
#     for(int pin = 0; pin < NUM_PINS; pin++) {
#         int value = analogRead(ANALOG_PINS[pin]);
       
#         // 버튼 입력 판단 및 처리
#         if(value < NO_PRESS) {  // 버튼 입력이 있는 경우
#             Serial.print("Pin A");
#             Serial.print(pin);
#             Serial.print(" Value: ");
#             Serial.print(value);
#             Serial.print(" -> Button: ");
           
#             if(value < BTN_DIRECT) {
#                 Serial.println(PIN_VALUES[pin][0]);  
#             }
#             else if(value < BTN_1K) {
#                 Serial.println(PIN_VALUES[pin][1]);  
#             }
#             else if(value < BTN_10K) {
#                 Serial.println(PIN_VALUES[pin][2]);  
#             }
           
#             // 디바운싱
#             delay(200);
#         }
#         else{
#           Serial.println("None");
#         }
#     }
# }