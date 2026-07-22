import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
import loadLevels
import block
from bg.getBg import getBg
from bg.drawBg import drawBg
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

blocks: list[list[Optional[block.Block]]] = loadLevels.loadLevels(level)

def update():
    for _ in blocks:
        for b in _:
            if b:
                if b.frameCount > 1:
                    b.addFrame()

bg = getBg(level, WIDTH, HEIGHT)

def draw():
    screen.fill((0, 0, 0))
    screen.blit(bg, (0,0))
    for _ in blocks:
        for tile in _:
            if tile:
                tile.draw(screen)
    drawBg(screen, level)

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

    draw()

    pygame.display.flip()
