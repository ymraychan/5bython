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
    elif getLevelBlockMode(level) == "H":
        if char[0] == ".":
            n: int = ord(char[1])
            if n == 8364: return 93
            if n <= 126: return n - 46
            if n <= 182: return n - 80
            return n - 81
        else:
            if char[1] == ".": return 110
            else: return ord(char[1]) + 65

    return -1
