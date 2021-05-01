import todo_cli_app
from .commands.file.file_io import Path
from .commands.help import Help
from .commands.create import Initialize
from .commands.delete import Delete
from .commands.read import Read


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
        elif command == "init" or ".":
            Initialize.initialize()
        elif command == "delete":
            Delete.delete()
        elif command == "read":
            Read.read()
        elif command == "add":
            Help._help("blob/main/Docs/User%20Manual.md")
        elif command == "edit":
            Help._help("blob/main/Docs/User%20Manual.md")
        elif command == "rm":
            Help._help("blob/main/Docs/User%20Manual.md")
        else:
            print("[!] - Command not found!")
            Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")

    if len(cmd) == 3:
        command = cmd[1]
        option = cmd[2]




if __name__ == "__main__":

    cli()