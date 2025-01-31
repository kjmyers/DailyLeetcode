class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        toIsland = {}
        islandSize = defaultdict(int)
        largestIsland = 0
        largestComboIsland = 0
        dirs = ((1,0), (0,1), (-1,0), (0,-1))

        def dfs(r,c,seen, islandNum):
            nonlocal largestIsland
            seen.add((r,c))
            toIsland[(r,c)] = islandNum
            islandSize[islandNum] += 1
            largestIsland = max(largestIsland, islandSize[islandNum])
            for dr,dc in dirs:
                nextR = r+dr
                nextC = c+dc
                if 0 <= nextR < rows and 0 <= nextC < cols and grid[nextR][nextC] == 1 and (nextR,nextC) not in seen:
                    dfs(nextR,nextC,seen,islandNum)            
            
        island_count = 0
        
        # Find all the islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in toIsland:
                    dfs(r, c, set(), island_count)
                    island_count += 1
        
        # If no more water, just return
        if largestIsland == rows * cols:
            return largestIsland
        
        # Find all 1 space shorelines between two islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    shores = set()
                    for dr,dc in dirs:
                        nextR = r+dr
                        nextC = c+dc
                        if 0 <= nextR < rows and 0 <= nextC < cols and grid[nextR][nextC] == 1:
                            shores.add(toIsland[(nextR,nextC)])
                    if len(shores) > 1:
                        largestComboIsland = max(largestComboIsland, sum([ islandSize[s] for s in shores]) + 1 )


        return max(largestIsland+1, largestComboIsland)
