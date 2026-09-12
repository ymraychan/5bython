from block import Block
from getLevels import *
import pygame
from entity.entity import Entity
from entity.character import Character
from entity.movingEntity import MovingEntity
from properties import blockProperties

class Level:
    lvlId: int
    blocks: list[list[Block]]
    borderimg: list[pygame.Surface] = [pygame.image.load(f"visuals/borders/tb{_:04d}.png") for _ in range(38)]
    bgSurf: pygame.Surface
    textSurf: pygame.Surface
    staticBlockSurf: pygame.Surface
    cameraX: float
    cameraY: float
    entities: list[Entity]

    def drawStaticBlocks(self, surf: pygame.Surface) -> None:
        for _ in self.blocks:
            for tile in _:
                if tile:
                    if tile.info[16] == 1 and tile.id != 6:
                        tile.draw(surf)

    def drawBorders(self, surf: pygame.Surface) -> None:
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[0])):
                this_tile = self.blocks[i][j]
                
                if not (this_tile and this_tile.info and this_tile.info[13]):
                    continue
                    
                def isEmpty(ni, nj):
                    if 0 <= ni < len(self.blocks) and 0 <= nj < len(self.blocks[0]):
                        neighbor = self.blocks[ni][nj]
                        return not (neighbor and neighbor.info and neighbor.info[13])
                    return False

                leftEmpty = isEmpty(i, j - 1)
                rightEmpty = isEmpty(i, j + 1)
                bottomEmpty = isEmpty(i + 1, j)
                topEmpty = isEmpty(i - 1, j)
                score = 0
                if rightEmpty: score += 1
                if leftEmpty: score += 2
                if bottomEmpty: score += 4
                if topEmpty: score += 8

                if score > 0:
                    surf.blit(self.borderimg[score - 1], (j * 30, i * 30))
                    
                if not topEmpty and not leftEmpty and isEmpty(i - 1, j - 1):
                    surf.blit(self.borderimg[34], (j * 30, i * 30))
                if not topEmpty and not rightEmpty and isEmpty(i - 1, j + 1):
                    surf.blit(self.borderimg[35], (j * 30, i * 30))
                if not bottomEmpty and not rightEmpty and isEmpty(i + 1, j + 1):
                    surf.blit(self.borderimg[36], (j * 30, i * 30))
                if not bottomEmpty and not leftEmpty and isEmpty(i + 1, j - 1):
                    surf.blit(self.borderimg[37], (j * 30, i * 30))

    def loadEntities(self) -> list[Entity]:
        raw: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = getEntityDat(self.lvlId)
        listEntities: list[Entity] = []
        for entity in raw:
            match entity:
                case (id, x, y, state):
                    e = Character(id, x, y, state, self.lvlId, self.blocks)
                case (id, x, y, state, movementStr):
                    e = MovingEntity(id, x, y, state, movementStr)
            
            listEntities.append(e)
        return listEntities

    def loadBlocks(self) -> list[list[Block]]:
        blocks: list[list[Block]] = []
        for _ in range(getLevelHeight(self.lvlId)):
            blocks.append([Block(0, 0, 0, name=".")] * getLevelWidth(self.lvlId))
        l = getLevelBlocks(self.lvlId)
        for i in range(getLevelHeight(self.lvlId)):
            if getLevelBlockMode(self.lvlId) == "L":
                for j in range(getLevelWidth(self.lvlId)):
                    x = j*30
                    y = i*30

                    blocks[i][j] = Block(level=self.lvlId, name=l[i][j], x=x, y=y)
            else:
                for j in range(getLevelWidth(self.lvlId)):
                    x = j*30
                    y = i*30

                    blocks[i][j] = Block(level=self.lvlId, name=f"{l[i][j*2]}{l[i][j*2+1]}", x=x, y=y)
        return blocks

    def __init__(self, lvlId: int) -> None:
        self.lvlId = lvlId
        self.blocks = self.loadBlocks()
        self.entities = self.loadEntities()
        self.staticBlockSurf = pygame.Surface((getLevelWidth(lvlId)*30, getLevelHeight(lvlId)*30), pygame.SRCALPHA)
        self.drawStaticBlocks(self.staticBlockSurf)
        self.drawBorders(self.staticBlockSurf)
        self.cameraX = 0 # TODO: Implement camera
        self.cameraY = 0 # TODO: Implement camera
        self.bgSurf = pygame.transform.scale(pygame.image.load(f"visuals/bg/bg{getLevelBgId(lvlId):04d}.png"), (960, 540)).convert()
        self.textSurf = pygame.font.Font("fonts/helveticabold.ttf", 32).render(f"{lvlId+1:03d}. {getLevelName(lvlId)}", True, (255, 255, 255)).convert_alpha()

    def drawBg(self, surf: pygame.Surface) -> None:
        surf.blit(self.bgSurf, (0, 0))

    def drawBlocks(self, surf: pygame.Surface) -> None:
        surf.blit(self.staticBlockSurf, (self.cameraX, self.cameraY))
        for _ in self.blocks:
            for tile in _:
                if tile:
                    if tile.info[16] > 1 or tile.id == 6:
                        tile.draw(surf)



    def drawEntities(self, surf: pygame.Surface) -> None:
        for entity in self.entities:
            entity.draw(surf)

    def drawLevelText(self, surf: pygame.Surface) -> None:
        surf.blit(self.textSurf, (12.85, 495.45))
    
    def draw(self, screen: pygame.Surface) -> None:
        self.drawBg(screen)
        self.drawBlocks(screen)
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
