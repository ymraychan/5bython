from typing import Final, Any, Optional

import pygame
from getLevels import charToCode
import properties
class Block:
    blockProperties: Final[list[list[Any]]] = properties.blockProperties
    id: Final[int]
    path: str
    info: Final[list[Any]]
    frame: int = 0
    frameCount: int
    image: pygame.Surface
    rect: pygame.Rect
    x: Final[int]
    y: Final[int]
    doorLightX: Final[list[list[int]]] = properties.doorLightX
    level: int
    
    def returnPath(self) -> str:
        p: str = ""
        if self.blockProperties[self.id][16] > 1:
            p = f"blocks/b{self.id:04d}f{self.frame:04d}"
        else:
            p = f"blocks/b{self.id:04d}"
        return p

    def addFrame(self) -> None:
        self.frame += 1
        self.frame %= self.frameCount
        self.path = self.returnPath()
        self.image = pygame.image.load(f"images/{self.path}.png").convert_alpha()
    
    def __init__(self, x: int, y: int, level: int, block_id: int=0, name: str="", frame: int=0) -> None:
        if block_id is None:
            self.id = charToCode(level, name)
        else:
            self.id = block_id
            
        self.frame = frame
        self.frameCount = self.blockProperties[self.id][16]
        self.path = self.returnPath()
        self.info = self.blockProperties[self.id]
        self.image = pygame.image.load(f"images/{self.path}.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y+30)
        self.x = x
        self.y = y
        self.level = level

    def draw(self, screen: pygame.Surface) -> None:
        if self.id == 6: self.drawDoor(screen)
        else:
            screen.blit(self.image, self.rect)

    def drawDoor(self, screen) -> None:
        door=pygame.Rect((self.x-30), (self.y-90), 60, 120)
        pygame.draw.rect(screen, (80, 80, 80), door)
