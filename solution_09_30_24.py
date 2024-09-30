class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.curSize = 0
        self.s = []

    def push(self, x: int) -> None:
        if self.curSize < self.maxSize:
            self.s.append(x)
            self.curSize += 1
        

    def pop(self) -> int:
        if self.s:
            self.curSize -= 1
            return self.s.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.curSize)):
            self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
