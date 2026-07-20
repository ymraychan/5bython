import pygame
from pgzero.builtins import images
import getLevels

def getBg(level: int, width: int, height: int) -> pygame.surface.Surface:
    bgId = getLevels.getLevelBgId(level)
    return pygame.transform.scale(images.load(f"bg/bg{bgId:04d}"), (width, height)) # type: ignore