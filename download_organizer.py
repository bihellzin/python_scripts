#!/usr/bin/env python3

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


def get_downloads_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        try:
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        except:
            print('error')
    else:
        try:
            download_path = os.path.join(os.path.expanduser('~'), 'downloads')
            os.chdir(download_path)
        except FileNotFoundError:
            download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        finally:
            return download_path


if __name__ == "__main__":
    try:
        download_path = get_downloads_path()
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

        print('Finished')

    except:
        print("An error occurred")