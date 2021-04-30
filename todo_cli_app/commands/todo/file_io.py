import os

class File:

    def write(name:str, ext:str, path:str, encripted:bytes):
        """saves a file in path
        """
        with open(r"{0}/{1}.{2}".format(path, name, ext), "wb") as encripted_file:
            encripted_file.write(encripted)

class _Path:
    def get_path() -> str:
        """Gets current script path
        """
        here = os.path.abspath(__file__)
        here = here.split("\\")
        root_path:list = here[:-6]
        root_p:str = "/".join(root_path) + "/"
        return root_p

    def get_terminal_path() -> str:
        """Gets the current terminal path
        """
        term_p = os.getcwd()
        return term_p

if __name__ == "__main__":

    print(_Path.get_path())