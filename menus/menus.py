import abc
import sys

import pygame

from button import Button


class Menu(abc.ABC):
    def __init__(self, game, title) -> None:
        self.game = game
        self.title = title
        self.open = True

    @abc.abstractmethod
    def handle_input(self):
        pass

    @abc.abstractmethod
    def handle_render(self, surf):
        pass

    @abc.abstractmethod
    def run(self, condition):
        pass


class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game, "Main Menu")
        self.items = [
            Button("Audio", (50, 100), (100, 50), lambda: AudioMenu(game).run()),
            Button("Video", (50, 160), (100, 50), lambda: print("video")),
        ]

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.open = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    for item in self.items:
                        item.handle_click(pygame.mouse.get_pos())

    def handle_render(self, surf):
        text = self.game.font.render(
            self.title, antialias=True, color=pygame.Color("black")
        )
        surf.blit(text, (50, 50))

        for item in self.items:
            item.draw(self.game.display)

    def run(self):
        while self.open:
            self.game.display.fill(pygame.Color("white"))
            self.handle_input()
            self.handle_render(self.game.display)

            self.game.screen.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.clock.tick(60)


class AudioMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game, "Audio Menu")
        self.items = [
            Button("Music", (50, 100), (100, 50), lambda: print("set music volume")),
            Button("SFX", (50, 160), (100, 50), lambda: print("set SFX volume")),
        ]

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.open = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    for item in self.items:
                        item.handle_click(pygame.mouse.get_pos())

    def handle_render(self, surf):
        text = self.game.font.render(
            self.title, antialias=True, color=pygame.Color("black")
        )
        surf.blit(text, (50, 50))

        for item in self.items:
            item.draw(self.game.display)

    def run(self):
        while self.open:
            self.game.display.fill(pygame.Color("white"))
            self.handle_input()
            self.handle_render(self.game.display)

            self.game.screen.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.clock.tick(60)
