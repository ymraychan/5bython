import pygame
from collections.abc import Callable
from typing import Final

class Button:
    rect: Final[pygame.FRect]
    color: Final[pygame.Color]
    colorOnHover: Final[pygame.Color]
    colorOnClick: Final[pygame.Color]
    cornerRadius: Final[int]
    fontSurf: Final[pygame.Surface]
    fontx: Final[float]
    fonty: Final[float]
    actionOnClick: Final[Callable[[], None]]

    def __init__(self, x: float, y: float, cornerRadius: int, text: str, color: pygame.Color, colorOnHover: pygame.Color,
                 colorOnClick: pygame.Color, font: pygame.Font, fontx: float, fonty: float, fontColor: pygame.Color,
                 actionOnClick: Callable[[], None], width: float, height: float) -> None:
        self.rect = pygame.FRect(x, y, width, height)
        self.color = color
        self.colorOnHover = colorOnHover
        self.colorOnClick = colorOnClick
        self.cornerRadius = cornerRadius
        self.fontSurf = font.render(text, True, fontColor)
        self.fontx = fontx
        self.fonty = fonty
        self.actionOnClick = actionOnClick


    def drawRect(self, screen: pygame.Surface) -> None:
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, self.colorOnClick, self.rect, border_radius=self.cornerRadius)
            else:
                pygame.draw.rect(screen, self.colorOnHover, self.rect, border_radius=self.cornerRadius)
            if pygame.mouse.get_just_released()[0]:
                self.actionOnClick()
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.cornerRadius)
    def draw(self, screen: pygame.Surface) -> None:
        self.drawRect(screen)
        screen.blit(self.fontSurf, (self.fontx, self.fonty))