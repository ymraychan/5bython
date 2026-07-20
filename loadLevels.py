import block
import getLevels
from typing import Optional

def loadLevels(level: int) -> list[list[Optional[block.Block]]]:
    blocks: list[list[Optional[block.Block]]] = []
    for _ in range(getLevels.getLevelHeight(level)):
        blocks.append([None] * getLevels.getLevelWidth(level))
    l = getLevels.getLevelBlocks(level)
    for i in range(getLevels.getLevelHeight(level)):
        if getLevels.getLevelBlockMode(level) == "L":
            for j in range(getLevels.getLevelWidth(level)):
                x = j*30
                y = i*30

                blocks[i][j] = block.Block(level=level, name=l[i][j], x=x, y=y)
        else:
            for j in range(0,getLevels.getLevelWidth(level), 2):
                x = j*15
                y = i*30

                blocks[i][j] = block.Block(level=level, name=f"{l[i][j]}{l[i][j+1]}", x=x, y=y)
    return blocks
            
loadLevels(0)
