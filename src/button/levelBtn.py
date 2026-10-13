from typing import Final

import pygame

bold_40_px_hect: Final[pygame.Font] = pygame.Font("fonts/helveticabold.ttf", 41)

black: Final[pygame.Color] = pygame.Color(0, 0, 0)

class LevelBtn:
    # {w: 100, h: 40}
    
    font_rect: Final[pygame.FRect]
    rect: Final[pygame.FRect]
    color: Final[pygame.Color]
    color_on_hover: Final[pygame.Color]
    color_on_click: Final[pygame.Color]
    font_surf: Final[pygame.Surface]
    level: Final[int]

    def __init__(self, text: str, x: float, y: float, id: int, color: int, level: int):
        fill: list[str] = ["0, 0, 0"] # [color, color_on_click, color_on_hover] # just like the js version
        if color == 1:
            fill = ["#585858", "#585858", "#585858"]
        elif color == 2:
            fill = ["#ff8000", "#d56a00", "#ffaa55"]
        elif color == 3:
            fill = ["#efe303", "#c6bc02", "#ffff99"]
        elif color == 4:
            fill = ["#00cc00", "#00a200", "#22ff22"]
        else:
            raise ValueError("Color must be 1, 2, 3, or 4")
        
        self.rect = pygame.FRect(x, y, 100, 40)
        self.color = pygame.Color(fill[0])
        self.color_on_hover = pygame.Color(fill[2])
        self.color_on_click = pygame.Color(fill[1])
        self.font_surf = bold_40_px_hect.render(text, True, (0, 0, 0))
        self.level = level

        self.font_rect = self.font_surf.get_frect()
        self.font_rect.center = (x + 100 / 2, y + (40 * 1.1) / 2)

    def draw_rect(self, screen: pygame.Surface, cx: float, cy: float) -> int:
        _rect: pygame.FRect = self.rect.move(cx, cy)
        level_playing: int = -1
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, self.color_on_click, _rect.inflate(2, 2))
            else:
                pygame.draw.rect(screen, self.color_on_hover, _rect.inflate(2, 2))
            if pygame.mouse.get_just_released()[0]:
                level_playing = self.level
        else:
            pygame.draw.rect(screen, self.color, _rect.inflate(2, 2))
        pygame.draw.rect(screen, "#000000", _rect.inflate(2, 2), width=2)
        return level_playing

    def draw_font(self, screen: pygame.Surface, cx: float, cy: float) -> None:
        screen.blit(self.font_surf, self.font_rect.move(cx, cy))

    def draw(self, screen, cx, cy) -> int:
        _ = self.draw_rect(screen, cx, cy)
        self.draw_font(screen, cx, cy)
        return _