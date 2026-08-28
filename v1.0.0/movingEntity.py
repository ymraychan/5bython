import pygame
from scipy import ndimage
import numpy as np
from typing import Final
import properties
import sys
from entity import Entity

class MovingEntity(Entity):
    id: int
    x: float
    y: float
    state: int
    movementStr: str
    path: str
    surf: pygame.Surface
    mat: tuple[float, float, float, float]
    tx: float
    ty: float
    vx: float
    vy: float
    collide: tuple[bool, bool, bool, bool] # hit ceiling, hit ground, hit left wall, hit right wall
    rect: pygame.FRect
    __frame: int
    __surfs: list[pygame.Surface]
    __time: int
    @staticmethod
    def transformMat(surf: pygame.Surface, a: float, b: float, c: float, d: float, tx: float, ty: float) -> pygame.Surface:
        surfArr = pygame.surfarray.array3d(surf)
        alphaArr = pygame.surfarray.array_alpha(surf)
        mat2d = np.linalg.inv([[a, c], [b, d]])
        matrix = np.eye(3)
        matrix[:2, :2] = mat2d
        surfTransformed = ndimage.affine_transform(surfArr, matrix, order=1) # type: ignore
        alphaTransformed = ndimage.affine_transform(alphaArr, mat2d, order=1) # type: ignore
        outSurf = pygame.Surface(surfTransformed.shape[:2], flags=pygame.SRCALPHA)
        pygame.surfarray.blit_array(outSurf, surfTransformed)
        pygame.surfarray.pixels_alpha(outSurf)[:] = alphaTransformed
        return outSurf
    def __init__(self, id: int, x: float, y: float, state: int, movementStr: str) -> None:
        super().__init__(id, x, y, state)
        self.movementStr = movementStr
        self.__frame = 0
        self.path = f"images/entities/e{id:04d}.png" if self.properties[7] == 1 else f"images/entities/e{id:04d}f{self.__frame:04d}.png"
        surf = pygame.image.load(self.path).convert_alpha()
        self.vx = 0
        self.vy = 0
        self.collide = (False, False, False, False)
        self.__surfs = []
        if id > 34:
            self.surf = surf
            if self.properties[7] > 1:
                for i in range(self.properties[7]):
                    self.__surfs.append(pygame.image.load(f"images/entities/e{id:04d}f{self.__frame:04d}.png").convert_alpha())
                    self.__frame += 1
                self.__frame = 0
            self.tx = self.ty = 0
        else:
            try:
                surf = self.transformMat(surf, *self.charModel["torsomat"].values())
                self.mat = tuple(list(self.charModel["torsomat"].values())[:4])
                self.tx, self.ty = list(self.charModel["torsomat"].values())[4:6]
                surf = pygame.transform.scale(surf, (surf.get_width()//self.scaleFactor, surf.get_height()//self.scaleFactor))
                self.surf = surf
            except:
                self.surf = surf
                self.tx = self.ty = 0
                print(f"No torsomat for id: {id}", file=sys.stderr)
        self.rect = pygame.FRect(0, 0, 0, 0) # TODO: Implement FRect
        self.__time = 0

    def draw(self, screen: pygame.Surface) -> None:
        if self.surf is not None:
            rect = self.surf.get_rect()
            rect.midbottom=(int(self.x * 30) + self.tx, int(self.y * 30) + self.ty)
            screen.blit(self.surf, rect)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.__time += 1
        self.updateSurf()
        self.updatePos()
    def updateSurf(self) -> None:
        if self.id > 34 and self.properties[7] > 1:
            self.__frame += 1
            self.__frame %= self.properties[7]
            self.path = f"images/entities/e{self.id:04d}f{self.__frame:04d}.png"
            self.surf = self.__surfs[self.__frame]
    def updatePos(self) -> None:
        string = self.movementStr[2:]
        rspeed = int(self.movementStr[:2])
        if self.__time >= len(string) * rspeed:
            self.__time = 0
        speed = 1 / rspeed
        pos = int(string[(self.__time // (rspeed)) % len(string)])
        if pos == 0:
            self.y -= speed
        if pos == 1:
            self.y += speed
        if pos == 2:
            self.x -= speed
        if pos == 3:
            self.x += speed