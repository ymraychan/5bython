import pygame
from scipy import ndimage
import numpy as np
from typing import Final
import properties
import sys

class Entity:
    id: int
    pos: pygame.Vector2
    state: int
    path: str
    surf: pygame.Surface
    scaleFactor: Final[int] = 3
    mat: tuple[float, float, float, float]
    tx: float
    ty: float
    velocity: pygame.Vector2
    properties: Final[list[int | float | bool]]
    charModel: Final[dict]
    hitbox: pygame.FRect
    nullVector: Final[pygame.Vector2] = pygame.Vector2(0.0, 0.0)
    @staticmethod
    def transformMat(surf: pygame.Surface, a: float, b: float, c: float, d: float, tx: float, ty: float) -> pygame.Surface:
        surfArr = pygame.surfarray.array3d(surf)
        alphaArr = pygame.surfarray.array_alpha(surf)
        mat2d = np.linalg.inv([[a, c], [b, d]])
        matrix = np.eye(3)
        matrix[:2, :2] = mat2d
        surfTransformed = ndimage.affine_transform(surfArr, matrix, order=1)
        alphaTransformed = ndimage.affine_transform(alphaArr, mat2d, order=1)
        outSurf = pygame.Surface(surfTransformed.shape[:2], flags=pygame.SRCALPHA)
        pygame.surfarray.blit_array(outSurf, surfTransformed)
        pygame.surfarray.pixels_alpha(outSurf)[:] = alphaTransformed
        return outSurf
    
    def __init__(self, id: int, x: float, y: float, state: int) -> None:
        self.id = id
        self.pos = pygame.Vector2(x, y)
        self.state = state
        self.__frame = 0
        self.properties = properties.charD[self.id]
        self.path = f"visuals/entities/e{id:04d}.png" if self.properties[7] == 1 else f"visuals/entities/e{id:04d}f{self.__frame:04d}.png"
        self.charModel = properties.charModels[self.id]
        surf = pygame.image.load(self.path).convert_alpha()
        self.velocity = self.nullVector
        self.__surfs = []
        if id > 34:
            self.surf = surf
            if self.properties[7] > 1:
                for i in range(int(self.properties[7])):
                    self.__surfs.append(pygame.image.load(f"images/entities/e{id:04d}f{self.__frame:04d}.png").convert_alpha())
                    self.__frame += 1
                self.__frame = 0
            self.tx = self.ty = 0.0
        else:
            surf = self.transformMat(surf, *self.charModel["torsomat"].values())
            self.mat = tuple(list(self.charModel["torsomat"].values())[:4])
            self.tx, self.ty = list(self.charModel["torsomat"].values())[4:6]
            surf = pygame.transform.scale(surf, (surf.get_width()//self.scaleFactor, surf.get_height()//self.scaleFactor))
            self.surf = surf
        self.hitbox = self.surf.get_frect()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox)

    def drawHitbox(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, width=2)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.updateRect()

    def updateRect(self) -> None:
        self.hitbox.midbottom = (int(self.pos.x * 30) + self.tx, int(self.pos.y * 30) + self.ty)