class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        ret = 1
        up = 0
        down = 0
        peak = 0

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                up += 1
                peak = up
                down = 0
                ret += 1 + up
            elif ratings[i-1] == ratings[i]:
                peak = 0
                up = 0
                down = 0
                ret += 1
            else:
                up = 0
                down += 1
                ret += (1 + down + (-1 if peak >= down else 0))
        
        return ret
