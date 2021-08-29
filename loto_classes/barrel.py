
class Barrel:
    def __init__(self, number):
        self._number = number

    def __repr__(self):
        return f"({self._number})"

    @property
    def number(self):
        return self._number
