from os import system as Sys

class Help:

    def _help(url_path:str=""):
        repo_url = "https://github.com/RickBarretto/todo-cli-app"
        Sys(f"start {repo_url}/{url_path}")