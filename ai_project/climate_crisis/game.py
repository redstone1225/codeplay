import pygame
import sys

# Pygame 초기화
pygame.init()

# 게임 화면 설정
win_width, win_height = 640, 480
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Survival Game")

# 색깔 정의
white = (255, 255, 255)
blue = (0, 0, 255)

# 플레이어 캐릭터
player_width, player_height = 50, 50
player_x, player_y = win_width // 2, win_height - player_height - 10
player_vel = 5
jump_count = 10
is_jump = False

# 해수면 초기 값 설정
sea_width, sea_height = win_width, 20
sea_level = sea_height  # 해수면 높이 초기화
sea_speed = 0.2  # 해수면 높이 변화 속도

# 시간 추적 변수
start_time = pygame.time.get_ticks()

# 게임 루프
running = True
while running:
    # 화면 클리어
    win.fill(white)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 시작 후 6초가 경과하면 해수면이 나타남
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000  # milliseconds를 seconds로 변환
    if elapsed_time >= 6:
        if sea_level < win_height:
            sea_level += sea_speed  # 해수면 높이 증가
        else:
            sea_level = win_height  # 최대 높이 설정

    # 해수면 그리기
    pygame.draw.rect(win, blue, (0, win_height - sea_level, sea_width, sea_level))

    # 플레이어 그리기
    pygame.draw.rect(win, (0, 0, 0), (player_x, player_y, player_width, player_height))

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
sys.exit()


