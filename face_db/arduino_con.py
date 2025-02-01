import tkinter as tk
import serial
import time

# 아두이노와의 시리얼 통신 설정
arduino = serial.Serial('COM10', 9600)  # COM 포트와 보드레이트를 아두이노 설정에 맞게 변경하세요.
time.sleep(2)  # 시리얼 통신 안정화를 위해 잠시 대기

# LED 밝기 변경 함수
def set_r_brightness(val):
    arduino.write(f'R{int(val)}\n'.encode())

def set_g_brightness(val):
    arduino.write(f'G{int(val)}\n'.encode())

def set_b_brightness(val):
    arduino.write(f'B{int(val)}\n'.encode())

def turn_off_all():
    arduino.write(b'A\n')  # 모든 LED 끄기
    r_slider.set(0)
    g_slider.set(0)
    b_slider.set(0)

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("Arduino RGB LED Control")
root.geometry("400x300")  # 창 크기 설정 (너비 x 높이)

# 슬라이더 생성
r_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=set_r_brightness)
r_slider.pack(pady=10)

g_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=set_g_brightness)
g_slider.pack(pady=10)

b_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=set_b_brightness)
b_slider.pack(pady=10)

all_button = tk.Button(root, text="All Off", command=turn_off_all)
all_button.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()

# 프로그램 종료 시 시리얼 포트 닫기
arduino.close()