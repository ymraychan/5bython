import pygame

from typing import Final

from collections.abc import Callable

from button.button import Button

# let menu0ButtonSize = {w: 273.0, h: 36.9, cr: 6.65};

font: Final[pygame.Font] = pygame.Font("fonts/helveticabold.ttf", 30)

color: Final[pygame.Color] = pygame.Color(255, 255, 255)
colorOnHover: Final[pygame.Color] = pygame.Color(212, 212, 212)
colorOnClick: Final[pygame.Color] = pygame.Color(184, 184, 184)
grayed: Final[pygame.Color] = colorOnClick # Coincindence since they have the same color
textColor: Final[pygame.Color] = pygame.Color(102, 102, 102)

class Menu0Btn(Button):

    fontRect: Final[pygame.FRect]
    def __init__(self, x: float, y: float, text: str,
                 actionOnClick: Callable[[], None], disabled: bool, width: float=273.0) -> None:
        if disabled:
            super().__init__(x, y, round(6.65), text, grayed, grayed, grayed,
                             font, 0, 0, textColor, actionOnClick, width, 36.9)
            # fontx, fonty has a dummy value of 0 because we're using a custom font drawing method anyway
        else:
            super().__init__(x, y, round(6.65), text, color, colorOnHover, colorOnClick,
                             font, 0, 0, textColor, actionOnClick, width, 36.9)
            # same here

        self.fontRect = self.fontSurf.get_frect()
        self.fontRect.center = (x + width / 2, y + (36.9 * 1.1) / 2)
    def draw(self, screen: pygame.Surface) -> None:
        super().drawRect(screen)
        screen.blit(self.fontSurf, self.fontRect)
        