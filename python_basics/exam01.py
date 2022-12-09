import random

who = ["명섹","지현", "홍석", "서윤"]
where = ["화장실", "교실", "운동장", "편의점"]
what = ["양말", "지우개", "샤프심", "교통카드"]

random.choice(who)
random.choice(where)
random.choice(what)

print(f"{random.choice(who)}(이)가 {random.choice(where)}에서 {random.choice(what)}(으)로 살해했습니다.")

