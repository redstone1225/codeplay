# -*- coding: utf-8 -*-
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("sdlkjsfdljk")

character = pygame.image.load("pygame_01/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_xPos = 0
character_yPos = 0

circleX_pos = 0
circleY_pos = 0

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # print("mouseMotion")
            # print(pygame.mouse.get_pos())
            character_xPos, character_yPos = pygame.mouse.get_pos()
            # screen.fill((0, 0, 0))
            # pygame.draw.circle(screen, (255, 0, 255), (circleX_pos, circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouseButtonDown")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("좌클")
            elif event.button == 3:
                print("우클")
            elif event.button == 2:
                print("휠클")
            elif event.button == 4:
                print("휠업")
            elif event.button == 5:
                print("휠다운")
            
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseButtonUp")
            pass

    screen.fill((0, 0, 0))
    screen.blit(character, (character_xPos - character_width / 2, character_yPos - character_height / 2))

    pygame.display.update()

pygame.quit()