from typing import Any, Final

import pygame
from mypy_extensions import i32

import properties
from get_levels import char_to_code, get_level_bg_id, get_level_char_count
from load_images import block_images


class Block:
    block_properties: Final[list[list]] = properties.block_properties
    id: i32
    info: Final[list[Any]]
    frame: i32
    frame_count: i32
    image: pygame.Surface
    frames: list[pygame.Surface]
    rect: pygame.FRect
    x: Final[int]
    y: Final[int]
    door_light_x: Final[list[list[float]]] = properties.door_light_x
    level: i32
    loop: bool


    @staticmethod
    def map_range(value, min1, max1, min2, max2):
        return min2 + ((value - min1) / (max1 - min1)) * (max2 - min2)

    def add_frame(self) -> None:
        if self.frame_count <= 1:
            return
        self.frame += 1
        if self.frame == self.frame_count:
            self.frame = 0
        self.image = self.frames[self.frame]
    
    def __init__(self, x: int, y: int, level: int, block_id: int=0, name: str="", frame: int=0) -> None:
        self.id = char_to_code(name) if block_id == 0 else block_id
            
        self.frame = frame
        self.frame_count = self.block_properties[self.id][16]
        self.info = self.block_properties[self.id]
        self.image = block_images[self.id][self.frame]
        self.rect = self.image.get_frect()
        self.rect.bottomright = (x+30, y+30)
        self.x = x
        self.y = y
        self.level = level
        self.frames = block_images[self.id]

    def draw(self, screen: pygame.Surface) -> None:
        if self.id == 6:
            self.draw_door(screen)
            return
        if self.frame_count == 0: return
        else:
            screen.blit(self.image, self.rect)

    def draw_door_lights(self, screen: pygame.Surface) -> None:
        entities: int = get_level_char_count(self.level)
        for i in range(entities):
            rect = pygame.FRect(self.x - 30 + self.door_light_x[(entities-1) % 6 if i//6 == (entities-1)//6 else 5][i%6],
                                self.y - 80 + i // 6 * 10, 5, 5)
            pygame.draw.rect(screen, (0, 0, 0), rect)

    def draw_door(self, screen: pygame.Surface) -> None:
        doorColor: pygame.Color = pygame.Color(153, 153, 153) if get_level_bg_id(self.level) == 9 or get_level_bg_id(self.level) == 10 else pygame.Color(80, 80, 80)
        door=pygame.Rect((self.x-30), (self.y-90), 60, 120)
        pygame.draw.rect(screen, doorColor, door)
        self.draw_door_lights(screen)