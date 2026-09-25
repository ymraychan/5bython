import pygame
from entity.entity import Entity
from math import sqrt
from block import Block
from typing import Literal
class Character(Entity):
    onObject: bool
    hitbox: pygame.FRect
    blocks: list[list[Block]]
    legDirection: Literal[-1, 1]
    legMat: list[dict[str, float]]
    prevPos: pygame.Vector2
    prevVel: pygame.Vector2

    @staticmethod
    def sign(n: float) -> int:
        return (n>0) - (n<0)

    def __init__(self, id: int, x: float, y: float, state: int, level: int, blocks: list[list[Block]]) -> None:
        super().__init__(id, x, y, state)
        self.level = level
        self.onObject = False
        self.blocks = blocks
        self.legDirection = 1
        self.legMat = [ { "a": 0.3648529052734375, "b": 0, "c": 0, "d": 0.3814697265625, "tx": -0.75 if self.legDirection > 0 else 0.35,  "ty": -0.35 },
						{
							"a": 0.3648529052734375, 
							"b": 0, 
							"c": 0,
							"d": 0.3814697265625, 
							"tx": -0.75 if self.legDirection > 0 else 0.35, 
							"ty": -0.35 } ]


    def drawLegs(self, surf: pygame.Surface) -> None:
        # if (self.id != 5): # TODO: Add the bubble dying clause
        self.legDirection = 1 if self.legDirection > 0 else -1

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox)
        super().drawHitbox(screen)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.applyGravity()
        self.updatePosition()
        self.collisionCheck()
        super().update(screen, keysPressed, keysInstant)
        # TODO: other event stuff

    def updatePosition(self) -> None:
        self.pos += self.velocity
        super().updateRect()
        self.preVel = self.velocity.copy()
        self.prePos = self.pos.copy()

    def applyGravity(self) -> None:
        weight: float = self.properties[2]
        gravity: float = sqrt(abs(weight)) * self.sign(weight)
        if not self.onObject:
            self.velocity.y = min(self.velocity.y + gravity, 25 / 30)
        # TODO: WATER/FLUIDS

    def collisionCheck(self) -> None:
        for _ in self.blocks:
            for block in _:
                if block.info[1] and self.hitbox.colliderect(block.rect):
                    self.onObject = True
                    self.velocity.y = 0
                    self.pos = self.prePos

    def die(self) -> None:
        pass