import pygame


class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        self.pos = pygame.Vector2(self.x, self.y)

    def get_rect(self):
        return pygame.Rect(self.pos, [self.size] * 2)

    def update(self, movement: pygame.Vector2):
        self.pos += movement

    def render(self, surf: pygame.Surface):
        pygame.draw.rect(surf, self.color, self.get_rect())
