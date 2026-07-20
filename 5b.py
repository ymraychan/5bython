import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun
import pygame
import logic
import loadLevels
import block
import Door
from typing import Final, Optional

TITLE: Final[str] = 'BFDIA 5b'
BLOCK_WIDTH: Final[int] = 30

_: list[tuple[int, int]] = pygame.display.get_desktop_sizes()

WIDTH: Final[int] = min(_[0][0], 32 * BLOCK_WIDTH)
HEIGHT: Final[int] = min(_[0][1], 18 * BLOCK_WIDTH)

del _


blocks: list[list[Optional[block.Block]]] = loadLevels.loadLevels(52)

def update():
    for _ in blocks:
        for b in _:
            if b:
                if b.frameCount > 1:
                    b.addFrame()


def draw():
    screen.clear() # type: ignore
    screen.blit(pygame.transform.scale(images.bg.bg0000, (WIDTH, HEIGHT)), (0,0)) # type: ignore
    for _ in blocks:
        for tile in _:
            if tile:
                tile.draw(screen) # type: ignore

pygame.mixer.music.load("data/the fiber 16x loop.wav")
pygame.mixer.music.play(-1)
            
pgzrun.go()
