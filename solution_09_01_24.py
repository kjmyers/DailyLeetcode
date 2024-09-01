class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        oLen = len(original)
        if m*n != oLen:
            return []
        
        ret = [[0] * n for _ in range(m)]
        i = 0
        r = 0
        c = 0
        while i < oLen:
            ret[r][c] = original[i]
            c += 1
            if c == n:
                c = 0
                r += 1
            i += 1
        return ret
