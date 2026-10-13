import re

with open("data/levels.txt", encoding="utf-8") as f:
    level_string = f.read()

def get_level(level: int) -> str:
    """ Get the entire string of the level in question """
    return level_string.split("\n\n")[level]

def get_level_name(level: int) -> str:
    """ Get the name of the level """
    return get_level(level).split("\n")[0]

def get_level_metadata(level: int) -> str:
    """ Get the entire metadata of the level """
    return get_level(level).split("\n")[1]

def get_level_width(level: int) -> int:
    """ Get the width of the level """
    return int(get_level_metadata(level)[0:2])

def get_level_height(level: int) -> int:
    """ Get the height of the level """
    return int(get_level_metadata(level)[3:5])

def get_level_num_entities(level: int) -> int:
    """ Get the number of entities in the level """
    return int(get_level_metadata(level)[6:8])

def get_level_bg_id(level: int) -> int:
    """ Get the background id of the level """
    return int(get_level_metadata(level)[9:11])

def get_level_block_mode(level: int) -> str:
    """ Get the block mode of the level. L means one char per block, H means two """
    return get_level_metadata(level)[12]

def get_level_blocks(level: int) -> list[str]:
    """ Get the list of blocks of the level """
    return get_level(level).split("\n")[2:2+get_level_height(level)]

def get_level_blocks_as_str(level: int) -> str:
    """ Return level blocks as a string instead of a list """
    v: str = ""
    for _ in get_level_blocks(level):
        v += _
        v += "\n"
    return v

def get_char_at(level: int, x_pos: int, y_pos: int) -> str:
    """ Get the character at (x_pos, y_pos), (0, 0) is top left corner """
    if get_level_block_mode(level) == "L":
        return get_level_blocks(level)[y_pos][x_pos]
    else:
        return get_level_blocks(level)[y_pos][2*x_pos:2*x_pos+2]

def char_to_code(char: str) -> int:
    """ Convert the character to a unique code """
    n: int = 0
    if len(char) == 1:
        n = ord(char)
        if n == 8364: return 93
        if n <= 126: return n - 46
        if n <= 182: return n - 80
        return n - 81
    else:
        if char[0] == ".":
            n = ord(char[1])
            if n == 8364: return 93
            if n <= 126: return n - 46
            if n <= 182: return n - 80
            return n - 81
        else:
            if char[1] == ".": return 110
            else: return ord(char[1]) + 65

def get_entity_dat(level: int) -> list[tuple[int, float, float, int] | tuple[int, float, float, int, str]]:
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
    entity_list: list[str] = get_level(level).split("\n")[2+get_level_height(level):2+get_level_height(level)+get_level_num_entities(level)]
    for _ in entity_list:
        parts = re.split(r",| ", _)
        if len(parts) > 4:
            val.append((int(parts[0]), float(parts[1]), float(parts[2]), int(parts[3]), str(parts[4])))
        else:
            val.append((int(parts[0]), float(parts[1]), float(parts[2]), int(parts[3])))

    return val

def get_level_char_count(level: int):
    entities = get_entity_dat(level)
    count = 0
    for entity in entities:
        if entity[3] == 9 or entity[3] == 10:
            count += 1

    return count

def get_num_lines_dialouge(level: int) -> int:
    return int(get_level(level).split("\n")[2+get_level_height(level)+get_level_num_entities(level)])

def get_dialouge(level: int) -> list[tuple[int, str, str]]:
    return []

def get_necessary_deaths(level: int) -> int:
    return int(get_level(level).split("\n")[2+get_level_height(level)+get_level_num_entities(level)+get_num_lines_dialouge(level)+1])