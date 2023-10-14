import sys

import pygame


class Game:
    def __init__(self, width=600, height=450, display_caption="game"):
        pygame.init()

        display_info = pygame.display.Info()
        self.fullscreen = False
        self.monitor_size = (display_info.current_w, display_info.current_h)

        pygame.display.set_caption(display_caption)

        init_window_size = (width, height)
        self.screen = pygame.display.set_mode(init_window_size, pygame.RESIZABLE)
        self.display = pygame.Surface(init_window_size)

        self.clock = pygame.time.Clock()

    @staticmethod
    def _quit():
        pygame.quit()
        sys.exit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            if event.type == pygame.VIDEORESIZE:
                if not self.fullscreen:
                    new_window_size = (event.w, event.h)
                    self.screen = pygame.display.set_mode(
                        new_window_size, pygame.RESIZABLE
                    )
                    self.display = pygame.Surface(new_window_size)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._quit()
                if event.key == pygame.K_f:
                    self.fullscreen ^= True
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(
                            self.monitor_size,
                            pygame.FULLSCREEN,
                        )
                        self.display = pygame.Surface(self.monitor_size)
                    else:
                        new_window_size = (
                            self.screen.get_width(),
                            self.screen.get_height(),
                        )
                        self.screen = pygame.display.set_mode(
                            new_window_size, pygame.RESIZABLE
                        )
                        self.display = pygame.Surface(new_window_size)

    def handle_update(self):
        pass

    def handle_render(self, surf):
        pygame.draw.rect(
            surf,
            pygame.Color("blue"),
            pygame.Rect(
                surf.get_width() - 5 - surf.get_width() / 5,
                50,
                surf.get_width() / 5,
                50,
            ),
        )

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
