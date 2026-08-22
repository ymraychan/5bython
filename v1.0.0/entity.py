import pygame
from scipy import ndimage
import numpy as np
from typing import Final
import properties
import sys

class Entity:
    id: int
    x: float
    y: float
    state: int
    movementStr: str
    path: str
    surf: pygame.Surface
    scaleFactor: Final[int] = 3
    mat: tuple[float, float, float, float]
    tx: float
    ty: float
    vx: float
    vy: float
    collide: tuple[bool, bool, bool, bool] # hit ceiling, hit ground, hit left wall, hit right wall
    properties: Final[list]
    charModel: Final[dict]
    rect: pygame.FRect
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
        self.id = id
        self.x = x
        self.y = y
        self.state = state
        self.movementStr = movementStr
        self.path = f"images/entities/e{id:04d}.png"
        self.charModel = properties.charModels[self.id]
        surf = pygame.image.load(self.path).convert_alpha()
        self.vx = 0
        self.vy = 0
        self.collide = (False, False, False, False)
        self.properties = properties.charD[self.id]
        if id > 34:
            if self.properties[7] == 1:
                # draw static image
                self.surf = surf
            else:
                # draw anim image
                pass
        else:
            try:
                surf = self.transformMat(surf, *self.charModel["torsomat"].values())
                self.mat = tuple(list(self.charModel["torsomat"].values())[:4])
                self.tx, self.ty = list(self.charModel["torsomat"].values())[4:6]
                surf = pygame.transform.scale(surf, (surf.get_width()//self.scaleFactor, surf.get_height()//self.scaleFactor))
                self.surf = surf
            except:
                self.surf = surf
                print(f"No torsomat for id: {id}", sys.stderr)
        self.rect = pygame.FRect(0, 0, 0, 0) # TODO: Implement FRect

    def draw(self, screen: pygame.Surface) -> None:
        if self.surf is not None:
            rect = self.surf.get_rect()
            rect.midbottom=(int(self.x * 30), int(self.y * 30))
            screen.blit(self.surf, rect)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        # TODO: update 
        pass


