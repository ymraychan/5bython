import pygame
from scipy import ndimage
import numpy as np
from typing import Final, Literal
import properties

from mypy_extensions import u8

from load_images import entity_images

scale_factor: Final[Literal[3]] = 3

class Entity:
    id: int
    x: float
    y: float
    state: u8
    path: str
    surf: pygame.Surface
    surfs: list[pygame.Surface]
    mat: tuple[float, float, float, float]
    tx: float
    ty: float
    vx: float
    vy: float
    properties: Final[list[int | float | bool]]
    char_model: Final[dict]
    hitbox: pygame.FRect
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
        self.x = x
        self.y = y
        self.state = state
        self.__frame = 0
        self.properties = properties.char_d[self.id]
        self.path = f"visuals/entities/e{id:04d}.png" if self.properties[7] == 1 else f"visuals/entities/e{id:04d}f{self.__frame:04d}.png"
        self.char_model = properties.char_models[self.id]
        surf = pygame.image.load(self.path).convert_alpha()
        self.vx = self.vy = 0
        self.surfs = []
        if id > 34:
            self.surf = surf
            if self.properties[7] > 1:
                for i in range(int(self.properties[7])):
                    self.surfs.append(pygame.image.load(f"visuals/entities/e{id:04d}f{self.__frame:04d}.png").convert_alpha())
                    self.__frame += 1
                self.__frame = 0
            self.tx = self.ty = 0.0
        else:
            surf = self.transformMat(surf, *self.char_model["torsomat"].values())
            self.mat = tuple(list(self.char_model["torsomat"].values())[:4])
            self.tx, self.ty = list(self.char_model["torsomat"].values())[4:6]
            surf = pygame.transform.scale(surf, (surf.get_width()//scale_factor, surf.get_height()//scale_factor))
            self.surf = surf
        self.hitbox = self.surf.get_frect(midbottom=(self.x, self.y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox)

    def drawHitbox(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox.move(self.tx, self.ty), width=2)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.updateRect()

    def updateRect(self) -> None:
        self.hitbox.midbottom = (self.x, self.y)