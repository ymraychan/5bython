from typing import Final

import numpy as np
import pygame
from cython import cclass
from scipy import ndimage

import properties
from types_5b import CharPropertiesRow

scale_factor: Final = 3

@cclass
class Entity:
    id: int
    x: float
    y: float
    state: int
    path: str
    mat: tuple[float, float, float, float]
    tx: float
    ty: float
    vx: float
    vy: float
    properties: Final[CharPropertiesRow]
    char_model: Final[dict]

    surf: pygame.Surface
    surfs: list[pygame.Surface]
    hitbox: pygame.FRect

    @staticmethod
    def transform_mat(surf: pygame.Surface, a: float, b: float, c: float, d: float, tx: float, ty: float) -> pygame.Surface:
        surf_arr = pygame.surfarray.array3d(surf)
        alpha_arr = pygame.surfarray.array_alpha(surf)
        mat_2d = np.linalg.inv([[a, c], [b, d]])
        matrix = np.eye(3)
        matrix[:2, :2] = mat_2d
        surf_transformed = ndimage.affine_transform(surf_arr, matrix, order=1)
        alpha_transformed = ndimage.affine_transform(alpha_arr, mat_2d, order=1)
        out_surf = pygame.Surface(surf_transformed.shape[:2], flags=pygame.SRCALPHA)
        pygame.surfarray.blit_array(out_surf, surf_transformed)
        pygame.surfarray.pixels_alpha(out_surf)[:] = alpha_transformed
        return out_surf
    
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
            surf = self.transform_mat(surf, *self.char_model["torsomat"].values())
            self.mat = tuple(list(self.char_model["torsomat"].values())[:4])
            self.tx, self.ty = list(self.char_model["torsomat"].values())[4:6]
            surf = pygame.transform.scale(surf, (surf.get_width()//scale_factor, surf.get_height()//scale_factor))
            self.surf = surf
        self.hitbox = self.surf.get_frect(midbottom=(self.x, self.y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surf, self.hitbox)

    def draw_hitbox(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox.move(self.tx, self.ty), width=2)

    def update(self, screen: pygame.Surface, keys_pressed: pygame.key.ScancodeWrapper, keys_instant: list[pygame.event.Event]) -> None:
        self.update_rect()

    def update_rect(self) -> None:
        self.hitbox.midbottom = (self.x, self.y)