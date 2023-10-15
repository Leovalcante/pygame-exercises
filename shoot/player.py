from typing import List

import pygame


class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        self.pos = pygame.Vector2(self.x, self.y)

        self.shoot_direction = pygame.Vector2()
        self.shoots: List[Shoot] = []

    def get_rect(self):
        return pygame.Rect(self.pos, [self.size] * 2)

    def update(self, movement: pygame.Vector2):
        self.pos += movement
        if self.shoot_direction != pygame.Vector2():
            self.shoots.append(
                Shoot(
                    self.get_rect().center + self.shoot_direction * self.size,
                    self.shoot_direction.copy(),
                    self.size,
                    10,
                )
            )

        for shoot in self.shoots:
            alive = shoot.update()
            if not alive:
                self.shoots.remove(shoot)

    def render(self, surf: pygame.Surface):
        pygame.draw.rect(surf, self.color, self.get_rect())
        for shoot in self.shoots.copy():
            shoot.render(surf)


class Shoot:
    def __init__(self, pos, velocity, size, time) -> None:
        self.pos = pos
        self.velocity = velocity
        self.size = size
        self.time = time

    def update(self):
        self.pos += self.velocity * self.size
        self.time = max(self.time - 0.1, 0)
        return self.time

    def render(self, surf):
        pygame.draw.circle(
            surf,
            "red",
            self.pos,
            8,
        )
