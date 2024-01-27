import pygame
import sys
import time

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
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("O/X 퀴즈 게임")

def draw_text(text, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_intro():
    screen.fill(WHITE)
    draw_text("지구가 환경오염과 지구 온난화 때문에 기온이 상승하고 있다.", BLACK, (50, 50))
    draw_text("기온이 상승되면 무슨 일이 발생하는지 알아보기 위해 간단한 O/X 퀴즈를 해보자!", BLACK, (50, 100))
    draw_text("O,X 게임을 시작하려면 ENTER를 누르시오.", BLACK, (50, 150))
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
        ("지구의 온난화로 인해 해수면이 상승한다. (O/X)", "O"),
        ("해안가에 상어가 더 많이 출몰할 것이다. (O/X)", "O"),
        (" (O/X)", "X"),
        (" (O/X)", "X"),
        (" (O/X)", "X"),
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
