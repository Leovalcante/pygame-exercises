import sys

import pygame.display

from player import Player


class Game:
    def __init__(self, width=1000, height=800, display_caption="game"):
        pygame.init()
        display_size = (width, height)
        pygame.display.set_caption(display_caption)
        self.screen = pygame.display.set_mode(display_size)
        self.display = pygame.Surface(display_size)
        self.clock = pygame.time.Clock()

        player_size = 20
        self.player = Player(
            self.display.get_width() // 2 - player_size // 2,
            self.display.get_height() // 2 - player_size // 2,
            player_size,
            pygame.Color("blue"),
        )
        self.movement = pygame.Vector2()

        self.render_scroll = pygame.Vector2()

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

                if event.key == pygame.K_w:
                    self.movement.y -= 1
                if event.key == pygame.K_s:
                    self.movement.y += 1
                if event.key == pygame.K_d:
                    self.movement.x += 1
                if event.key == pygame.K_a:
                    self.movement.x -= 1

                if event.key == pygame.K_UP:
                    self.player.shoot_direction.y -= 1
                if event.key == pygame.K_DOWN:
                    self.player.shoot_direction.y += 1
                if event.key == pygame.K_LEFT:
                    self.player.shoot_direction.x -= 1
                if event.key == pygame.K_RIGHT:
                    self.player.shoot_direction.x += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.movement.y += 1
                if event.key == pygame.K_s:
                    self.movement.y -= 1
                if event.key == pygame.K_d:
                    self.movement.x -= 1
                if event.key == pygame.K_a:
                    self.movement.x += 1

                if event.key == pygame.K_UP:
                    self.player.shoot_direction.y += 1
                if event.key == pygame.K_DOWN:
                    self.player.shoot_direction.y -= 1
                if event.key == pygame.K_LEFT:
                    self.player.shoot_direction.x += 1
                if event.key == pygame.K_RIGHT:
                    self.player.shoot_direction.x -= 1

    def handle_update(self):
        self.player.update(self.movement)

    def handle_render(self, surf):
        self.render_scroll += (
            self.player.get_rect().center
            - pygame.Vector2(self.display.get_size()) / 2
            - self.render_scroll
        ) / 30

        self.player.render(surf, self.render_scroll)

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
