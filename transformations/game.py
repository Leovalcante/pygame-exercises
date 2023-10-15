import sys

import pygame

pygame.init()
pygame.display.set_caption("game")
screen = pygame.display.set_mode((1000, 500), 0, 32)
clock = pygame.time.Clock()

arrow_img = pygame.image.load("arrow.png")
arrow_spin = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill("white")
    arrow_spin += 1
    for i in range(4):
        arrow = arrow_img.copy()

        if i == 0:
            arrow = pygame.transform.flip(arrow, True, False)
        elif i == 1:
            arrow = pygame.transform.scale(arrow, (80, 10))
        elif i == 2:
            arrow = pygame.transform.rotate(arrow, arrow_spin)

        screen.blit(arrow, (50 + i * 250, 200))

    arrow = arrow_img.copy()

    mx, my = pygame.mouse.get_pos()
    arr = pygame.transform.rotate(arrow, arrow_spin)
    screen.blit(
        arr,
        (mx - arr.get_width() // 2, my - arr.get_height() // 2),
    )

    pygame.display.update()
    clock.tick(60)
