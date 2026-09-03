import pygame
from level import Level
from typing import Final

class Game:
    currLevel: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level | None
    preMenuImg: Final[pygame.Surface] = pygame.transform.scale(pygame.image.load("./images/premenubg.png").convert_alpha(), (960, 540))
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = None
    def drawPreMenuButton(self, screen: pygame.Surface) -> None:
        # drawMenu0Button('START GAME', (cwidth - menu0ButtonSize.w) / 2, (cheight - menu0ButtonSize.h) / 2, false, playGame);
        font: pygame.font.Font = pygame.font.Font("fonts/helveticabold.ttf", 30)
        rect: pygame.FRect = pygame.FRect(373.5, 251.55, 213.0, 36.9)
        cursorPos: tuple[int, int] = pygame.mouse.get_pos()
        isMouseDown: bool = pygame.mouse.get_pressed()[0]
        color: tuple[int, int, int] = (0, 0, 0)
        if rect.collidepoint(*cursorPos):
            if isMouseDown:
                color = (184, 184, 184)
            else:
                color = (212, 212, 212)
        else:
            color = (255, 255, 255)
            
        pygame.draw.rect(screen, color, rect, border_radius=round(6.65))

    def draw(self, screen: pygame.Surface):
        if self.currLevel == -2:
            screen.blit(self.preMenuImg, (0, 0))
            self.drawPreMenuButton(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        pass