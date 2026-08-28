from getLevels import getEntityDat, getDialouge
from entity import Entity
from movingEntity import MovingEntity
def loadEntities(level: int) -> list[Entity]:
    raw: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = getEntityDat(level)
    listEntities: list[Entity] = []
    for entity in raw:
        match entity:
            case (id, x, y, state):
                e = Entity(id, x, y, state)
            case (id, x, y, state, movementStr):
                e = MovingEntity(id, x, y, state, movementStr)
        
        listEntities.append(e)
    return listEntities