from pathlib import Path
from typing import List
import shutil

class Parser:
    extensions = []
    extensions.__annotations__(List[str])

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        return False

    def parse(self, path, source, dest):
        path : Path
        source : Path
        dest : Path
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)
    
    def copy(self, path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
        
