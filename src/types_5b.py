from typing import TypedDict

class SaveData(TypedDict):
    lvlProgress: int
    winToken: list[int]
    deaths: int
    time: int

class AffineMat(TypedDict):
    a: float
    b: float
    c: float
    d: float
    tx: float
    ty: float