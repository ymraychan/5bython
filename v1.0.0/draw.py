import getSurf
import pygame
import block
import loadLevels

def draw(screen: pygame.Surface, level: int, width: int, height: int, blocks: list[list[block.Block | None]]) -> None:
    screen.blit(getSurf.getBgSurf(level, width, height), (0, 0))
    for _ in blocks:
        for tile in _:
            if tile:
                tile.draw(screen)
    screen.blit(getSurf.getLevelTextSurf(level), (12.85, 495.45))