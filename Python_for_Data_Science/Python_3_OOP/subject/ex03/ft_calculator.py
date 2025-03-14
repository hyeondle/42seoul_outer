class calculator:
    """Basic calculator class"""
    def __init__(self, object):
        self.object = object

    def __add__(self, object) -> None:
        self.object = [x + object for x in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        self.object = [x * object for x in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        self.object = [x - object for x in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Division by zero is not allowed")
            return
        self.object = [x / object for x in self.object]
        print(self.object)
