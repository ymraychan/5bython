import pygame
from level import Level
from typing import Final, final
import menu.levelSelect
import menu.preMenu
import menu.menu
from platformdirs import PlatformDirs
import os
import json
import readData

@final
class Game:
    currLevel: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    saveFolder: Final[PlatformDirs]
    saveData: readData.SaveData
    numDeathsReqSoFar: int
    timer: int # measured in frames
    
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = Level(0)
        self.saveFolder = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        self.timer = 0
        self.saveData = readData.readSaveData()

    def draw(self, screen: pygame.Surface) -> None:
        if self.currLevel == -2:
            menu.preMenu.draw(screen)
        elif self.currLevel == -1:
            menu.menu.draw(screen)
        elif self.currLevel == 0:
            menu.levelSelect.draw(screen)
        else:
            self.level.draw(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.timer += 1
        if self.currLevel == -2:
            self.currLevel = menu.preMenu.currLevel
        elif self.currLevel == -1:
            menu.menu.levelProgress = self.saveData["lvlProgress"]
            self.currLevel = menu.menu.currLevel
        elif self.currLevel == 0:
            menu.levelSelect.update(screen)
            menu.levelSelect.timer += 1
            self.currLevel = menu.levelSelect.currLevel
        else:
            self.level.update(screen, keysPressed, keysInstant)