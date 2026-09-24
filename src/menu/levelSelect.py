from button.levelBtn import LevelBtn
from platformdirs import PlatformDirs

import pygame
from typing import Final, final
from collections.abc import Callable

import json
import os

import readData
from readData import SaveData

@final
class LevelSelect:
    menu2png: Final[pygame.Surface]
    _cameraX: float
    _cameraY: float
    cameraX: float
    cameraY: float
    font5bSurf: Final[pygame.Surface]
    levelSurf: Final[pygame.Surface]
    selectSurf: Final[pygame.Surface]
    wtFont: Final[pygame.Font]
    winTokenSurf: Final[pygame.Surface]
    platform: Final[PlatformDirs]
    levelSelectBtn: list[LevelBtn]
    saveData: SaveData
    currLevel: int
    saveFilePath: Final[str]
    winTokenCount: int
    winTokenTextSurf: pygame.Surface
    timer: int # measured in frames



    def playLevel(self, lvl: int) -> None:
        self.currLevel = lvl
    
    def __init__(self) -> None:
        # self._menu2pngUnscaled = pygame.image.load("visuals/menu2.png").convert()
        # self.menu2png = pygame.transform.scale_by(self._menu2pngUnscaled, 1/3).convert() # unexplainable downscaling
        self.menu2png = pygame.image.load("visuals/menu2.png").convert()
        self._cameraX = self.cameraX = 0
        self._cameraY = self.cameraY = 0
        self.font5bSurf = pygame.Font("fonts/arialbold.ttf", 115).render("5b", True, (0, 0, 0))
        self.levelSurf = pygame.Font("fonts/helveticabold.ttf", 48).render("Level", True, (0, 0, 0))
        self.selectSurf = pygame.Font("fonts/helveticabold.ttf", 48).render("Select", True, (0, 0, 0))
        self.winTokenSurf = pygame.transform.smoothscale(pygame.image.load("visuals/wintoken.png").convert_alpha(), (73, 73))
        self.platform = readData.saveFolder
        self.saveFilePath = readData.saveFilePath
        self.wtFont = pygame.Font("fonts/helvetica.ttf", 40)
        readData.createSaveData()

		
        self.saveData = readData.readSaveData()

        self.levelSelectBtn = []
        for i in range(133):
            j = i
            if j >= 100:
                j += 19
            color = 1
            if i >= 100:
                color = 1
            if i in self.saveData["winToken"]:
                color = 4
            elif self.saveData["lvlProgress"] == i:
                color = 2
            elif self.saveData["lvlProgress"] > i:
                color = 3
            text = f"{(i+1):03d}"
            if i >= 100:
                text = f"B{(i-99):02d}"
            self.levelSelectBtn.append(LevelBtn(text, (j % 8) * 110 + 45, int(j / 8) * 50 + 160, i, color, i))
        self.winTokenCount = len(self.saveData["winToken"])
        self.winTokenTextSurf = self.wtFont.render(f"x {self.winTokenCount}", True, "#000000")
        self.timer = 0

        

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.menu2png, (self.cameraX, self.cameraY))
        screen.blit(self.font5bSurf, (47 + self.cameraX, 23 + self.cameraY))
        screen.blit(self.levelSurf, (211 + self.cameraX, 30 + self.cameraY))
        screen.blit(self.selectSurf, (211 + self.cameraX, 80 + self.cameraY))
        screen.blit(self.winTokenSurf, (398.5 + self.cameraX, 34.5 + self.cameraY))
        for btn in self.levelSelectBtn:
            if btn.draw(screen, self.cameraX, self.cameraY) != -1:
                self.currLevel = btn.draw(screen, self.cameraX, self.cameraY)
        screen.blit(self.winTokenTextSurf, (477.95 + self.cameraX, 50.9 + self.cameraY))
        # TODO: Draw a bunch more stuff


    def update(self, screen: pygame.Surface) -> None:
        xmouse, ymouse = pygame.mouse.get_pos()
        if xmouse < 587 or ymouse < 469:
            if ymouse <= 180:
                self._cameraY = min(max(self._cameraY - (180 - ymouse) * 0.1, 0), 1080)
            elif ymouse >= 360:
                # self.cameraY = min(max(self.cameraY + (ymouse - 360) * 0.1,), 1080)
                self._cameraY = min(self._cameraY + (ymouse - 360) * 0.1, 1080)
            self.cameraX = self._cameraX * -1
            self.cameraY = self._cameraY * -1

		

"""
function drawLevelMap() {
	ctx.drawImage(svgMenu2, 0, 0, svgMenu2.width/scaleFactor, svgMenu2.height/scaleFactor);

	ctx.fillStyle = '#000000';
	ctx.textAlign = 'left';
	ctx.textBaseline = 'top';
	ctx.font = '21px Helvetica';
	ctx.fillText(toHMS(timer), 767.3, 27.5);
	ctx.fillText(deathCount.toLocaleString(), 767.3, 55.9);
	ctx.textAlign = 'right';
	ctx.fillText('Time:', 757.05, 27.5);
	ctx.fillText('Deaths:', 757.05, 55.9);
	if (levelProgress > 0) {
		ctx.font = '14px Helvetica';
		ctx.textAlign = 'right';
		ctx.fillText('Minimal deaths to complete level ' + levelProgress + ':', 756.3, 90.5);
		ctx.font = '21px Helvetica';
		ctx.fillText('Unnecessary deaths:', 756.3, 116.8);
		ctx.textAlign = 'left';
		ctx.fillText(mdao[levelProgress - 1], 767.3, 85.4);
		ctx.fillText((deathCount - mdao[levelProgress - 1]).toLocaleString(), 767.3, 116.8);
	}
}"""