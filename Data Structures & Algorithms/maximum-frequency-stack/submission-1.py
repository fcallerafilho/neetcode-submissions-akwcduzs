class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if val not in [i[1] for i in self.stack]:
            self.stack.append((1, val))
        else:
            cnt = 0
            for i in range(len(self.stack)):
                if self.stack[i][1] == val:
                    cnt += 1
                
            self.stack.append((cnt+1, val))

    def pop(self) -> int:
        maxFreq = max([i[0] for i in self.stack])
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == maxFreq:
                mfe = self.stack.pop(i)
                return mfe[1]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()