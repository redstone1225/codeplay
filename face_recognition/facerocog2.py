import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class FaceRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Add CAP_DSHOW
        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera")
        self.db_folder = 'faces'
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

    def __del__(self):
        if hasattr(self, 'cap'):
            self.cap.release()

    def run(self):
        print("\n얼굴 인식 시스템 시작")
        print("r: 얼굴 등록")
        print("q: 종료\n")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("카메라로부터 프레임을 읽을 수 없습니다.")
                    break
                
                result = self.detect_face(frame)
                frame = self.draw_text(frame, result, (10, 30))
                cv2.imshow('Face Recognition', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('r'):
                    self.register_face()
        
        finally:
            cv2.destroyAllWindows()
            self.cap.release()

if __name__ == "__main__":
    try:
        fr = FaceRecognition()
        fr.run()
    except Exception as e:
        print(f"Error: {e}")