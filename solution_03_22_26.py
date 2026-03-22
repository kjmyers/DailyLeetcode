class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)

        ret = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    ret = False
        if ret:
            return ret

        ret = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[c][n-1-r]:
                    ret = False
        if ret:
            return ret
        
        ret = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n-1-r][n-1-c]:
                    ret = False
        if ret:
            return ret
        
        ret = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n-1-c][r]:
                    ret = False
        return ret
