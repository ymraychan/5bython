from collections.abc import Callable
from typing import Final

import pygame


class Button:
    rect: Final[pygame.FRect]
    color: Final[pygame.Color]
    color_on_hover: Final[pygame.Color]
    color_on_click: Final[pygame.Color]
    corner_radius: Final[int]
    font_surf: Final[pygame.Surface]
    font_x: Final[float]
    font_y: Final[float]
    action_on_click: Final[Callable[[], None]]

    def __init__(self, x: float, y: float, corner_radius: int, text: str, color: pygame.Color, color_on_hover: pygame.Color,
                 color_on_click: pygame.Color, font: pygame.Font, font_x: float, font_y: float, font_color: pygame.Color,
                 action_on_click: Callable[[], None], width: float, height: float) -> None:
        self.rect = pygame.FRect(x, y, width, height)
        self.color = color
        self.color_on_hover = color_on_hover
        self.color_on_click = color_on_click
        self.corner_radius = corner_radius
        self.font_surf = font.render(text, True, font_color)
        self.font_x = font_x
        self.font_y = font_y
        self.action_on_click = action_on_click


    def draw_rect(self, screen: pygame.Surface) -> None:
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, self.color_on_click, self.rect, border_radius=self.corner_radius)
            else:
                pygame.draw.rect(screen, self.color_on_hover, self.rect, border_radius=self.corner_radius)
            if pygame.mouse.get_just_released()[0]:
                self.action_on_click()
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.corner_radius)
    def draw(self, screen: pygame.Surface) -> None:
        self.draw_rect(screen)
        screen.blit(self.font_surf, (self.font_x, self.font_y))