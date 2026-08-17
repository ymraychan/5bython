import block
import getLevels
from typing import Optional

def loadLevels(level: int) -> list[list[block.Block]]:
    blocks: list[list[block.Block]] = []
    for _ in range(getLevels.getLevelHeight(level)):
        blocks.append([block.Block(0, 0, 0, name=".")] * getLevels.getLevelWidth(level))
    l = getLevels.getLevelBlocks(level)
    for i in range(getLevels.getLevelHeight(level)):
        if getLevels.getLevelBlockMode(level) == "L":
            for j in range(getLevels.getLevelWidth(level)):
                x = j*30
                y = i*30

                blocks[i][j] = block.Block(level=level, name=l[i][j], x=x, y=y)
        else:
            for j in range(getLevels.getLevelWidth(level)):
                x = j*30
                y = i*30

                blocks[i][j] = block.Block(level=level, name=f"{l[i][j*2]}{l[i][j*2+1]}", x=x, y=y)
    return blocks
