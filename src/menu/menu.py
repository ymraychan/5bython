from button.menu0Btn import Menu0Btn
import webbrowser
import os
from read_data import SaveData, read_save_data, write_save_data, save_folder
from load_images import svg_menu_0

import pygame
from typing import Final


def watch_5a() -> None:
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=4q77g4xo9ic")

def watch_5c() -> None:
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=YrsRLT3u0Cg")

def new_game() -> None:
	global curr_level
	curr_level = 0
	dat: SaveData = read_save_data()
	dat["lvlProgress"] = 0
	write_save_data(dat)
	

def cont_game() -> None:
	global curr_level
	curr_level = 0
	
def level_creator() -> None:
	pass

def explore() -> None:
	pass


bg_color: Final[pygame.Color] = pygame.Color(102, 102, 102)
level_progress: int = 0
watch_5a_btn: Final[Menu0Btn] = Menu0Btn(665.55, 303.75, 'WATCH BFDIA 5a', watch_5a, False)
new_game_btn: Final[Menu0Btn] = Menu0Btn(665.55, 348.4, 'NEW GAME', new_game, False)
curr_level: int = -1
cont_game_btn: Final[Menu0Btn] = Menu0Btn(665.55, 393.05, 'CONTINUE GAME', cont_game, level_progress <= 1)
lc_btn: Final[Menu0Btn] = Menu0Btn(665.55, 437.7, 'LEVEL CREATOR', level_creator, True)
explore_btn: Final[Menu0Btn] = Menu0Btn(665.55, 482.5, 'EXPLORE', explore, True)
save_file_path: Final[str] = os.path.join(save_folder.user_data_dir, "data.json")


def draw(screen: pygame.Surface) -> None:
	screen.fill(bg_color)
	screen.blit(svg_menu_0)
	watch_5a_btn.draw(screen)
	new_game_btn.draw(screen)
	cont_game_btn.draw(screen)
	lc_btn.draw(screen)
	explore_btn.draw(screen)