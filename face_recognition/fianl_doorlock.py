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
arduino = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # 아두이노 초기화 시간 대기

# 비밀번호 설정
correct_password = "1234"
entered_password = ""

# 카메라 피드 업데이트 함수
def update_frame():
    ret, frame = cap.read()
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
        if button_value in [str(i) for i in range(1, 13)]:
            on_button_click(button_value)

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