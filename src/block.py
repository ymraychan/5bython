from typing import Final, Any
from mypy_extensions import i32

import pygame
from getLevels import charToCode, getLevelBgId, getLevelCharCount
import properties

blocks: list[list[pygame.Surface]] = []
for i in range(134):
    obj: list[pygame.Surface] = []
    frameCount: i32 = properties.blockProperties[i][16]
    if frameCount == 0:
        obj = [pygame.Surface((30, 30), pygame.SRCALPHA)]
    for j in range(frameCount):
        if frameCount > 1:
            if len(properties.blockProperties[i]) == 19:
                obj.append(pygame.image.load(f"visuals/blocks/b{i:04d}f{properties.blockProperties[i][18][j]:04d}.png").convert_alpha())
            else:
                obj.append(pygame.image.load(f"visuals/blocks/b{i:04d}f{j:04d}.png").convert_alpha())
        else:
            obj.append(pygame.image.load(f"visuals/blocks/b{i:04d}.png").convert_alpha())
    blocks.append(obj)

class Block:
    blockProperties: Final[list[list[Any]]] = properties.blockProperties
    id: i32
    info: Final[list[Any]]
    frame: i32
    frameCount: i32
    image: pygame.Surface
    frames: list[pygame.Surface]
    rect: pygame.FRect
    x: Final[int]
    y: Final[int]
    doorLightX: Final[list[list[float]]] = properties.doorLightX
    level: i32
    loop: bool


    @staticmethod
    def mapRange(value, min1, max1, min2, max2):
        return min2 + ((value - min1) / (max1 - min1)) * (max2 - min2)

    def addFrame(self) -> None:
        if self.frameCount <= 1:
            return
        self.frame += 1
        if self.frame == self.frameCount:
            self.frame = 0
        self.image = self.frames[self.frame]
    
    def __init__(self, x: int, y: int, level: int, block_id: int=0, name: str="", frame: int=0) -> None:
        self.id = charToCode(name) if block_id == 0 else block_id
            
        self.frame = frame
        self.frameCount = self.blockProperties[self.id][16]
        self.info = self.blockProperties[self.id]
        self.image = blocks[self.id][self.frame]
        self.rect = self.image.get_frect()
        self.rect.bottomright = (x+30, y+30)
        self.x = x
        self.y = y
        self.level = level
        self.frames = blocks[self.id]

    def draw(self, screen: pygame.Surface) -> None:
        if self.id == 6:
            self.drawDoor(screen)
            return
        if self.frameCount == 0: return
        else:
            screen.blit(self.image, self.rect)

    def drawDoorLights(self, screen: pygame.Surface) -> None:
        entities: int = getLevelCharCount(self.level)
        for i in range(entities):
            rect = pygame.FRect(self.x - 30 + self.doorLightX[(entities-1) % 6 if i//6 == (entities-1)//6 else 5][i%6],
                                self.y - 80 + i // 6 * 10, 5, 5)
            pygame.draw.rect(screen, (0, 0, 0), rect)

    def drawDoor(self, screen: pygame.Surface) -> None:
        doorColor: pygame.Color = pygame.Color(153, 153, 153) if getLevelBgId(self.level) == 9 or getLevelBgId(self.level) == 10 else pygame.Color(80, 80, 80)
        door=pygame.Rect((self.x-30), (self.y-90), 60, 120)
        pygame.draw.rect(screen, doorColor, door)
        self.drawDoorLights(screen)