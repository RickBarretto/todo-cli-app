from .file.file_io import *
import os
import sys

class Initialize:

    def initialize():
        print("init")
        termp = Path.get_terminal_path()
        print("Todo created in:", termp)

        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            print("[!] - File was already created!")
        else:
            _Generic.create(termp)

class _Generic:

    def create(termp:str):
        f = open(f"{termp}\\.todo", "x")
        f.write("")
        f.close()