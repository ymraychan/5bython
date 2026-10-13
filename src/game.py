from typing import Final, final

import pygame
from platformdirs import PlatformDirs

import menu.level_select
import menu.menu
import menu.pre_menu
import read_data
from level import Level


@final
class Game:
    curr_level: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    save_folder: Final[PlatformDirs]
    save_data: read_data.SaveData
    num_deaths_req_so_far: int
    timer: int # measured in frames
    
    def __init__(self) -> None:
        self.curr_level = -2
        self.level = Level(0)
        self.save_folder = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        self.timer = 0
        self.saveData = read_data.read_save_data()

    def draw(self, screen: pygame.Surface) -> None:
        if self.curr_level == -2:
            menu.pre_menu.draw(screen)
        elif self.curr_level == -1:
            menu.menu.draw(screen)
        elif self.curr_level == 0:
            menu.level_select.draw(screen)
        else:
            self.level.draw(screen)
            
    def update(self, screen: pygame.Surface, keys_pressed: pygame.key.ScancodeWrapper, keys_instant: list[pygame.event.Event]) -> None:
        self.timer += 1
        if self.curr_level == -2:
            self.curr_level = menu.pre_menu.curr_level
        elif self.curr_level == -1:
            menu.menu.level_progress = self.saveData["lvl_progress"]
            self.curr_level = menu.menu.curr_level
        elif self.curr_level == 0:
            menu.level_select.update(screen)
            menu.level_select.timer += 1
            self.curr_level = menu.level_select.curr_level
        else:
            self.level.update(screen, keys_pressed, keys_instant)
