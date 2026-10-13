from typing import Final

import pygame
from mypy_extensions import i32

import properties
from get_levels import get_level_bg_id

_tmp: list[list[pygame.Surface]] = []

for i in range(135):
    obj: list[pygame.Surface] = []
    frame_count: i32 = properties.block_properties[i][16]
    if frame_count == 0:
        obj = [pygame.Surface((30, 30), pygame.SRCALPHA)]
    for j in range(frame_count):
        if frame_count > 1:
            if len(properties.block_properties[i]) == 19:
                obj.append(
                    pygame.image.load(f"visuals/blocks/b{i:04d}f{properties.block_properties[i][18][j]:04d}.png")
                    .convert_alpha())
            else:
                obj.append(pygame.image.load(f"visuals/blocks/b{i:04d}f{j:04d}.png").convert_alpha())
        else:
            obj.append(pygame.image.load(f"visuals/blocks/b{i:04d}.png").convert_alpha())
    _tmp.append(obj)


_tmp = []

for i in range(56):
    obj: list[pygame.Surface] = []
    frame_count = int(properties.char_d[i][7])
    for j in range(frame_count):
        obj.append(
            pygame.image.load(
                f"visuals/entities/e{i:04d}.png" if frame_count == 1
                else f"visuals/entities/e{i:04d}f{j:04d}.png"
            )
        .convert_alpha())
    _tmp.append(obj)


block_images: Final[list[list[pygame.Surface]]] = _tmp
entity_images: Final[list[list[pygame.Surface]]] = _tmp
bg_images: Final[list[pygame.Surface]] = [ pygame.transform.scale(
    pygame.image.load(f"visuals/bg/bg{get_level_bg_id(i):04d}.png").convert(), (960, 540)
    )
    for i in range(12) ]

border_surf: Final[list[pygame.Surface]] = [pygame.image.load(f"visuals/borders/tb{_:04d}.png") for _ in range(38)]
svg_menu_0: Final[pygame.Surface] = pygame.image.load("visuals/menu0.png").convert_alpha()
menu_2_surf: Final[pygame.Surface] = pygame.image.load("visuals/menu2.png").convert()
win_token_surf: Final[pygame.Surface] = pygame.transform.smoothscale(pygame.image.load("visuals/wintoken.png").convert_alpha(), (73, 73))
pre_menu_surf: Final[pygame.Surface] = pygame.transform.scale(pygame.image.load("visuals/premenubg.png").convert_alpha(), (960, 540))

del _tmp
