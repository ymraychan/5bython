from typing import Any
import re

levelString = open("data/levels.txt", encoding="utf-8").read()

def getLevel(level: int) -> str:
    """ Get the entire string of the level in question """
    return levelString.split("\n\n")[level]

def getLevelName(level: int) -> str:
    """ Get the name of the level """
    return getLevel(level).split("\n")[0]

def getLevelMetadata(level: int) -> str:
    """ Get the entire metadata of the level """
    return getLevel(level).split("\n")[1]

def getLevelWidth(level: int) -> int:
    """ Get the width of the level """
    return int(getLevelMetadata(level)[0:2])

def getLevelHeight(level: int) -> int:
    """ Get the height of the level """
    return int(getLevelMetadata(level)[3:5])

def getLevelNumEntities(level: int) -> int:
    """ Get the number of entities in the level """
    return int(getLevelMetadata(level)[6:8])

def getLevelBgId(level: int) -> int:
    """ Get the background id of the level """
    return int(getLevelMetadata(level)[9:11])

def getLevelBlockMode(level: int) -> str:
    """ Get the block mode of the level. L means one char per block, H means two """
    return getLevelMetadata(level)[12]

def getLevelBlocks(level: int) -> list[str]:
    """ Get the list of blocks of the level """
    return getLevel(level).split("\n")[2:2+getLevelHeight(level)]

def getLevelBlocksAsStr(level: int) -> str:
    """ Return level blocks as a string instead of a list """
    v: str = ""
    for _ in getLevelBlocks(level):
        v += _
        v += "\n"
    return v

def getCharAt(level: int, x_pos: int, y_pos: int) -> str:
    """ Get the character at (x_pos, y_pos), (0, 0) is top left corner """
    if getLevelBlockMode(level) == "L":
        return getLevelBlocks(level)[y_pos][x_pos]
    else:
        return getLevelBlocks(level)[y_pos][2*x_pos:2*x_pos+2]

def charToCode(level: int, char: str) -> int:
    """ Convert the character to a unique code """
    if getLevelBlockMode(level) == "L":
        n: int = ord(char)
        if n == 8364: return 93
        if n <= 126: return n - 46
        if n <= 182: return n - 80
        return n - 81
    else:
        if char[0] == ".":
            n: int = ord(char[1])
            if n == 8364: return 93
            if n <= 126: return n - 46
            if n <= 182: return n - 80
            return n - 81
        else:
            if char[1] == ".": return 110
            else: return ord(char[1]) + 65

def getEntityDat(level: int) -> list[tuple[int, float, float, int] | tuple[int, float, float, int, str]]:
    """ Returns a list of the entity data in the given level
        Args:
            level (int): the level
        Returns:
            list of tuples
            - Tuple pos 1 (int): Entity ID
            - Tuple pos 2 (int): Entity x pos
            - Tuple pos 3 (int): Entity y pos
            - Tuple pos 4 (int): Entity state
            - Tuple pos 5 (optional) (str): Movement string"""
    val: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = []
    entityList: list[str] = getLevel(level).split("\n")[2+getLevelHeight(level):2+getLevelHeight(level)+getLevelNumEntities(level)]
    for _ in entityList:
        parts = re.split(r",| ", _)
        if len(parts) > 4:
            val.append((int(parts[0]), float(parts[1]), float(parts[2]), int(parts[3]), str(parts[4])))
        else:
            val.append((int(parts[0]), float(parts[1]), float(parts[2]), int(parts[3])))

    return val

def getNumLinesDialouge(level: int) -> int:
    return int(getLevel(level).split("\n")[2+getLevelHeight(level)+getLevelNumEntities(level)])

def getDialouge(level: int) -> list[tuple[int, str, str]]:
    ...