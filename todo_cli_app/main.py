import todo_cli_app
from .commands.file.file_io import Path
from .commands.help import Help
from .commands.todo import *


import argparse
import sys

def cli():
    try:
        command = sys.argv[1]
    except:
        command = None
        Help._help("blob/main/Docs/help.md#-------help")

    if command == "--help":
        Help._help("blob/main/Docs/help.md#-------help")
    elif command == "init" or ".":
        Init.init()
    elif command == "delete":
        pass
    elif command == "open":
        pass
    else:
        print("[!] - Command not found!")



if __name__ == "__main__":

    cli()