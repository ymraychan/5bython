from typing import Final

import pygame
from platformdirs import PlatformDirs

import read_data
from button.levelBtn import LevelBtn
from load_images import menu_2_surf, win_token_surf
from types_5b import SaveData

_camera_x: float = 0
_camera_y: float = 0
camera_x: float = 0
camera_y: float = 0
font_5b_surf: Final[pygame.Surface] = pygame.Font("fonts/arialbold.ttf", 115).render("5b", True, (0, 0, 0))
level_surf: Final[pygame.Surface] = pygame.Font("fonts/helveticabold.ttf", 48).render("Level", True, (0, 0, 0))
select_surf: Final[pygame.Surface] = pygame.Font("fonts/helveticabold.ttf", 48).render("Select", True, (0, 0, 0))
wt_font: Final[pygame.Font] = pygame.Font("fonts/helvetica.ttf", 40)
platform: Final[PlatformDirs] = read_data.save_folder
level_select_btn: list[LevelBtn]
save_data: SaveData = read_data.read_save_data()
curr_level: int = 0
save_file_path: Final[str] = read_data.save_file_path
win_token_count: int = len(save_data["win_token"])
win_token_text_surf: pygame.Surface = wt_font.render(f"x {win_token_count}", True, "#000000")
timer: int = 0 # measured in frames

level_select_btn = []
for i in range(133):
    j = i
    if j >= 100:
        j += 19
    color = 1
    if i >= 100:
        color = 1
    if i in save_data["win_token"]:
        color = 4
    elif save_data["lvl_progress"] == i:
        color = 2
    elif save_data["lvl_progress"] > i:
        color = 3
    text = f"{(i+1):03d}"
    if i >= 100:
        text = f"B{(i-99):02d}"
    level_select_btn.append(LevelBtn(text, (j % 8) * 110 + 45, int(j / 8) * 50 + 160, i, color, i+1))

    

def draw(screen: pygame.Surface) -> None:
    global curr_level
    screen.blit(menu_2_surf, (camera_x, camera_y))
    screen.blit(font_5b_surf, (47 + camera_x, 23 + camera_y))
    screen.blit(level_surf, (211 + camera_x, 30 + camera_y))
    screen.blit(select_surf, (211 + camera_x, 80 + camera_y))
    screen.blit(win_token_surf, (398.5 + camera_x, 34.5 + camera_y))
    for btn in level_select_btn:
        _ = btn.draw(screen, camera_x, camera_y)
        if _ != -1:
            curr_level = _

    screen.blit(win_token_text_surf, (477.95 + camera_x, 50.9 + camera_y))
    # TODO: Draw a bunch more stuff


def update(screen: pygame.Surface) -> None:
    global _camera_y, camera_x, camera_y
    xmouse, ymouse = pygame.mouse.get_pos()
    if xmouse < 587 or ymouse < 469:
        if ymouse <= 180:
            _camera_y = min(max(_camera_y - (180 - ymouse) * 0.1, 0), 1080)
        elif ymouse >= 360:
            # camera_y = min(max(camera_y + (ymouse - 360) * 0.1,), 1080)
            _camera_y = min(_camera_y + (ymouse - 360) * 0.1, 1080)
        camera_x = _camera_x * -1
        camera_y = _camera_y * -1

		

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