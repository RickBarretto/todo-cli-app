import todo_cli_app
from .commands.file.file_io import Path
from .commands.help import Help
from .commands.todo import *


import argparse
import sys

def cli():
    cmd = sys.argv

    if len(cmd) == 1:
        Help._help("blob/main/Docs/User%20Manual.md#-------help")

    if len(cmd) == 2:
        command = cmd[1]
        if command == "--help":
            Help._help("blob/main/Docs/User%20Manual.md#-------help")
        elif command == "init" or ".":
            Init.init()
        elif command == "add":
            pass
        elif command == "edit":
            pass
        elif command == "rm":
            pass
        elif command == "delete":
            Init.delete()
        else:
            print("[!] - Command not found!")



if __name__ == "__main__":

    cli()