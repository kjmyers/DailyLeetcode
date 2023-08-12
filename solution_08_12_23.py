class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        seen = {}

        def solve(i, j):
            if (i,j) in seen:
                return seen[(i,j)]
            
            if i == 0 and j == 0:
                return 0 if obstacleGrid[i][j] == 1 else 1
            
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                seen[(i,j)] = 0
                return seen[(i,j)]
            
            seen[(i,j)] = solve(i,j-1) + solve(i-1,j)

            return seen[(i,j)]
        
        return solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1)
