from button.menu0Btn import Menu0Btn
import webbrowser
import os
from readData import SaveData, readSaveData, writeSaveData, saveFolder

import pygame
from typing import Final


def watch5a() -> None:
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=4q77g4xo9ic")

def watch5c() -> None:
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=YrsRLT3u0Cg")

def newGame() -> None:
	global currLevel
	currLevel = 0
	dat: SaveData = readSaveData()
	dat["lvlProgress"] = 0
	writeSaveData(dat)
	

def contGame() -> None:
	global currLevel
	currLevel = 0
	
def levelCreator() -> None:
	pass

def explore() -> None:
	pass


bgColor: Final[pygame.Color] = pygame.Color(102, 102, 102)
levelProgress: int = 0
svgMenu0: Final[pygame.Surface] = pygame.image.load("visuals/menu0.png").convert_alpha()
watch5aBtn: Final[Menu0Btn] = Menu0Btn(665.55, 303.75, 'WATCH BFDIA 5a', watch5a, False)
newGameBtn: Final[Menu0Btn] = Menu0Btn(665.55, 348.4, 'NEW GAME', newGame, False)
currLevel: int = -1
contGameBtn: Final[Menu0Btn] = Menu0Btn(665.55, 393.05, 'CONTINUE GAME', contGame, levelProgress <= 1)
lcBtn: Final[Menu0Btn] = Menu0Btn(665.55, 437.7, 'LEVEL CREATOR', levelCreator, True)
exploreBtn: Final[Menu0Btn] = Menu0Btn(665.55, 482.5, 'EXPLORE', explore, True)
saveFilePath: Final[str] = os.path.join(saveFolder.user_data_dir, "data.json")


def draw(screen: pygame.Surface) -> None:
	screen.fill(bgColor)
	screen.blit(svgMenu0)
	watch5aBtn.draw(screen)
	newGameBtn.draw(screen)
	contGameBtn.draw(screen)
	lcBtn.draw(screen)
	exploreBtn.draw(screen)