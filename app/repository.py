import os


class IdsRepository:
    def __init__(self, path: str):
        self.path = path

    def read_id(self) -> str or None:
        if not os.path.exists(self.path):
            return None

        with open(self.path, "r") as file:
            line = file.readline()
            file.close()
        return line

    def save_id(self, id: int):
        with open(self.path, "w+") as file:
            file.seek(0)
            file.write(f"{id}")
            file.close()
