import cv2
import numpy as np
from deepface import DeepFace
import os
from PIL import Image, ImageDraw, ImageFont
import logging

class FaceRecognition:
    def __init__(self):
        # Suppress unnecessary warnings and info messages
        logging.getLogger('tensorflow').setLevel(logging.ERROR)
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        
        # Create database folder
        self.db_folder = "face_db"
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)
    
    def draw_text(self, frame, text, position):
        # Convert to PIL for Korean text
        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        
        # Use Korean font
        try:
            font = ImageFont.truetype("malgun.ttf", 30)
        except:
            font = ImageFont.load_default()
            
        draw.text(position, text, font=font, fill=(255, 255, 255))
        return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    
    def register_face(self):
        print("\n=== 얼굴 등록 모드 ===")
        print("공간 바를 눌러 사진 촬영")
        print("'q'를 눌러 취소")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # 프리뷰 표시
            cv2.imshow('Registration Mode', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("등록 취소됨")
                cv2.destroyWindow('Registration Mode')
                return
            elif key == ord(' '):  # 스페이스바
                name = input("\n등록할 이름을 입력하세요: ")
                if name:
                    try:
                        # 파일 저장
                        file_path = os.path.join(self.db_folder, f"{name}.jpg")
                        cv2.imwrite(file_path, frame)
                        print(f"\n{name}님의 얼굴이 성공적으로 등록되었습니다.")
                        print(f"저장 위치: {file_path}")
                    except Exception as e:
                        print(f"저장 실패: {str(e)}")
                break
        
        cv2.destroyWindow('Registration Mode')    
    def recognize_face(self, frame):
        try:
            if len(os.listdir(self.db_folder)) == 0:
                return "등록된 얼굴이 없습니다"
            
            # Suppress DeepFace verbose output
            result = DeepFace.find(
                img_path=frame,
                db_path=self.db_folder,
                enforce_detection=False,
                silent=True  # Add this parameter
            )
            
            if len(result[0]) > 0:
                identity = result[0]['identity'][0]
                name = os.path.splitext(os.path.basename(identity))[0]
                return f"인식된 사람: {name}"
            
            return "미등록 얼굴"
            
        except Exception as e:
            return "얼굴이 감지되지 않음"
    
    def run(self):
        print("\n얼굴 인식 시스템 시작")
        print("'r': 얼굴 등록")
        print("'q': 프로그램 종료\n")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # 얼굴 인식 실행
            result = self.recognize_face(frame)
            
            # 결과 표시
            frame = self.draw_text(frame, result, (10, 30))
            cv2.imshow('Face Recognition', frame)
            
            # 키 입력 처리
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.register_face()
        
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition = FaceRecognition()
    face_recognition.run()