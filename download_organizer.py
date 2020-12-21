#!/usr/bin/env python3.6

import os

from os import listdir, replace, makedirs
from os.path import isfile, join, splitext
from pathlib import Path

def get_directories(directory_path: str) -> dict:
    dirs = {}
    for item in listdir(directory_path):
        if not isfile(join(download_path, item)):
            dirs[item] = True

    return dirs


def move_file(file_name: str, current_dir_path: str, new_dir: str):
    current_full_path = current_dir_path + '/' + file_name
    new_full_path = current_dir_path + '/' + new_dir + '/' + file_name

    replace(current_full_path, new_full_path)


if __name__ == "__main__":
    home = str(Path.home())
    os.chdir('{0}/Downloads'.format(home))
    download_path = os.getcwd()

    dirs = get_directories(download_path)

    for f in listdir(download_path):
        if isfile(join(download_path, f)):
            _, extension = splitext(f)
            extension = extension[1:]

            if extension == '':
                extension = 'no_extension'

            if not dirs.get(extension):
                makedirs(extension, exist_ok=True)

            move_file(f, download_path, extension)