from pathlib import Path

class Site():
    
    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    #find the root directory
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)

    #make the destination directory
    def build(self):
        self.destination.mkdir(parents = True, exist_ok = True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

