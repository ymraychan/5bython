from button.menu0Btn import Menu0Btn
import webbrowser
from platformdirs import PlatformDirs
import os
import json
from readData import SaveData, readSaveData, writeSaveData

import pygame
from typing import Final, final

@final
class Menu:
	bgColor: Final[pygame.Color]
	svgMenu0: Final[pygame.Surface]
	watch5aBtn: Final[Menu0Btn]
	newGameBtn: Final[Menu0Btn]
	currLevel: int
	contGameBtn: Final[Menu0Btn]
	lcBtn: Final[Menu0Btn]
	exploreBtn: Final[Menu0Btn]
	levelProgress: int
	saveFolder: PlatformDirs
	saveFilePath: Final[str]

	def watch5a(self) -> None:
		webbrowser.open_new_tab("https://www.youtube.com/watch?v=4q77g4xo9ic")

	def watch5c(self) -> None:
		webbrowser.open_new_tab("https://www.youtube.com/watch?v=YrsRLT3u0Cg")

	def newGame(self) -> None:
		self.currLevel = 0
		dat: SaveData = readSaveData()
		dat["lvlProgress"] = 0
		writeSaveData(dat)
		

	def contGame(self) -> None:
		self.currLevel = 0
		
	def levelCreator(self) -> None:
		pass

	def explore(self) -> None:
		pass

	def __init__(self, platform: PlatformDirs) -> None:
		self.bgColor = pygame.Color(102, 102, 102)
		self.svgMenu0 = pygame.image.load("visuals/menu0.png").convert_alpha()
		self.watch5aBtn = Menu0Btn(665.55, 303.75, 'WATCH BFDIA 5a', self.watch5a, False)
		self.newGameBtn = Menu0Btn(665.55, 348.4, 'NEW GAME', self.newGame, False)
		self.currLevel = -1
		self.levelProgress = 1
		self.contGameBtn = Menu0Btn(665.55, 393.05, 'CONTINUE GAME', self.contGame, self.levelProgress <= 1)
		self.lcBtn = Menu0Btn(665.55, 437.7, 'LEVEL CREATOR', self.levelCreator, True)
		self.exploreBtn = Menu0Btn(665.55, 482.5, 'EXPLORE', self.explore, True)
		self.saveFolder = platform
		self.saveFilePath = os.path.join(self.saveFolder.user_data_dir, "data.json")

	def draw(self, screen: pygame.Surface) -> None:
		screen.fill(self.bgColor)
		screen.blit(self.svgMenu0)
		self.watch5aBtn.draw(screen)
		self.newGameBtn.draw(screen)
		self.contGameBtn.draw(screen)
		self.lcBtn.draw(screen)
		self.exploreBtn.draw(screen)