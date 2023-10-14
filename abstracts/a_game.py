import abc
import sys

import pygame


class AbstractGame(abc.ABC):
    def __init__(self, width=600, height=450, display_caption="game"):
        pygame.init()
        self.width = width
        self.height = height
        self.display_size = (self.width, self.height)
        pygame.display.set_caption(display_caption)
        self.screen = pygame.display.set_mode(self.display_size)
        self.display = pygame.Surface(self.display_size)
        self.clock = pygame.time.Clock()

    @staticmethod
    def _quit():
        pygame.quit()
        sys.exit()

    @abc.abstractmethod
    def handle_input(self):
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         self._quit()
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE:
        #             self._quit()
        pass

    @abc.abstractmethod
    def handle_update(self):
        pass

    @abc.abstractmethod
    def handle_render(self, surf):
        pass

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

    class Game(AbstractGame):
        def __init__(self, width=600, height=450, display_caption="game"):
            super().__init__(width, height, display_caption)

        def handle_input(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()

        def handle_update(self):
            pass

        def handle_render(self, surf):
            pass

    Game().run()
