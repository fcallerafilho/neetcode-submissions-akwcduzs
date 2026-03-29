class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack or price < self.stack[-1][0]:
            self.stack.append((price, 1))
        else:
            cnt = 1
            print(self.stack[-1][0])
            while self.stack and price >= self.stack[-1][0]:
                p, span = self.stack.pop()
                cnt += span
            self.stack.append((price, cnt))

        return self.stack[-1][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)