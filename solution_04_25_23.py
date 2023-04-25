class SmallestInfiniteSet:

    def __init__(self):
        self.min = 1
        self.out = set()
        

    def popSmallest(self) -> int:
        ret = self.min
        self.out.add(self.min)

        self.min += 1
        while self.min in self.out:
            self.min += 1
        
        return ret
        

    def addBack(self, num: int) -> None:
        if num in self.out:
            self.out.remove(num)
        if num < self.min:
            self.min = num

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
