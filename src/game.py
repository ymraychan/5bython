import pygame
from level import Level
from typing import Final, final
from menu.preMenu import PreMenu
from menu.menu import Menu
from menu.levelSelect import LevelSelect
from platformdirs import PlatformDirs
import os
import json

@final
class Game:
    currLevel: int # -2 means pre menu, -1 means menu, 0 means level select
    level: Level
    preMenuStage: Final[PreMenu]
    menuStage: Final[Menu]
    levelSelectStage: Final[LevelSelect]
    saveFolder: Final[PlatformDirs]
    saveData: dict[str, list[int]]
    saveFilePath: Final[str]
    userdatPath: Final[str]
    
    def __init__(self) -> None:
        self.currLevel = -2
        self.level = Level(0)
        self.saveFolder = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        self.preMenuStage = PreMenu()
        self.menuStage = Menu(self.saveFolder)
        self.levelSelectStage = LevelSelect()
        os.makedirs(self.saveFolder.user_data_dir, mode=0o755, exist_ok=True)
        # TODO: read savedata
        self.saveFilePath = os.path.join(self.saveFolder.user_data_dir, "data.json")
        self.userdatPath = os.path.join(self.saveFolder.user_data_dir, "userdat.json")
        if not os.path.exists(self.saveFilePath):
            with open(self.saveFilePath, "w", encoding="utf-8") as f:
                f.write(json.dumps(
                    {
                        "lvlProgress": [1],
                        "winToken": [],
                        "deaths": [0],
                        "time": [0],
                    }
                , indent=4))
        with open(self.saveFilePath, "r", encoding="utf-8") as f:
            self.saveData = json.load(f)

    def draw(self, screen: pygame.Surface) -> None:
        if self.currLevel == -2:
            self.preMenuStage.draw(screen)
        elif self.currLevel == -1:
            self.menuStage.draw(screen)
        elif self.currLevel == 0:
            self.levelSelectStage.draw(screen)
            
    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        if self.currLevel == -2:
            self.currLevel = self.preMenuStage.currLevel
        elif self.currLevel == -1:
            self.menuStage.levelProgress = self.saveData["lvlProgress"][0]
            self.currLevel = self.menuStage.currLevel
        elif self.currLevel == 0:
            self.levelSelectStage.update(screen)