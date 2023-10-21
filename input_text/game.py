import sys

import pygame
import pygame_gui


class TextInput:
    def __init__(self, pos, size: list) -> None:
        self.pos = pos
        self.size = size
        self.color_focus = pygame.Color("lightskyblue3")
        self.color_no_focus = pygame.Color("gray15")
        self.focus = False

    def get_rect(self):
        return pygame.Rect(self.pos, self.size)

    def draw(self, surf):
        color = self.color_focus if self.focus else self.color_no_focus
        pygame.draw.rect(
            surface=surf,
            color=color,
            rect=self.get_rect(),
            width=2,
        )


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

        self.font = pygame.font.Font(None, 32)
        self.user_input = ""
        self.overflow_user_input = ""

        self.input = TextInput((10, 10), [200, 50])
        self.overflow_input = TextInput((100, 100), [200, 50])

        self.manager = pygame_gui.UIManager(self.display_size)

        self.gui_text_input = pygame_gui.elements.UITextEntryLine(
            pygame.Rect((350, 275), (200, 50)),
            self.manager,
            object_id="#main_text_entry",
        )

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
                    self._quit()

                if self.input.focus:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        self.user_input += event.unicode
                if self.overflow_input.focus:
                    if event.key == pygame.K_BACKSPACE:
                        self.overflow_user_input = self.overflow_user_input[:-1]
                    else:
                        self.overflow_user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if self.input.get_rect().collidepoint(event.pos):
                        self.input.focus = True
                    else:
                        self.input.focus = False

                    if self.overflow_input.get_rect().collidepoint(event.pos):
                        self.overflow_input.focus = True
                    else:
                        self.overflow_input.focus = False

            if (
                event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                and event.ui_object_id == "#main_text_entry"
            ):
                self.show_text(event.text)

            self.manager.process_events(event)

    def show_text(self, text):
        while True:
            self.display.fill("white")

            self.handle_input()

            text_surf = self.font.render(text, True, "black")
            self.display.blit(
                text_surf,
                (
                    self.width // 2 - text_surf.get_width() // 2,
                    self.height // 2 - text_surf.get_height() // 2,
                ),
            )

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()

    def handle_update(self):
        pass

    def handle_render(self, surf: pygame.Surface):
        # Input with awful overflow management
        text_surf = self.font.render(
            self.user_input, antialias=True, color=pygame.Color("black")
        )
        self.input.size[0] = max(200, text_surf.get_width() + 10)
        input_rect = self.input.get_rect()
        surf.blit(
            text_surf,
            (input_rect.x + 5, input_rect.centery - text_surf.get_height() // 2),
        )
        self.input.draw(surf)

        # Input with scroll overflow management - I FAILED TO HIDE THE TEXT @todo
        self.overflow_input.draw(surf)
        overflow_input_rect = self.overflow_input.get_rect()
        overflow_text = self.font.render(
            self.overflow_user_input, antialias=True, color=pygame.Color("black")
        )
        overflow_x = min(10, overflow_input_rect.size[0] - overflow_text.get_width())
        surf.blit(
            overflow_text,
            (
                overflow_input_rect.x - 5 + overflow_x,
                overflow_input_rect.centery - overflow_text.get_height() // 2,
            ),
        )

    def run(self):
        while True:
            time_delta = self.clock.tick(60) / 1000.0
            self.display.fill(pygame.Color("white"))

            self.handle_input()

            self.handle_update()

            self.handle_render(self.display)

            self.manager.update(time_delta)

            self.screen.blit(self.display, (0, 0))

            self.manager.draw_ui(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    Game().run()
