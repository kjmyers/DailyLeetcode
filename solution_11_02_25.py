class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        ret = m*n - len(guards) - len(walls)
        block = set()
        seen = set()
        for r,c in walls:
            block.add((r,c))
        for r,c in guards:
            block.add((r,c))
        
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        for r,c in guards:
            for dr,dc in dirs:
                curR, curC = r+dr, c+dc
                while 0 <= curR < m and 0 <= curC < n and (curR,curC) not in block:
                    if (curR,curC) not in seen:
                        ret -= 1
                        seen.add((curR,curC))
                    curR, curC = curR+dr, curC+dc

        return ret
