import todo_cli_app
from .commands.file.file_io import Path
from .commands.help import Help
from .commands.create import Initialize
from .commands.delete import Delete


import argparse
import sys

def cli():
    cmd = sys.argv
    print(cmd)

    if len(cmd) == 1:
        Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")

    if len(cmd) == 2:
        command = cmd[1]
        if command == "--help":
            Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")
        elif command == "init" or command == ".":
            Initialize.initialize()
        elif command == "delete":
            Delete.delete()
        elif command == "add":
            pass
        elif command == "edit":
            pass
        elif command == "rm":
            pass
        else:
            print("[!] - Command not found!")
            Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")



if __name__ == "__main__":

    cli()