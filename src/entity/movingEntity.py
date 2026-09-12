import pygame
from entity.entity import Entity

class MovingEntity(Entity):
    movementStr: str
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
            hitbox = self.surf.get_rect()
            hitbox.midbottom=(int(self.pos.x * 30) + self.tx, int(self.pos.y * 30) + self.ty)
            screen.blit(self.surf, hitbox)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.__time += 1
        self.updateSurf()
        self.updatePos()

    def updateSurf(self) -> None:
        if self.id > 34 and self.properties[7] > 1:
            self.__frame += 1
            self.__frame %= int(self.properties[7])
            self.path = f"images/entities/e{self.id:04d}f{self.__frame:04d}.png"
            self.surf = self.__surfs[self.__frame]
    def updateVelocity(self) -> None:
        self.velocity.update(self.nullVector)
        string = self.movementStr[2:]
        rspeed = int(self.movementStr[:2])
        if self.__time >= len(string) * rspeed:
            self.__time = 0
        speed = 1 / rspeed
        pos = int(string[(self.__time // (rspeed)) % len(string)])
        if pos == 0:
            self.velocity.y = speed * -1
        if pos == 1:
            self.velocity.y = speed
        if pos == 2:
            self.velocity.x = speed * -1
        if pos == 3:
            self.velocity.x = speed
    def updatePos(self) -> None:
        self.updateVelocity()
        self.pos += self.velocity
        self.hitbox.x += self.velocity.x * 30
        self.hitbox.y += self.velocity.y * 30