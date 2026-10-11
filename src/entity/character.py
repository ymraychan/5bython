import pygame
from entity.entity import Entity
from math import sqrt
from block import Block
from typing import Literal, Final
from types_5b import AffineMat

jump_power: Final[Literal[11]] = 11
power: Final[Literal[1]] = 1

class Character(Entity):
    onObject: bool
    hitbox: pygame.FRect
    blocks: list[list[Block]]
    leg_direction: Literal[-1, 1]
    leg_mat: list[AffineMat]
    fric_goal: float # TODO: Look into what fric_goal means
    weight: Final[float]
    gravity: Final[float]
    friction: Final[float]

    def __init__(self, id: int, x: float, y: float, state: int, level: int, blocks: list[list[Block]]) -> None:
        super().__init__(id, x, y, state)
        self.level = level
        self.onObject = False
        self.blocks = blocks
        self.leg_direction = 1
        self.leg_mat = [ { "a": 0.3648529052734375, "b": 0, "c": 0, "d": 0.3814697265625, "tx": -0.75 if self.leg_direction > 0 else 0.35, "ty": -0.35 },
						{
							"a": 0.3648529052734375, 
							"b": 0, 
							"c": 0,
							"d": 0.3814697265625, 
							"tx": -0.75 if self.leg_direction > 0 else 0.35, 
							"ty": -0.35 } ]
        self.weight = self.properties[2]
        self.gravity = sqrt(self.weight)
        self.friction = self.properties[4]
        self.fric_goal = 0


    def drawLegs(self, surf: pygame.Surface) -> None:
        # if (self.id != 5): # TODO: Add the bubble dying clause
        self.leg_direction = 1 if self.leg_direction > 0 else -1

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox.move(self.tx,self.ty))
        super().drawHitbox(screen)

    def updatePosition(self) -> None:
        self.x += self.vx
        self.y += self.vy
        super().updateRect()

    def applyForces(self) -> None:
        if not self.onObject:
            self.vy = min(self.vy + self.gravity, 25)
        if self.onObject:
            self.vx = (self.vx - self.fric_goal) * self.friction + self.fric_goal
        else:
            self.vx *= 1 - (1 - self.friction) * (0.12)
        
        if abs(self.vx) < 0.01: self.vx = 0
        # TODO: WATER/FLUIDS

    def collisionCheck(self) -> None:
        self.onObject = False
        for _ in self.blocks:
            for block in _:
                # TODO: Fix left/right collisions
                """if block.info[2] and self.hitbox.colliderect(block.rect):
                    self.vx = 0
                if block.info[3] and self.hitbox.colliderect(block.rect) and \
                    self.hitbox.right > block.rect.left:
                    self.vx = 0"""
                if block.info[1] and self.hitbox.colliderect(block.rect):
                    self.onObject = True
                    self.vy = 0
                    self.hitbox.bottom = block.rect.top
                elif block.info[0] and self.hitbox.colliderect(block.rect) and self.vy > 0:
                    self.vy *= -1
                
        

    def jump(self, jumpPower: int) -> None:
        if self.onObject:
            self.vy = jumpPower
            self.onObject = False

    def checkKeys(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        for k in keysInstant:
            if k.type == pygame.KEYDOWN:
                if k.key == pygame.K_SPACE:
                    self.jump(-jump_power)
                if k.key == pygame.K_UP:
                    print("up")
                if k.key == pygame.K_DOWN:
                    print("down")
                if k.key == pygame.K_z:
                    print("z")
                if k.key == pygame.K_RETURN:
                    print("enter")
        if keysPressed[pygame.K_LEFT]:
            self.moveHorizontal(-power)
        if keysPressed[pygame.K_RIGHT]:
            self.moveHorizontal(power)
        # No key presses after this line

    def moveHorizontal(self, power: int) -> None:
        if not self.onObject and ((power * self.fric_goal)<= 0):
            self.fric_goal = 0
        
        self.vx += power


    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.checkKeys(screen, keysPressed, keysInstant)
        self.applyForces()
        self.updatePosition()
        self.collisionCheck()
        # TODO: other event stuff

    def die(self) -> None:
        pass