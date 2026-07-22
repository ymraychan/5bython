from getLevels import getLevelName

import pygame

pygame.font.init()

font = pygame.font.Font("fonts/helveticabold.ttf", 32)

def drawBg(screen: pygame.Surface, level: int):
    textToDraw: str = f"{level+1:03d}. {getLevelName(level)}"
    textColor: tuple[int, int, int] = (255, 255, 255)
    textSurf = font.render(textToDraw, True, textColor)
    screen.blit(textSurf, (round(12.85), round(495.45)))