import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
from music import playBgMusic
from typing import Final, Optional
from entity import Entity
from level import Level

pygame.init()

TITLE: Final[str] = 'BFDIA 5b'
BLOCK_WIDTH: Final[int] = 30

WIDTH: Final[int] = min(pygame.display.get_desktop_sizes()[0][0], 32 * BLOCK_WIDTH)
HEIGHT: Final[int] = min(pygame.display.get_desktop_sizes()[0][1], 18 * BLOCK_WIDTH)

screen: pygame.Surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption(title=TITLE)
clock = pygame.time.Clock()
playBgMusic()

running = True

level: Level = Level(0)

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

    keysPressed = pygame.key.get_pressed()
    keysInstant = pygame.event.get()

    level.update(screen, keysPressed, keysInstant)
    level.draw(screen)

    pygame.display.flip()
