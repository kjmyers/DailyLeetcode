class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dirs = (
            (1,2),
            (-1,2),
            (-1,-2),
            (1,-2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1)
        )

        dp = {}

        def solve(r, c, moves):
            if moves == 0:
                return 1
            
            nextMoves = []
            count = 0
            if (r,c,moves) in dp:
                return dp[(r,c,moves)]
            
            ret = 0
            for nr, nc in dirs:
                if 0 <= r + nr < n and 0 <= c + nc < n:
                    ret += solve(r + nr, c + nc, moves-1)
                
            dp[(r,c,moves)] = ret

            return ret
        
        return solve(row, column, k)/(8 ** k)
