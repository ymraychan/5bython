from button.levelBtn import LevelBtn
from platformdirs import PlatformDirs

import pygame
from typing import Final

import json
import os
from types5b import SaveData

import read_data

menu2png: Final[pygame.Surface] = pygame.image.load("visuals/menu2.png").convert()
_cameraX: float = 0
_cameraY: float = 0
cameraX: float = 0
cameraY: float = 0
font5bSurf: Final[pygame.Surface] = pygame.Font("fonts/arialbold.ttf", 115).render("5b", True, (0, 0, 0))
levelSurf: Final[pygame.Surface] = pygame.Font("fonts/helveticabold.ttf", 48).render("Level", True, (0, 0, 0))
selectSurf: Final[pygame.Surface] = pygame.Font("fonts/helveticabold.ttf", 48).render("Select", True, (0, 0, 0))
wtFont: Final[pygame.Font] = pygame.Font("fonts/helvetica.ttf", 40)
winTokenSurf: Final[pygame.Surface] = pygame.transform.smoothscale(pygame.image.load("visuals/wintoken.png").convert_alpha(), (73, 73))
platform: Final[PlatformDirs] = read_data.saveFolder
levelSelectBtn: list[LevelBtn]
saveData: SaveData = read_data.readSaveData()
currLevel: int = 0
saveFilePath: Final[str] = read_data.saveFilePath
winTokenCount: int = len(saveData["winToken"])
winTokenTextSurf: pygame.Surface = wtFont.render(f"x {winTokenCount}", True, "#000000")
timer: int = 0 # measured in frames

# _menu2pngUnscaled = pygame.image.load("visuals/menu2.png").convert()
# menu2png = pygame.transform.scale_by(_menu2pngUnscaled, 1/3).convert() # unexplainable downscaling

levelSelectBtn = []
for i in range(133):
    j = i
    if j >= 100:
        j += 19
    color = 1
    if i >= 100:
        color = 1
    if i in saveData["winToken"]:
        color = 4
    elif saveData["lvlProgress"] == i:
        color = 2
    elif saveData["lvlProgress"] > i:
        color = 3
    text = f"{(i+1):03d}"
    if i >= 100:
        text = f"B{(i-99):02d}"
    levelSelectBtn.append(LevelBtn(text, (j % 8) * 110 + 45, int(j / 8) * 50 + 160, i, color, i+1))

    

def draw(screen: pygame.Surface) -> None:
    global currLevel
    screen.blit(menu2png, (cameraX, cameraY))
    screen.blit(font5bSurf, (47 + cameraX, 23 + cameraY))
    screen.blit(levelSurf, (211 + cameraX, 30 + cameraY))
    screen.blit(selectSurf, (211 + cameraX, 80 + cameraY))
    screen.blit(winTokenSurf, (398.5 + cameraX, 34.5 + cameraY))
    for btn in levelSelectBtn:
        _ = btn.draw(screen, cameraX, cameraY)
        if _ != -1:
            currLevel = _

    screen.blit(winTokenTextSurf, (477.95 + cameraX, 50.9 + cameraY))
    # TODO: Draw a bunch more stuff


def update(screen: pygame.Surface) -> None:
    global _cameraX, _cameraY, cameraX, cameraY
    xmouse, ymouse = pygame.mouse.get_pos()
    if xmouse < 587 or ymouse < 469:
        if ymouse <= 180:
            _cameraY = min(max(_cameraY - (180 - ymouse) * 0.1, 0), 1080)
        elif ymouse >= 360:
            # cameraY = min(max(cameraY + (ymouse - 360) * 0.1,), 1080)
            _cameraY = min(_cameraY + (ymouse - 360) * 0.1, 1080)
        cameraX = _cameraX * -1
        cameraY = _cameraY * -1

		

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