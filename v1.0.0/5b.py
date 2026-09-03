import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
from music import playBgMusic
from typing import Final, Literal

pygame.init()

pygame.font.init()

TITLE: Final[str] = 'BFDIA 5b'
BLOCK_WIDTH: Final[int] = 30

WIDTH: Final[Literal[960]] = 960
HEIGHT: Final[Literal[540]] = 540

screen: pygame.Surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
playBgMusic()

from game import Game

running = True

game: Game = Game()

keysInstant: list[pygame.Event] = []

def events():
    global running, keysInstant
    keysInstant = pygame.event.get()
    for event in keysInstant:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
while running:
    dt: float = clock.tick(60) / 1000.0

    events()

    keysPressed = pygame.key.get_pressed()

    game.update(screen, keysPressed, keysInstant)
    game.draw(screen)

    pygame.display.flip()
