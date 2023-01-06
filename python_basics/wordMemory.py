def word_in():
    kor = open("wordkor.text", "a", encoding = "UTF - 8")
    eng = open("wording.text", "a", encoding = "UTF - 8")
    while True:
        kor_in = input("한글뜻을 입력하세요 (입력종료 : 꺼져 ) : ")
        if kor_in == "꺼져":
            break
        else:
            kor.write(kor_in)
        eng_in = input("영어단어를 입력하세요 (입력종료 : 꺼져) : ")
        if eng_in == "꺼져":
            break
        else:
            eng.write(eng_in + "\n")
    kor.close()
    eng.close()

def eng_exam():
    kor = open("wordkor.text", "a", encoding = "UTF - 8")
    eng = open("wording.text", "a", encoding = "UTF - 8")
    kor_Q = kor.readlines()
    eng_A = eng.readlines()
    score = 0

    for i in range(len(kor_Q)):
        answer = input(f"{kor_Q[i].strip()} -> 영어로? ( 종료 = 꺼져) : ")
        if answer == "꺼져":
            break
        elif answer == eng_A[i].strip():
            print("정답입니다.")
            score += 1
        else:
            print(f"틀렸습니다, 정답 : {eng_A[i].strip()}")
    print("수고하셨습니다.")
    print(f"{len(kor_Q)+1} 문제중 {score}문제를 맞추셨습니다.")
    
    kor.close()
    eng.close()

while True:
    select = int(input("1.단어입력 / 2. 단어시험 / 3. 종료 "))
    if select == 1:
        word_in()
    elif select == 2:
        eng_exam()
    elif select == 3:
        break
    else:
        print("잘못입력하셧습니다.")

    


