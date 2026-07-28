import getSurf
import pygame
import block
from entity import Entity

def draw(screen: pygame.Surface, level: int, width: int, height: int, blocks: list[list[block.Block | None]], entities: list[Entity]) -> None:
    screen.fill((0, 0, 0))
    screen.blit(getSurf.getBgSurf(level, width, height), (0, 0))
    for _ in blocks:
        for tile in _:
            if tile:
                tile.draw(screen)

    for entity in entities:
        if entity:
            entity.draw(screen)
    screen.blit(getSurf.getLevelTextSurf(level), (12.85, 495.45))