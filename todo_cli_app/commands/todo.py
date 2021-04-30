from .file.file_io import *
import os

class Init:

    def init():

        termp = Path.get_terminal_path()
        rootp = Path.get_root_path()
        print("Todo created in:", termp)

        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            print("[!] - File was already created!")
        else:
            _Generic.create(termp)


class _Generic:

    def create(termp:str):
        name = termp.split("/")[-1]
        f = open(f"{termp}/.todo", "rb")
        f.read()
        f.close()

if __name__ == "__main__":
    Init.init("hello")