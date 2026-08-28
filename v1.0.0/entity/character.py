import pygame
from entity.entity import Entity
from math import sqrt
from block import Block
from loadLevels import loadLevels
class Character(Entity):
    id: int
    x: float
    y: float
    state: int
    path: str
    surf: pygame.Surface
    mat: tuple[float, float, float, float]
    onObject: bool
    tx: float
    ty: float
    vx: float
    vy: float
    rect: pygame.FRect
    blocks: list[list[Block]]

    @staticmethod
    def sign(n: float) -> int:
        return (n>0) - (n<0)

    def __init__(self, id: int, x: float, y: float, state: int, level: int) -> None:
        super().__init__(id, x, y, state)
        self.level = level
        self.onObject = False
        self.blocks = loadLevels(level)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.rect)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.applyGravity()
        self.updatePosition()
        self.collisionCheck()
        super().update(screen, keysPressed, keysInstant)
        # TODO: other event stuff

    def updatePosition(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.onObject = False
        super().updateRect()

    def applyGravity(self) -> None:
        weight = self.properties[2]
        gravity = sqrt(abs(weight)) * self.sign(weight)
        if not self.onObject:
            self.vy = min(self.vy + gravity, 25 / 30)
        # TODO: WATER/FLUIDS

    def collisionCheck(self) -> None:
        """for row in self.blocks:
            for block in row:
                if self.rect.colliderect(block.rect):
                    if self.vy > 0 and block.blockProperties[0]:
                        self.vy = 0
                        self.y = (self.rect.y // 30) + self.ty
                        self.rect.bottom = block.rect.top
                        self.onObject = True
                    if self.vy < 0 and block.blockProperties[1]:
                        self.vy = 0
                        self.y = (self.rect.y // 30) + self.ty
                        self.rect.top = block.rect.bottom
                    if self.vx > 0 and block.blockProperties[2]:
                        self.vx = 0
                        self.x = (self.rect.x // 30) + self.tx
                        self.rect.right = block.rect.left
                    if self.vx < 0 and block.blockProperties[3]:
                        self.vx = 0
                        self.x = (self.rect.x // 30) + self.tx
                        self.rect.left = block.rect.right"""

        pass

    def die(self) -> None:
        pass