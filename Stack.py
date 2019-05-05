class Stack:
    def __init__(self, obj):
        self.stack = [obj]

    def get_next(self):
        return self.stack.pop()

    def add(self, objs):
        for cell in objs:
            self.stack.append(cell)
