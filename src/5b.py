import os
os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers

import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen: pygame.Surface = pygame.display.set_mode(size=(960, 540))
pygame.display.set_caption('BFDIA 5b')
clock = pygame.time.Clock()

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
