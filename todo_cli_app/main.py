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
        if cmd[1] == "--help":
            Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")
        elif cmd[1] == "init" or ".":
            Initialize.initialize()
        elif cmd[1] == "delete":
            Delete.delete()
        elif cmd[1] == "read":
            Read.read()
        elif cmd[1] == "add":
            Help._help("blob/main/Docs/User%20Manual.md")
        elif cmd[1] == "edit":
            Help._help("blob/main/Docs/User%20Manual.md")
        elif cmd[1] == "rm":
            Help._help("blob/main/Docs/User%20Manual.md")
        else:
            print("[!] - Command not found!")
            Help._help("blob/main/Docs/User%20Manual.md#-------user-manual")




if __name__ == "__main__":

    cli()