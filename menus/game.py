import sys

import pygame

from menus import MainMenu


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

        self.font = pygame.font.SysFont(("Roboto", "Consolas"), 20)
        self.menu = None

    @staticmethod
    def _quit():
        pygame.quit()
        sys.exit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainMenu(self).run()

    def handle_update(self):
        pass

    def handle_render(self, surf):
        text = self.font.render("Game", antialias=True, color=pygame.Color("black"))
        surf.blit(text, (50, 50))

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
