import random
import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

fps = 60


# [location, velocity, timer]
particles = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill("black")

    particles.append(
        [
            list(pygame.mouse.get_pos()),
            [random.randint(0, 20) / 10 - 1, -2],
            random.randint(4, 10),
        ]
    )

    for particle in particles.copy():
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1

        particle[1][1] += 0.1

        pygame.draw.circle(screen, "white", particle[0], particle[2])
        if particle[2] <= 0:
            particles.remove(particle)

    pygame.display.update()
    clock.tick(fps)
