#!/usr/bin/env python3.6

import os

from os import listdir
from os.path import isfile, join
from pathlib import Path

def get_directories(directory_path: str) -> dict:
    dirs = {}
    for item in listdir(directory_path):
        if not isfile(join(download_path, f)):
            dirs[item] = True

    return dirs

if __name__ == "__main__":
    home = str(Path.home())
    os.chdir('{0}/Downloads'.format(home))
    download_path = os.getcwd()

    for f in listdir(download_path):
        if isfile(join(download_path, f)):
            pass