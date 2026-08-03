from block import Block
import getSurf
from loadEntities import loadEntities
from loadLevels import loadLevels
import pygame
from typing import Optional
from entity import Entity

class Level:
    lvlId: int
    blocks: list[list[Optional[Block]]]
    entities: list[Entity]

    def __init__(self, lvlId: int) -> None:
        self.lvlId = lvlId
        self.blocks = loadLevels(lvlId)
        self.entities = loadEntities(lvlId)

    def drawBg(self, surf: pygame.Surface) -> None:
        surf.blit(getSurf.getBgSurf(self.lvlId), (0, 0))

    def drawBlocks(self, surf: pygame.Surface) -> None:
        for _ in self.blocks:
            for tile in _:
                if tile:
                    tile.draw(surf)

    def drawOutlines(self, surf: pygame.Surface) -> None:
        pass

    def drawEntities(self, surf: pygame.Surface) -> None:
        for entity in self.entities:
            entity.draw(surf)

    def drawLevelText(self, surf: pygame.Surface) -> None:
        surf.blit(getSurf.getLevelTextSurf(self.lvlId), (12.85, 495.45))

    
    def draw(self, screen: pygame.Surface) -> None:
        self.drawBg(screen)
        self.drawBlocks(screen)
        self.drawOutlines(screen)
        self.drawEntities(screen)
        self.drawLevelText(screen)

    def updateAnimBlocks(self, surf: pygame.Surface) -> None:
        for _ in self.blocks:
            for b in _:
                if b:
                    b.addFrame()

    def updateEntities(self, surf: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        for entity in self.entities:
            entity.update(surf, keysPressed, keysInstant)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.updateAnimBlocks(screen)
        self.updateEntities(screen, keysPressed, keysInstant)
