class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ret = [ [0] * (n-2) for x in range(n-2) ]
        print(ret)


        for i in range(1, n-1):
            for j in range(1, n-1):
                for ii in range(-1,2):
                    for jj in range(-1,2):
                        ret[i-1][j-1] = max(ret[i-1][j-1], grid[i+ii][j+jj])
        
        return ret
                
