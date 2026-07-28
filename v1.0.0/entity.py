import pygame
from scipy import ndimage
import numpy as np
from typing import Final

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
    @staticmethod
    def transformMat(surf: pygame.Surface, a: float, b: float, c: float, d: float, tx: float, ty: float) -> pygame.Surface:
        surfArr = pygame.surfarray.array3d(surf)
        alphaArr = pygame.surfarray.array_alpha(surf)
        mat2d = np.linalg.inv([[a, c], [b, d]])
        matrix = np.eye(3)
        matrix[:2, :2] = mat2d
        surfOffset = (tx, ty, 0)
        alphaOffset = (tx, ty)
        surfTransformed = ndimage.affine_transform(surfArr, matrix, offset=surfOffset, order=1) # type: ignore
        alphaTransformed = ndimage.affine_transform(alphaArr, mat2d, offset=alphaOffset, order=1) # type: ignore
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
        # self.surf = self.transformMat(pygame.image.load(self.path).convert_alpha(), 0.12158203125, -0.0020751953125, 0.0037384033203125, 0.12152099609375, 0.1, 0.4)
        # self.surf = pygame.image.load(self.path)
        surf = self.transformMat(pygame.image.load(self.path).convert_alpha(), 1, 0, 0, 1, 0, 0)
        self.mat = (1, 0, 0, 1)
        self.tx = 1.15
        self.ty = -8.95
        surf = pygame.transform.scale(surf, (surf.get_width()//self.scaleFactor, surf.get_height()//self.scaleFactor))
        self.surf = surf
        self.vx = 0
        self.vy = 0
        self.collide = (False, False, False, False)
        # TODO: Load values dynamincally

    def draw(self, screen: pygame.Surface) -> None:
        if self.surf is not None:
            screen.blit(self.surf, (self.x * 30, self.y * 30))


