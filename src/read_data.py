import json
import os
from typing import Final

from platformdirs import PlatformDirs

from types_5b import SaveData

save_folder: Final[PlatformDirs] = PlatformDirs("5bython", "Ilovebfdi314", version="v1.0.0")

save_file_path: Final[str] = os.path.join(save_folder.user_data_dir, "data.json")
user_dat_path: Final[str] = os.path.join(save_folder.user_data_dir, "userdat.json")

def create_save_data() -> None:
    # print(save_file_path)
    os.makedirs(save_folder.user_data_dir, mode=0o755, exist_ok=True)
    if not os.path.exists(save_file_path):
        with open(save_file_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "lvl_progress": 0,
                    "win_token": [],
                    "deaths": 0,
                    "time": 0,
                }
            , f, indent=4)

def read_save_data() -> SaveData:
    if not os.path.exists(save_file_path):
        create_save_data()
    with open(save_file_path, "r", encoding="utf-8") as f:
        return json.load(f) 

def write_save_data(data: SaveData) -> None:
    with open(save_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)