
class IdGenerator:

    def next(self) -> int:
        value = self.i
        self.i += 1
        return value

    def __init__(self):
        self.i: int = 0
