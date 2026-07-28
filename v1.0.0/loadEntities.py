from getLevels import getEntityDat, getDialouge
from entity import Entity

def loadEntities(level: int) -> list[Entity]:
    raw: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = getEntityDat(level)
    listEntities: list[Entity] = []
    for entity in raw:
        match entity:
            case (id, x, y, state):
                movementStr = ""
            case (id, x, y, state, movementStr):
                pass
        e = Entity(id, x, y, state, movementStr)
        
        listEntities.append(e)
    return listEntities