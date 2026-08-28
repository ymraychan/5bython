from getLevels import getEntityDat, getDialouge
from entity.entity import Entity
from entity.movingEntity import MovingEntity
from entity.character import Character
def loadEntities(level: int) -> list[Entity]:
    raw: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = getEntityDat(level)
    listEntities: list[Entity] = []
    for entity in raw:
        match entity:
            case (id, x, y, state):
                e = Character(id, x, y, state, level)
            case (id, x, y, state, movementStr):
                e = MovingEntity(id, x, y, state, movementStr)
        
        listEntities.append(e)
    return listEntities