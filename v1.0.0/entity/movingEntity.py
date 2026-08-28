import pygame
from entity.entity import Entity

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
    rect: pygame.FRect
    __frame: int
    __surfs: list[pygame.Surface]
    __time: int
    def __init__(self, id: int, x: float, y: float, state: int, movementStr: str) -> None:
        super().__init__(id, x, y, state)
        self.movementStr = movementStr
        self.__frame = 0
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
    def updateVelocity(self) -> None:
        self.vx = self.vy = 0
        string = self.movementStr[2:]
        rspeed = int(self.movementStr[:2])
        if self.__time >= len(string) * rspeed:
            self.__time = 0
        speed = 1 / rspeed
        pos = int(string[(self.__time // (rspeed)) % len(string)])
        if pos == 0:
            self.vy = speed * -1
        if pos == 1:
            self.vy = speed
        if pos == 2:
            self.vx = speed * -1
        if pos == 3:
            self.vx = speed
    def updatePos(self) -> None:
        self.updateVelocity()
        self.x += self.vx
        self.y += self.vy
        self.rect.x += self.vx * 30
        self.rect.y += self.vy * 30