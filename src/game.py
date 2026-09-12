import pygame
from level import Level
from typing import Final, final
from menu.preMenu import PreMenu
from menu.menu import Menu
from menu.levelSelect import LevelSelect
from platformdirs import PlatformDirs
import os

@final
class Game:
    currLevel: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    preMenuStage: Final[PreMenu]
    menuStage: Final[Menu]
    levelSelectStage: Final[LevelSelect]
    saveFilePath: Final[PlatformDirs] = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
    
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = Level(0)
        self.preMenuStage = PreMenu()
        self.menuStage = Menu(0)
        self.levelSelectStage = LevelSelect()
        os.makedirs(self.saveFilePath.user_data_dir, exist_ok=True)

    def draw(self, screen: pygame.Surface) -> None:
        if self.currLevel == -2:
            self.preMenuStage.draw(screen)
        if self.currLevel == -1:
            self.menuStage.draw(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        if self.currLevel == -2:
            self.currLevel = self.preMenuStage.currLevel
        elif self.currLevel == -1:
            self.currLevel = self.menuStage.currLevel
            # self.menuStage.currLevel = self.level.lvlId