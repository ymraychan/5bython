from typing import TypedDict


class SaveData(TypedDict):
    lvl_progress: int
    win_token: list[int]
    deaths: int
    time: int

class AffineMat(TypedDict):
    a: float
    b: float
    c: float
    d: float
    tx: float
    ty: float