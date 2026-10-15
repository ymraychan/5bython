from typing import TypedDict, Any, Never

type BlankDict = dict[Never, Never]


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

type BlockProperties = list[BlockPropertiesRow]

type CharPropertiesRow = tuple[
    float,
    float,
    float,
    int,
    float,
    bool,
    float,
    int,
    bool,
    int
]

type CharProperties = list[CharPropertiesRow]

type _CharModelCharacterFrame = list[dict[str, Any]]

class _CharModelCharacter(TypedDict):
    torsomat: AffineMat
    legx: list[float]
    legy: list[float]
    firemat: AffineMat
    charimgmat: AffineMat
    burstmat: AffineMat
    defaultExpr: int
    mouthType: int
    frames: list[_CharModelCharacterFrame]

class _CharModelObjects1(TypedDict):
    burstmat: AffineMat
    charimgmat: AffineMat

class _CharModelObjects2(TypedDict):
    firemat: AffineMat
    burstmat: AffineMat
    charimgmat: AffineMat

type CharModelRow = _CharModelCharacter | _CharModelObjects1 | _CharModelObjects2 | BlankDict

type CharModel = list[CharModelRow]

