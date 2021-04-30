import todo_cli_app
from .commands.file.file_io import Path
from .commands.help import Help


import argparse
import sys

def cli():
    command = sys.argv[1]

    if command == "--help":
        Help._help("blob/main/Docs/help.md#-------help")
    elif command == "init":
        pass
    elif command == "delete":
        pass
    elif command == "open":
        pass



if __name__ == "__main__":

    cli()