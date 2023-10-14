import sys

import pygame


class Game:
    def __init__(self, width=600, height=450, display_caption="game"):
        pygame.init()
        pygame.display.set_caption(display_caption)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(("Roboto", "Consolas", "Serif"), 20)

    def run(self):
        while True:
            self.screen.fill(pygame.Color("black"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    Game().run()
