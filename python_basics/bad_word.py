bad_words = ["병신", "니얼굴 코딩쌤", "시발", "씨발", "시발년", "시발놈", "씨발년", "씨발놈", "느짬", "느금먀", "엄마 없니?", "노에미", "민재", "코딩쌤", "장애", "장애년", "지랄", "개새끼"]
bad_word = []
answer = 0
add_word = 0


while True:
    answer = input("말씀하세요 주인님 : ") 
    bad_word = []
    for word in bad_words:
        if word in answer:
            bad_word.append(word)
            
    if len(bad_word) > 0:
        print(f"{bad_word} < - 이런 말은 쓰면 안돼요. 나빠요. 병신아")
        continue
    else:
        if answer == "꺼져":
            print("안녕히 가세요 주인님!")
            break
        elif answer == "추가":
            add_word = input("어떤 단어를 추가할까요? : ")
            bad_words.append(add_word)
            print(f"{add_word} 단어가 금칙어에 추가되었습니다")
            print(f"지금까지 등록된 금지단어를 ")
            print("=" * 50)
            print(bad_word)
            print("=" * 50)
            continue

        else:
            print(f"{answer} (이)라구요? 옳은 말씀이십니다 주인님")
        
