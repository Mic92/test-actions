#!/usr/bin/env python3

import sys
from pathlib import Path
from os import getenv


def get_user_data_dir(appname: str) -> Path:
    if sys.platform == "win32":
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        )
        dir_,_ = winreg.QueryValueEx(key, "Local AppData")
        ans = Path(dir_).resolve(strict=False)
    elif sys.platform == 'darwin':
        ans = Path('~/Library/Application Support/').expanduser()
    else:
        ans = Path(getenv('XDG_DATA_HOME', "~/.local/share")).expanduser()
    return ans.joinpath(appname)


print(f"tts dir: {get_user_data_dir('tts')}")
