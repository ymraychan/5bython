from collections.abc import Callable
from typing import Final

import pygame

from button.button import Button

# let menu0ButtonSize = {w: 273.0, h: 36.9, cr: 6.65};

font: Final[pygame.Font] = pygame.Font("fonts/helveticabold.ttf", 30)

color: Final[pygame.Color] = pygame.Color(255, 255, 255)
color_on_hover: Final[pygame.Color] = pygame.Color(212, 212, 212)
color_on_click: Final[pygame.Color] = pygame.Color(184, 184, 184)
grayed: Final[pygame.Color] = color_on_click # Coincindence since they have the same color
text_color: Final[pygame.Color] = pygame.Color(102, 102, 102)

class Menu0Btn(Button):

    font_rect: Final[pygame.FRect]
    def __init__(self, x: float, y: float, text: str,
                 action_on_click: Callable[[], None], disabled: bool, width: float=273.0) -> None:
        if disabled:
            super().__init__(x, y, round(6.65), text, grayed, grayed, grayed,
                             font, 0, 0, text_color, action_on_click, width, 36.9)
            # fontx, fonty has a dummy value of 0 because we're using a custom font drawing method anyway
        else:
            super().__init__(x, y, round(6.65), text, color, color_on_hover, color_on_click,
                             font, 0, 0, text_color, action_on_click, width, 36.9)
            # same here

        self.font_rect = self.font_surf.get_frect()
        self.font_rect.center = (x + width / 2, y + (36.9 * 1.1) / 2)
    def draw(self, screen: pygame.Surface) -> None:
        super().draw_rect(screen)
        screen.blit(self.font_surf, self.font_rect)
        