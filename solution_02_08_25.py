class NumberContainers:

    def __init__(self):
        self.indices = defaultdict(int)
        self.smallestInd = {}

    def change(self, index: int, number: int) -> None:
        self.indices[index] = number
        if number not in self.smallestInd:
            self.smallestInd[number] = []
        heappush(self.smallestInd[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.smallestInd:
            return -1
        while self.smallestInd[number] and self.indices[ self.smallestInd[number][0] ] != number:
            heappop(self.smallestInd[number])
        if number not in self.smallestInd or not self.smallestInd[number]:
            return -1
        return self.smallestInd[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
