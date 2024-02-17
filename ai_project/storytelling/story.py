import pygame
import sys

# 파이게임 초기화``
pygame.init()

# 창 크기 설정
screen_width = 1024
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))

# 창 제목 설정
pygame.display.set_caption("이미지 넘기기")

# 이미지 경로들
image_paths = [
    "ai_project/storytelling/image/001.png",
    "ai_project/storytelling/image/002.png",
    "ai_project/storytelling/image/003.png",
    "ai_project/storytelling/image/004.png",
    "ai_project/storytelling/image/005.png",
    "ai_project/storytelling/image/006.png",
    "ai_project/storytelling/image/007.png",
    "ai_project/storytelling/image/008.png",
    # 추가적인 이미지 파일들의 경로를 이곳에 넣어주세요
]

# 이미지를 불러오고 크기 조정
images = [pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height)) for path in image_paths]

current_image = 0  # 현재 표시 중인 이미지의 인덱스

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 마우스 클릭 이벤트 감지
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 왼쪽 버튼 클릭 시 이미지 전환
            if event.button == 1:
                current_image = (current_image + 1) % len(images)  # 다음 이미지로 전환

                # 마지막 이미지 이후 클릭 시 창 닫기
                if current_image == len(images) - 1:
                    running = False

    # 현재 이미지 화면에 그리기
    screen.blit(images[current_image], (0, 0))

    # 화면 업데이트
    pygame.display.update()

    # 마지막 이미지를 표시한 후 한 번 더 클릭하면 창 닫히도록 처리
    if current_image == len(images) - 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.quit()
                    sys.exit()




