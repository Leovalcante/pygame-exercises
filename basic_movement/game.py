import sys

import pygame.display

from player import Player


class Game:
    def __init__(self, width=600, height=450, display_caption="game"):
        pygame.init()
        self.width = width
        self.height = height
        self.display_size = (self.width, self.height)
        pygame.display.set_caption(display_caption)
        self.screen = pygame.display.set_mode(self.display_size)
        self.display = pygame.Surface(self.display_size)
        self.clock = pygame.time.Clock()

        player_size = 20
        self.player = Player(
            self.display.get_width() // 2 - player_size // 2,
            self.display.get_height() // 2 - player_size // 2,
            player_size,
            pygame.Color("blue"),
        )
        self.movement = pygame.Vector2()

    @staticmethod
    def __quit():
        pygame.quit()
        sys.exit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__quit()

                if event.key == pygame.K_UP:
                    self.movement.y -= 1
                if event.key == pygame.K_DOWN:
                    self.movement.y += 1
                if event.key == pygame.K_RIGHT:
                    self.movement.x += 1
                if event.key == pygame.K_LEFT:
                    self.movement.x -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.movement.y += 1
                if event.key == pygame.K_DOWN:
                    self.movement.y -= 1
                if event.key == pygame.K_RIGHT:
                    self.movement.x -= 1
                if event.key == pygame.K_LEFT:
                    self.movement.x += 1

    def handle_update(self):
        self.player.update(self.movement)

    def handle_render(self, surf):
        self.player.render(surf)

    def run(self):
        while True:
            self.display.fill(pygame.Color("white"))

            self.handle_input()

            self.handle_update()

            self.handle_render(self.display)

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game().run()
