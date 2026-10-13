from button.menu0Btn import Menu0Btn

from load_images import pre_menu_surf

import pygame
from typing import Final

def start_game() -> None:
    global curr_level
    pygame.mixer.music.load("data/the fiber 16x loop.wav")
    pygame.mixer.music.play(-1)
    curr_level = -1

pre_menu_btn: Final[Menu0Btn] = Menu0Btn(343.5, 251.55, 'START GAME', start_game, False)
curr_level: int = -2

def draw(screen: pygame.Surface) -> None:
    screen.blit(pre_menu_surf)
    pre_menu_btn.draw(screen)