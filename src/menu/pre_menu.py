from button.menu0Btn import Menu0Btn

import pygame
from typing import Final

def startGame() -> None:
    global currLevel
    pygame.mixer.music.load("data/the fiber 16x loop.wav")
    pygame.mixer.music.play(-1)
    currLevel = -1

preMenuBtn: Final[Menu0Btn] = Menu0Btn(343.5, 251.55, 'START GAME', startGame, False)
preMenuImg: Final[pygame.Surface] = pygame.transform.scale(pygame.image.load("visuals/premenubg.png").convert_alpha(), (960, 540))
currLevel: int = -2

def draw(screen: pygame.Surface) -> None:
    screen.blit(preMenuImg)
    preMenuBtn.draw(screen)