import random
import os
clear = lambda: os.system('cls')

eng = ["car", "hat", "green", "happy", "use", "ear", "boy", "girl", "dog", "cat"]
kor = ["자동차", "모자", "초록", "행복한", "사용하다", "귀", "소년", "소녀", "강아지", "고양이"]
select = 0
answer = 0


while True:
    clear()
    print("ons 깜지봇 III")
    print("*" * 24)
    print(f"수록 영딘이 갯수 : {len(eng)}")
    print("*" * 24)
    mode = input("원하는 작업 선택 : 단어시험 / 단어입력 / 종료 => ")
    print("*" * 24)
    
    if mode == "단어시험":
        while len(kor) != 0:
            clear()
            select = random.randint(0, len(eng) - 1)
            answer = input(f"{kor[select]} - 이 단어를 영어로 하면 ? :")
            
            if answer == eng[select]:
                print(f"정답입니다!{kor[select]} = {eng[select]} 이죠! 명석이보다 명석하시네요")
                eng.pop(select)
                kor.pop(select)
            else:
                print("틀리셨어요. 님 명석이임?")
        print("10개의 준비된 단어를 모두 멈추셨습니다.")

    elif mode == "종료":
        print("종료합니다")
        break
    elif mode == "단어입력":
        while True:
            eng.append(input("영어단어를 입력하세요 :"))
            kor.append(input("한글단어를 입력하세요 :"))
            if "아니오" == input("입력을 더 하시겠습니까? (예 / 아니오)"):
                print("단어를입력을 마쳤습니다.")
                break
              


