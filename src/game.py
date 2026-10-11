import pygame
from level import Level
from typing import Final, final
import menu.level_select
import menu.pre_menu
import menu.menu
from platformdirs import PlatformDirs
import read_data

@final
class Game:
    curr_level: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    save_folder: Final[PlatformDirs]
    save_data: read_data.SaveData
    num_deaths_req_so_far: int
    timer: int # measured in frames
    
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = Level(0)
        self.save_folder = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        self.timer = 0
        self.saveData = read_data.read_save_data()

    def draw(self, screen: pygame.Surface) -> None:
        if self.currLevel == -2:
            menu.pre_menu.draw(screen)
        elif self.currLevel == -1:
            menu.menu.draw(screen)
        elif self.currLevel == 0:
            menu.level_select.draw(screen)
        else:
            self.level.draw(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.timer += 1
        if self.currLevel == -2:
            self.currLevel = menu.pre_menu.currLevel
        elif self.currLevel == -1:
            menu.menu.levelProgress = self.saveData["lvlProgress"]
            self.currLevel = menu.menu.currLevel
        elif self.currLevel == 0:
            menu.level_select.update(screen)
            menu.level_select.timer += 1
            self.currLevel = menu.level_select.currLevel
        else:
            self.level.update(screen, keysPressed, keysInstant)
