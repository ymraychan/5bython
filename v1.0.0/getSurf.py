import pygame
from getLevels import getLevelName, getLevelBgId

pygame.font.init()

font = pygame.font.Font("fonts/helveticabold.ttf", 32)

def getBgSurf(level: int, width: int, height: int) -> pygame.surface.Surface:
    bgId: int = getLevelBgId(level)
    return pygame.transform.scale(pygame.image.load(f"images/bg/bg{bgId:04d}.png"), (width, height))

def getLevelTextSurf(level: int) -> pygame.surface.Surface:
    return font.render(f"{level+1:03d}. {getLevelName(level)}", True, (255, 255, 255))