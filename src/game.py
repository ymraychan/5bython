import pygame
from level import Level
from typing import Final, final
from menu.preMenu import PreMenu
from menu.menu import Menu
from menu.levelSelect import LevelSelect
from platformdirs import PlatformDirs
import os
import json
import readData

@final
class Game:
    currLevel: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    preMenuStage: Final[PreMenu]
    menuStage: Final[Menu]
    levelSelectStage: Final[LevelSelect]
    saveFolder: Final[PlatformDirs]
    saveData: readData.SaveData
    numDeathsReqSoFar: int
    timer: int # measured in frames
    
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = Level(0)
        self.saveFolder = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        self.preMenuStage = PreMenu()
        self.menuStage = Menu(self.saveFolder)
        self.levelSelectStage = LevelSelect()
        self.timer = 0
        self.saveData = readData.readSaveData()

    def draw(self, screen: pygame.Surface) -> None:
        if self.currLevel == -2:
            self.preMenuStage.draw(screen)
        elif self.currLevel == -1:
            self.menuStage.draw(screen)
        elif self.currLevel == 0:
            self.levelSelectStage.draw(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.timer += 1
        if self.currLevel == -2:
            self.currLevel = self.preMenuStage.currLevel
        elif self.currLevel == -1:
            self.menuStage.levelProgress = self.saveData["lvlProgress"]
            self.currLevel = self.menuStage.currLevel
        elif self.currLevel == 0:
            self.levelSelectStage.update(screen)
            self.levelSelectStage.timer += 1