import math
import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def draw_polygon(surf, pos, sides, radius, color):
    x, y = pos
    pygame.draw.polygon(
        surf,
        color,
        [
            (
                x + radius * math.sin(math.pi * 2 * i / sides),
                y + radius * -(math.cos(math.pi * 2 * i / sides)),
            )
            for i in range(sides)
        ],
        4,
    )


def pyquit():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pyquit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                pyquit()

    screen.fill("white")
    draw_polygon(
        screen, (screen.get_width() // 2, screen.get_height() // 2), 3, 200, "blue"
    )
    draw_polygon(
        screen, (screen.get_width() // 2, screen.get_height() // 2), 4, 200, "green"
    )
    draw_polygon(
        screen, (screen.get_width() // 2, screen.get_height() // 2), 5, 200, "red"
    )

    pygame.display.update()
    clock.tick(60)
