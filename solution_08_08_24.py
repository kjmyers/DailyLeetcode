class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        curDir = 0
        ret = []
        cur = [rStart, cStart]
        numSteps = 1

        while len(ret) < rows * cols:
            
            for _ in range(2):
                for _ in range(numSteps):
                    # Add current to ret if in grid
                    if 0 <= cur[0] < rows and 0 <= cur[1] < cols:
                        ret.append(cur[:])
                    
                    # Go to next spot
                    cur[0] = cur[0] + dirs[curDir][0]
                    cur[1] = cur[1] + dirs[curDir][1]

                curDir = (curDir + 1) % 4
            numSteps += 1
        return ret
