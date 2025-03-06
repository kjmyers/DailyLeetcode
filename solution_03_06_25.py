class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        numset = set()
        for i in range(1,n**2+1):
            numset.add(i)
        
        ret = [0,0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in numset:
                    ret[0] = grid[i][j]
                else:
                    numset.remove(grid[i][j])
        ret[1] = numset.pop()

        return ret
