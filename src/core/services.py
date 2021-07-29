import os
from pathlib import Path
import datetime
from sys import platform


def get_env_path():
    if platform == "linux" or platform == "linux2":
        env_path = os.path.join(os.path.abspath(os.path.curdir), ".env")
    else:
        env_path = Path("..") / ".env"
    return env_path
