import pygame
from entity.entity import Entity
from math import sqrt
from block import Block
from typing import Literal, Final
from types5b import AffineMat

class Character(Entity):
    onObject: bool
    hitbox: pygame.FRect
    blocks: list[list[Block]]
    legDirection: Literal[-1, 1]
    legMat: list[AffineMat]
    fricGoal: float # TODO: Look into what fricGoal means
    weight: Final[float]
    gravity: Final[float]
    friction: Final[float]
    jumpPower: Final[int] = 11
    power: Final[int] = 1

    def __init__(self, id: int, x: float, y: float, state: int, level: int, blocks: list[list[Block]]) -> None:
        super().__init__(id, x, y, state)
        self.level = level
        self.onObject = False
        self.blocks = blocks
        self.legDirection = 1
        self.legMat = [ { "a": 0.3648529052734375, "b": 0, "c": 0, "d": 0.3814697265625, "tx": -0.75 if self.legDirection > 0 else 0.35, "ty": -0.35 },
						{
							"a": 0.3648529052734375, 
							"b": 0, 
							"c": 0,
							"d": 0.3814697265625, 
							"tx": -0.75 if self.legDirection > 0 else 0.35, 
							"ty": -0.35 } ]
        self.weight = self.properties[2]
        self.gravity = sqrt(self.weight)
        self.friction = self.properties[4]
        self.fricGoal = 0


    def drawLegs(self, surf: pygame.Surface) -> None:
        # if (self.id != 5): # TODO: Add the bubble dying clause
        self.legDirection = 1 if self.legDirection > 0 else -1

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox.move(self.tx,self.ty))
        super().drawHitbox(screen)

    def updatePosition(self) -> None:
        self.pos += self.velocity
        super().updateRect()

    def applyGravity(self) -> None:
        if not self.onObject:
            self.velocity.y = min(self.velocity.y + self.gravity / 30, 25 / 30)
        # TODO: WATER/FLUIDS
    
    def applyResistiveForces(self) -> None:
        if self.onObject:
            self.velocity.x = (self.velocity.x - self.fricGoal) * self.friction + self.fricGoal
        else:
            self.velocity.x *= 1 - ((1 - self.friction) * 0.12)
        if abs(self.velocity.x) < 0.01: self.velocity.x = 0

    def collisionCheck(self) -> None:
        for _ in self.blocks:
            for block in _:
                if block.info[1] and self.hitbox.colliderect(block.rect):
                    self.onObject = True
                    self.velocity.y = 0
                    self.hitbox.bottom = block.rect.top
                if block.info[0] and self.hitbox.colliderect(block.rect) and self.velocity.y > 0:
                    self.velocity.y *= -1

    def jump(self, jumpPower: int) -> None:
        if self.onObject:
            self.velocity.y = jumpPower / 30
            self.onObject = False

    def checkKeys(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        for k in keysInstant:
            if k.type == pygame.KEYDOWN:
                if k.key == pygame.K_SPACE:
                    self.jump(-self.jumpPower)
                if k.key == pygame.K_UP:
                    print("up")
                if k.key == pygame.K_DOWN:
                    print("down")
                if k.key == pygame.K_z:
                    print("z")
                if k.key == pygame.K_RETURN:
                    print("enter")
        if keysPressed[pygame.K_LEFT]:
            self.moveHorizontal(-self.power)
        if keysPressed[pygame.K_RIGHT]:
            self.moveHorizontal(self.power)
        # No key presses after this line

    def moveHorizontal(self, power: int) -> None:
        if not self.onObject and ((power * self.fricGoal) <= 0):
            self.fricGoal = 0
        self.applyResistiveForces()
        
        self.velocity.x += power / 30


    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.checkKeys(screen, keysPressed, keysInstant)
        self.updatePosition()
        self.collisionCheck()
        self.applyGravity()
        # TODO: other event stuff

    def die(self) -> None:
        pass