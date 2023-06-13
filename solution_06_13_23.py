class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        n = len(grid)

        ret = 0

        for i in range(n):
            d[(",".join([str(x) for x in grid[i]]))] += 1

        for i in range(n):
            col = ",".join([str(x) for x in [row[i] for row in grid]])
            if col in d:
                ret += d[col]
            
        return ret
