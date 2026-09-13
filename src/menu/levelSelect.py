from button.menu0Btn import Menu0Btn
from platformdirs import PlatformDirs

import pygame
from typing import Final, final

@final
class LevelSelect:

    # _menu2pngUnscaled: Final[pygame.Surface]
    menu2png: Final[pygame.Surface]
    _cameraX: float
    _cameraY: float
    cameraX: float
    cameraY: float
    font5bSurf: Final[pygame.Surface]
    levelSurf: Final[pygame.Surface]
    selectSurf: Final[pygame.Surface]
    winTokenSurf: Final[pygame.Surface]
    platform: Final[PlatformDirs]
    levelSelectSurfs: list[pygame.Font]

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
        self.platform = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")
        for i in range(133):
            j = i + 19
        
        """	for (let i = 0; i < (playingLevelpack?levelCount:133); i++) {
		let j = i;
		if (!playingLevelpack && j >= 100) j += 19;
		let color = 1;
		if (i >= levelCount) color = 1;
		else if (gotCoin[i]) color = 4;
		else if (levelProgress == i) color = 2;
		else if (levelProgress > i) color = 3;
		// else if (i > 99 && i < bonusProgress + 100) {
		// 	if (!bonusesCleared[i - 100]) color = 2;
		// 	else color = 3;
		// }
		let text = '';
		if (!playingLevelpack && i >= 100) text = 'B' + (i - 99).toString().padStart(2, '0');
		else text = (i + 1).toString().padStart(3, '0');
		drawLevelButton(text, (j % 8) * 110 + 45, Math.floor(j / 8) * 50 + 160, i, color);
	}"""

    """function drawLevelButton(text, x, y, id, color) {
	let fill = '#585858';
	if (color == 2) fill = '#ff8000';
	else if (color == 3) fill = '#efe303';
	else if (color == 4) fill = '#00cc00';
	if (color > 1) {
		if (
			onRect(_xmouse, _ymouse + cameraY, x, y, levelButtonSize.w, levelButtonSize.h) &&
			(_xmouse < 587 || _ymouse < 469)
		) {
			onButton = true;
			if (mouseIsDown) {
				if (color == 2) fill = '#d56a00';
				else if (color == 3) fill = '#c6bc02';
				else if (color == 4) fill = '#00a200';
				levelButtonClicked = id;
			} else {
				if (color == 2) fill = '#ffaa55';
				else if (color == 3) fill = '#ffff99';
				else if (color == 4) fill = '#22ff22';
			}
		}
		if (!mouseIsDown && levelButtonClicked === id) {
			levelButtonClicked = -1;
			if (id <= levelProgress) { // || (id > 99 && id < bonusProgress + 100)
				playLevel(id);
				whiteAlpha = 100;
			}
		}
	}

	ctx.fillStyle = fill;
	ctx.fillRect(x, y, levelButtonSize.w, levelButtonSize.h);
	ctx.lineWidth = 2;
	ctx.strokeStyle = '#000000';
	ctx.strokeRect(x, y, levelButtonSize.w, levelButtonSize.h);

	ctx.font = 'bold 41px Helvetica';
	ctx.fillStyle = '#000000';
	ctx.textAlign = 'center';
	ctx.textBaseline = 'middle';
	ctx.fillText(text, x + levelButtonSize.w / 2, y + (levelButtonSize.h * 1.1) / 2);
}"""

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.menu2png, (self.cameraX, self.cameraY))
        screen.blit(self.font5bSurf, (47 + self.cameraX, 23 + self.cameraY))
        screen.blit(self.levelSurf, (211 + self.cameraX, 30 + self.cameraY))
        screen.blit(self.selectSurf, (211 + self.cameraX, 80 + self.cameraY))
        screen.blit(self.winTokenSurf, (398.5 + self.cameraX, 34.5 + self.cameraY))
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

	if (!playingLevelpack) {
		ctx.font = 'bold 115px Arial';
		ctx.fillText('5b', 47, 23);
		ctx.font = '48px Helvetica';
		ctx.fillText('Level', 211, 30);
		ctx.fillText('Select', 211, 80);

		ctx.drawImage(svgTiles[12], 398.5, 34.5, 73, 73);
		ctx.font = '40px Helvetica';
		ctx.fillText('x ' + coins, 477.95, 50.9);
	} else {
		ctx.font = 'bold 48px Helvetica';
		// ctx.fillText(exploreLevelPageLevel.title, 55, 35);
		let titleLineCount = wrapText((levelpackType === 0)?exploreLevelPageLevel.title:lcSavedLevelpacks['l' + lcCurrentSavedLevelpack].title, 50, 35, 500, 48).length;
		if (levelpackType === 0) {
			const isGuest = exploreLevelPageLevel.creator === "";
			const username = isGuest ? "Guest" : exploreLevelPageLevel.creator.username;
			
			ctx.font = 'italic 21px Helvetica';
			ctx.fillText('by ' + username, 50, 32 + titleLineCount*48);
		}

		ctx.drawImage(svgTiles[12], 568.5, 29.5, 50, 50);
		ctx.font = '21px Helvetica';
		ctx.fillText('x ' + coins, 627.95, 45.9);
	}

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
	for (let i = 0; i < (playingLevelpack?levelCount:133); i++) {
		let j = i;
		if (!playingLevelpack && j >= 100) j += 19;
		let color = 1;
		if (i >= levelCount) color = 1;
		else if (gotCoin[i]) color = 4;
		else if (levelProgress == i) color = 2;
		else if (levelProgress > i) color = 3;
		// else if (i > 99 && i < bonusProgress + 100) {
		// 	if (!bonusesCleared[i - 100]) color = 2;
		// 	else color = 3;
		// }
		let text = '';
		if (!playingLevelpack && i >= 100) text = 'B' + (i - 99).toString().padStart(2, '0');
		else text = (i + 1).toString().padStart(3, '0');
		drawLevelButton(text, (j % 8) * 110 + 45, Math.floor(j / 8) * 50 + 160, i, color);
	}
}"""

# This part is done
"""		case 2:
			drawLevelMap();
			if (_xmouse < 587 || _ymouse < 469) {
				if (_ymouse <= 180) {
					cameraY = Math.min(Math.max(cameraY - (180 - _ymouse) * 0.1, 0), 1080);
				} else if (_ymouse >= 360) {
					cameraY = Math.min(Math.max(cameraY + (_ymouse - 360) * 0.1, ), 1080);
				}
			}
			break;
"""