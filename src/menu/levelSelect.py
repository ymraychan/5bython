from button.menu0Btn import Menu0Btn

import pygame
from typing import Final, final

@final
class LevelSelect:
    preMenuBtn: Final[Menu0Btn]
    preMenuImg: Final[pygame.Surface] = pygame.transform.scale(pygame.image.load("visuals/premenubg.png").convert_alpha(), (960, 540))

    def startGame(self) -> None:
        pygame.mixer.music.load("data/the fiber 16x loop.wav")
        pygame.mixer.music.play(-1)

    def __init__(self) -> None:
        self.preMenuBtn = Menu0Btn(303.5, 251.55, 'START GAME', self.startGame, False)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.preMenuImg)
        self.preMenuBtn.draw(screen)