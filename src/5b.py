import os

os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers

import sys

import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen: pygame.Surface = pygame.display.set_mode(size=(960, 540))
pygame.display.set_caption('BFDIA 5b')
clock = pygame.time.Clock()
if sys.platform == "win32":
    tickloop = pygame.time.Clock.tick_busy_loop
else:
    tickloop = pygame.time.Clock.tick

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

while running:
    dt: float = tickloop(clock, 60) / 1000.0

    events()

    keysPressed = pygame.key.get_pressed()

    game.update(screen, keysPressed, keysInstant)
    game.draw(screen)

    # print(clock.get_fps())

    pygame.display.flip()
