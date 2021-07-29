import os

with open("/opt/file.txt", "w") as f:
    f.write(os.path.abspath(os.curdir))
