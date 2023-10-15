import random
import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
clock = pygame.time.Clock()

display = pygame.Surface((800 // 2, 600 // 2))

shake_time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                print("shake")
                shake_time = 30

    screen.fill("white")

    render_offset = [0, 0]
    if shake_time > 0:
        shake_time -= 1
        render_offset = [random.randint(0, 8) - 4, random.randint(0, 8) - 4]

    screen.blit(pygame.transform.scale(display, screen.get_size()), render_offset)
    pygame.display.update()
    clock.tick(60)
