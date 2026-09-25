import json
import os
from platformdirs import PlatformDirs

from typing import Final
from types5b import SaveData

saveFolder: Final[PlatformDirs] = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")

saveFilePath: Final[str] = os.path.join(saveFolder.user_data_dir, "data.json")
userdatPath: Final[str] = os.path.join(saveFolder.user_data_dir, "userdat.json")

def createSaveData() -> None:
    print(saveFilePath)
    os.makedirs(saveFolder.user_data_dir, mode=0o755, exist_ok=True)
    if not os.path.exists(saveFilePath):
        with open(saveFilePath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "lvlProgress": 0,
                    "winToken": [],
                    "deaths": 0,
                    "time": 0,
                }
            , f, indent=4)

def readSaveData() -> SaveData:
    if not os.path.exists(saveFilePath):
        createSaveData()
    with open(saveFilePath, "r", encoding="utf-8") as f:
        return json.load(f) 

def writeSaveData(data: SaveData) -> None:
    with open(saveFilePath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)