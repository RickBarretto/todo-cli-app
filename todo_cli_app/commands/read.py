from .file.file_io import Path

class Read:

    def read():
        termp = Path.get_terminal_path()
        todo = termp + "\\.todo"
        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            _Print.sort(todo)
            _Print.read(todo)
        else:
            print("[!] - File not found!\nTry: 'todo .' or 'todo init'")


class _Print:

    def read(todo:str):
        pass

    def sort(todo:str):
        lines = []
        todo_content = open(todo, "rb")
        todo_content.truncate(0)
        priorities = ["@today", "@critical", "@high", "@normal", "@low"]
        for priority in priorities:
            for line in todo_content:
                if line.split(" ")[1] == priority:
                    print(line, file=todo) 