import pygame
import sys
import time
import os
# 파이게임 초기화
pygame.init()

# 한글 폰트 설정
font_path = "ai_project/climate_crisis/src/NanumGothicEco.ttf"  # 여기에 사용하고자 하는 폰트 파일의 경로를 입력하세요
font_size = 24
font = pygame.font.Font(font_path, font_size)

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 화면 크기 설정
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("O/X 퀴즈 게임")

def draw_text(text, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_intro():
    screen.fill(WHITE)

    # 첫 번째 텍스트 및 이미지 표시
    draw_text("지구가 환경오염과 지구 온난화 때문에 기온이 상승하고 있다. 산업 혁명이 발달한 1850년대 이후", BLACK, (50, 30))
    draw_text("화석 연료 사용량이 급격히 증가한 것과 더불어 벌목 및 무분별한 토지 개발 등 인간 활동으로 CO2 등 많은", BLACK, (50, 70))
    draw_text("양의 온실가스가 대기로 배출되고 이것이 누적된 결과 지구 전체의 평균 기온은 계속 상승하고 있다.", BLACK, (50, 110))
    draw_text("다음으로 넘기려면 ENTER를 누르시오.", BLACK, (50, 150))

    image_path1 = 'ai_project/climate_crisis/src/bg.png'  # 첫 번째 이미지 파일의 경로를 입력하세요
    if os.path.exists(image_path1):
        original_image1 = pygame.image.load(image_path1)
        resized_image1 = pygame.transform.scale(original_image1, (700, 500))  # 원하는 크기로 조절
        screen.blit(resized_image1, (250, 210))  # 이미지 위치 조절

    pygame.display.flip()

    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_enter = False

    # 화면 지우기
    screen.fill(WHITE)
    pygame.display.flip()

    # 두 번째 텍스트 및 이미지 표시
    draw_text("지구의 기온은 올라갈 수 밖에 없다. 우리는 지구 기온이 올라가면 그에 대한 방안을 만들어내고 잘 극복해 나가면 된다.", BLACK, (40, 30))
    draw_text("잘 극복해 나가면 된다. 그러기 위해서는 지구온난화가 발생하면 우리 생활이 어떻게 변화하고 환경이 어떻게 변하는지 알아야 한다.", BLACK, (40, 70))
    draw_text("환경이 어떻게 변하는지 알아야 한다.", BLACK, (40, 110))
    draw_text("그래서 O,X 퀴즈로 재미있게 알아보자!!", BLACK, (40, 150))
    draw_text("다음으로 넘기려면 ENTER를 누르시오.", BLACK, (40, 190))

    image_path2 = 'ai_project/climate_crisis/src/bg2.png'  # 두 번째 이미지 파일의 경로를 입력하세요
    if os.path.exists(image_path2):
        original_image2 = pygame.image.load(image_path2)
        resized_image2 = pygame.transform.scale(original_image2, (700, 500))  # 원하는 크기로 조절
        screen.blit(resized_image2, (250, 210))  # 이미지 위치 조절

    pygame.display.flip()

    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_enter = False

def ask_question(question, correct_answer):
    user_answer = None

    while user_answer not in ['O', 'X']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    user_answer = 'O'
                elif event.key == pygame.K_x:
                    user_answer = 'X'
        
        screen.fill(WHITE)
        draw_text(question, BLACK, (50, 50))
        draw_text("정답을 입력하세요 (O/X):", BLACK, (50, 150))
        pygame.display.flip()

    return user_answer == correct_answer

def play_game():
    score = 0

    questions = [
        ("극지방의 빙하가 녹아 해수면 상승이 가속화될 것이다 (O/X)", "O"),
        ("해안가에 상어가 더 많이 출몰할 것이다. (O/X)", "O"),
        ("인간이 체온 조절 능력을 잃을 것이다. (O/X)", "O"),
        ("온난화로 인해 이산화탄소 농도가 감소하고 해수면 산성화가 발생할 수 있습니다. (O/X)", "X"), 
        # 감소 하는게 아니다
        ("온도 상승으로 인해 작물의 생육에 부정적인 영향을 미칠 수 있다.(O/X)", "O"),
        ("폭염, 폭우 같은 극단적인 이상 기후로 홍수나 산사태 등 자연재해가 빈번하게 발생할 것이다. (O/X)", "O"),
        ("새로운 생물이 나와 생물 종이 더 다양해 질 것이다. (O/X)", "X"),
        # 새로운 종이 나오지만 멸종하는 종이 더 많기 때문에 다양해지지 않는다
    ]

    for question, correct_answer in questions:
        user_answer = None
        while user_answer not in ['O', 'X']:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        user_answer = 'O'
                    elif event.key == pygame.K_x:
                        user_answer = 'X'

            screen.fill(WHITE)
            draw_text(question, BLACK, (50, 50))
            draw_text("정답을 입력하세요 (O/X):", BLACK, (50, 150))
            pygame.display.flip()

        if user_answer == correct_answer:
            draw_text("정답입니다!", BLACK, (50, 250))
            pygame.display.flip()
            score += 1
        else:
            draw_text("틀렸습니다!", BLACK, (50, 250))
            pygame.display.flip()

        time.sleep(1)

    draw_text(f"게임 종료! 총 {score}/{len(questions)} 문제를 맞추셨습니다.", BLACK, (50, 300))
    pygame.display.flip()
    time.sleep(2)

if __name__ == "__main__":
    display_intro()
    play_game()
