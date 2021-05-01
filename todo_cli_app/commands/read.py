from .file.file_io import Path

class Read:

    def read():
        print("read")
        termp = Path.get_terminal_path()
        todo = termp + "\\.todo"
        check = os.path.isfile(termp + "\\.todo")
        if check == True:
            Print.sort(todo)
            Print.read(todo)
        else:
            print("[!] - File not found!\nTry: 'todo .' or 'todo init'")


class Print:

    def read(todo:str):
        pass

    def sort(todo:str):
        lines = []
        todo_content = open(todo, "rb")
        todo_content.truncate(0)
        status = ["x", "-"]
        priorities = ["@today", "@critical", "@high", "@normal", "@low"]
        for s in status:
            for priority in priorities:
                for line in todo_content:
                    if line.split(" ")[1] == priority:
                        print(line, file=todo) 