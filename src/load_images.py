import pygame

from typing import Final

import properties

from mypy_extensions import i32

block_images: Final[list[list[pygame.Surface]]]
entity_images: Final[list[list[pygame.Surface]]]
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

block_images = _tmp
tmp = []

for i in range(56):
    obj: list[pygame.Surface] = []
    frame_count: i32 = int(properties.char_d[i][7])
    for j in range(frame_count):
        obj.append(
            pygame.image.load(
                f"visuals/entities/e{i:04d}.png" if frame_count == 1
                else f"visuals/entities/e{i:04d}f{j:04d}.png"
            )
        .convert_alpha())
    _tmp.append(obj)

entity_images = _tmp
_tmp = []
