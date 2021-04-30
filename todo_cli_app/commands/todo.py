from .file.file_io import *
import os

class Init:

    def init():

        termp = Path.get_terminal_path()
        print("Todo created in:", termp)

        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            print("[!] - File was already created!")
        else:
            _Generic.create(termp)

    def delete():
        termp = Path.get_terminal_path()
        todo = termp + "\\.todo"
        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            os.remove(todo)
            print("[!] - Todo deleted!")
        else:
            print("[!] - File not found!")



class _Generic:

    def create(termp:str):
        name = termp.split("/")[-1]
        f = open(f"{termp}/.todo", "rb")
        f.read()
        f.close()