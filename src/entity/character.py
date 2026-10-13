from math import sqrt
from typing import Final, Literal

import pygame

from block import Block
from entity.entity import Entity
from types_5b import AffineMat

jump_power: Final = 11
power: Final = 1

class Character(Entity):
    on_object: bool
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
        self.on_object = False
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


    def draw_legs(self, surf: pygame.Surface) -> None:
        # if (self.id != 5): # TODO: Add the bubble dying clause
        self.leg_direction = 1 if self.leg_direction > 0 else -1

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox.move(self.tx,self.ty))
        super().draw_hitbox(screen)

    def update_position(self) -> None:
        self.x += self.vx
        self.y += self.vy
        super().update_rect()

    def apply_forces(self) -> None:
        if not self.on_object:
            self.vy = min(self.vy + self.gravity, 25)
        if self.on_object:
            self.vx = (self.vx - self.fric_goal) * self.friction + self.fric_goal
        else:
            self.vx *= 1 - (1 - self.friction) * (0.12)
        
        if abs(self.vx) < 0.01: self.vx = 0
        # TODO: WATER/FLUIDS

    def collision_check(self) -> None:
        self.on_object = False
        for _ in self.blocks:
            for block in _:
                # TODO: Fix left/right collisions
                """if block.info[2] and self.hitbox.colliderect(block.rect):
                    self.vx = 0
                if block.info[3] and self.hitbox.colliderect(block.rect) and \
                    self.hitbox.right > block.rect.left:
                    self.vx = 0"""
                if block.info[1] and self.hitbox.colliderect(block.rect):
                    self.on_object = True
                    self.vy = 0
                    self.hitbox.bottom = block.rect.top
                elif block.info[0] and self.hitbox.colliderect(block.rect) and self.vy > 0:
                    self.vy *= -1
                
        

    def jump(self, jump_power: int) -> None:
        if self.on_object:
            self.vy = jump_power
            self.on_object = False

    def check_keys(self, screen: pygame.Surface, keys_pressed: pygame.key.ScancodeWrapper, keys_instant: list[pygame.event.Event]) -> None:
        for k in keys_instant:
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
        if keys_pressed[pygame.K_LEFT]:
            self.move_horizontal(-power)
        if keys_pressed[pygame.K_RIGHT]:
            self.move_horizontal(power)
        # No key presses after this line

    def move_horizontal(self, power: int) -> None:
        if not self.on_object and ((power * self.fric_goal)<= 0):
            self.fric_goal = 0
        
        self.vx += power


    def update(self, screen: pygame.Surface, keys_pressed: pygame.key.ScancodeWrapper, keys_instant: list[pygame.event.Event]) -> None:
        self.check_keys(screen, keys_pressed, keys_instant)
        self.apply_forces()
        self.update_position()
        self.collision_check()
        # TODO: other event stuff

    def die(self) -> None:
        pass