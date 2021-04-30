import os
from .file.file_io import Path

class Delete:
    def delete():
        termp = Path.get_terminal_path()
        todo = termp + "\\.todo"
        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            os.remove(todo)
            print("[!] - Todo deleted!")
        else:
            print("[!] - File not found!")