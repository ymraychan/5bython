from typing import Final, Any, Optional

from pgzero.actor import Actor
from pgzero.rect import Rect
from getLevels import charToCode
import properties
class Block:
    blockProperties: Final[list[list[Any]]] = properties.blockProperties
    id: Final[int]
    path: str
    info: Final[list[Any]]
    frame: int = 0
    frameCount: int
    actor: Actor
    bottomleft: tuple[int, int]
    x: Final[int]
    y: Final[int]
    doorLightX: Final[list[list[int]]] = properties.doorLightX
    level: int
    
    def returnPath(self) -> str:
        p: str = ""
        if self.blockProperties[self.id][16] > 1:
            p = f"blocks/b{self.id:04d}f{self.frame:04d}"
        else:
            p = f"blocks/b{self.id:04d}"
        return p

    def addFrame(self) -> None:
        self.frame += 1
        self.frame %= self.frameCount
        self.path = self.returnPath()
    
    def __init__(self, x: int, y: int, level: int, block_id: Optional[int]=None, name: Optional[str]=None, frame: Optional[int]=0) -> None:
        if block_id is None:
            self.id = charToCode(level, name)
        else:
            self.id = block_id
            
        self.frame = frame
        self.frameCount = self.blockProperties[self.id][16]
        self.path = self.returnPath()
        self.info = self.blockProperties[self.id]
        self.actor = Actor(self.path, anchor=('left', 'bottom'))
        self.actor.bottomleft = (x, y+30)
        self.x = x
        self.y = y
        self.level = level

    def draw(self, screen) -> None:
        if self.id == 6: self.drawDoor(screen)
        else:
            self.actor.image = self.path
            if self.info[16] > 0: self.actor.draw()

    def drawDoor(self, screen) -> None:
        door=Rect((self.x-30), (self.y-90), 60, 120)
        screen.draw.filled_rect(door, (80, 80, 80))
