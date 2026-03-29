class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.aux.append(val)
            self.aux.append(val)
        else:
            self.stack.append(val)
            if val < self.aux[-2]:
                self.aux.append(val)
                self.aux.append(val)
            else:
                self.aux.append(self.aux[-2])
                self.aux.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.aux.pop()
        self.aux.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux[-2]
