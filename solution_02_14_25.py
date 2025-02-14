class ProductOfNumbers:

    def __init__(self):
        self.count = 0
        self.h = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.h = [1]
            self.count = 0
        else:
            self.h.append(self.h[self.count] * num)
            self.count += 1
        

    def getProduct(self, k: int) -> int:
        if k > self.count:
            return 0
        
        return (self.h[self.count] // self.h[self.count - k])
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
