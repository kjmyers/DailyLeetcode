class Solution:
    def coloredCells(self, n: int) -> int:
        prev = 0
        total = 1

        for i in range(n-1):
            toAdd = 4 + prev
            total += toAdd
            prev = toAdd
        
        return total
