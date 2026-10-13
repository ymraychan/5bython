from typing import TypedDict, Final


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

type _BlockProperties1 = tuple[
    bool,
    bool,
    bool,
    bool,
    bool,
	bool,
	bool,
	bool,
    bool,
	bool,
	bool,
    int,
    int,
    bool,
    bool,
    bool,
    int,
    bool
]

type _BlockProperties2 = tuple[
    *_BlockProperties1,
    tuple[int, ...]
]

type BlockPropertiesRow = _BlockProperties1 | _BlockProperties2

type BlockProperties = list[_BlockProperties1 | _BlockProperties2]