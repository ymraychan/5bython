from typing import Final, Any

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
    frames: list[pygame.Surface]
    rect: pygame.Rect
    x: Final[int]
    y: Final[int]
    doorLightX: Final[list[list[float]]] = properties.doorLightX
    level: int
    __cache: dict[int, list[pygame.Surface]] = {}
    
    def returnPath(self) -> str:
        p: str = ""
        if self.frameCount > 1:
            p = f"blocks/b{self.id:04d}f{self.frame:04d}"
        else:
            p = f"blocks/b{self.id:04d}"
        return p
    
    def __loadFrames(self) -> list[pygame.Surface]:
        l = []
        for _ in range(self.frameCount):
            l.append(pygame.image.load(f"images/blocks/b{self.id:04d}f{_:04d}.png").convert_alpha())
        return l

    def addFrame(self) -> None:
        if self.frameCount <= 1:
            return
        self.frame += 1
        self.frame %= self.frameCount
        self.image = self.frames[self.frame]
    
    def __init__(self, x: int, y: int, level: int, block_id: int=0, name: str="", frame: int=0) -> None:
        self.id = charToCode(level, name) if block_id == 0 else block_id
            
        self.frame = frame
        self.frameCount = self.blockProperties[self.id][16]
        self.path = self.returnPath()
        self.info = self.blockProperties[self.id]
        self.image = pygame.image.load(f"images/{self.path}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y+30)
        self.x = x
        self.y = y
        self.level = level
        if self.frameCount > 1:
            self.frames = self.__loadFrames()

    def draw(self, screen: pygame.Surface) -> None:
        if self.frameCount == 0:
            return
        if self.id == 6: self.drawDoor(screen)
        else:
            screen.blit(self.image, self.rect)

    def drawDoor(self, screen: pygame.Surface) -> None:
        door=pygame.Rect((self.x-30), (self.y-90), 60, 120)
        pygame.draw.rect(screen, (80, 80, 80), door)