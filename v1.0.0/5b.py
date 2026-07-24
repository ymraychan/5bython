import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
import loadLevels
import block
import draw
from music import playBgMusic
from typing import Final, Optional

pygame.init()

TITLE: Final[str] = 'BFDIA 5b'
BLOCK_WIDTH: Final[int] = 30

WIDTH: Final[int] = min(pygame.display.get_desktop_sizes()[0][0], 32 * BLOCK_WIDTH)
HEIGHT: Final[int] = min(pygame.display.get_desktop_sizes()[0][1], 18 * BLOCK_WIDTH)

level = 0

screen: pygame.Surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption(title=TITLE)
clock = pygame.time.Clock()
playBgMusic()

blocks: list[list[block.Block | None]] = loadLevels.loadLevels(level)
def update():
    for _ in blocks:
        for b in _:
            if b:
                b.addFrame()


running = True
def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
while running:
    dt: float = clock.tick(60) / 1000.0

    events()

    update()

    draw.draw(screen, level, WIDTH, HEIGHT, blocks)

    pygame.display.flip()