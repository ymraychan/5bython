import pygame
from getLevels import getLevelName, getLevelBgId
from typing import Any

pygame.font.init()

font = pygame.font.Font("fonts/helveticabold.ttf", 32)

__cache: dict[str, Any] = {}

def getBgSurf(level: int, width: int, height: int) -> pygame.surface.Surface:
    global __cache
    if __cache.get("bgSurf") is None or __cache.get("level") != level:
        __cache["level"] = level
        bgId: int = getLevelBgId(level)
        __cache["bgSurf"] = pygame.transform.scale(pygame.image.load(f"images/bg/bg{bgId:04d}.png"), (width, height)).convert()
    return __cache["bgSurf"]

def getLevelTextSurf(level: int) -> pygame.Surface:
    global __cache
    if __cache.get("levelTextSurf") is None or __cache.get("level") != level:
        __cache["levelTextSurf"] = font.render(f"{level+1:03d}. {getLevelName(level)}", True, (255, 255, 255)).convert_alpha()
        __cache["level"] = level
    return __cache["levelTextSurf"]