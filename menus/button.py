import pygame


class Button:
    def __init__(
        self,
        text,
        pos,
        size,
        func,
        font=None,
        txt_color=None,
        btn_color=None,
        antialias=True,
    ) -> None:
        self.text = text
        self.pos = pos
        self.size = size
        self.func = func
        self.antialias = antialias
        self.font = font
        if self.font is None:
            self.font = pygame.font.SysFont("Courier New", 20)

        self.txt_color = txt_color
        if txt_color is None:
            self.txt_color = pygame.Color("white")

        self.btn_color = btn_color
        if btn_color is None:
            self.btn_color = pygame.Color("black")

    def __get_rect(self):
        return pygame.Rect(self.pos, self.size)

    def handle_click(self, click_position):
        if self.__get_rect().collidepoint(click_position):
            self.func()

    def draw(self, surf):
        this_rect = self.__get_rect()
        pygame.draw.rect(surf, self.btn_color, this_rect)
        text2render = self.font.render(
            self.text, color=self.txt_color, antialias=self.antialias
        )
        surf.blit(
            text2render,
            pygame.Vector2(this_rect.center)
            - pygame.Vector2(text2render.get_width(), text2render.get_height()) // 2,
        )
