class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        dp = {}

        def level(row,col):

            if (row,col) in dp:
                return dp[(row,col)]
            
            ret = matrix[row][col]

            if row+1 < n:
                choices = []
                for inc in (1,0,-1):
                    nc = col + inc
                    if -1 < nc < n:
                        choices.append(level(row+1,nc))
                ret += min(choices)
            
            dp[(row,col)] = ret

            return ret
        
        r = level(0,0)
        
        for i in range(1,n):
            r = min(r,level(0,i))
                        
        return r
