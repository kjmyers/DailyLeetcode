class Solution:
    def minPartitions(self, n: str) -> int:
        ret = 0
        for c in n:
            if int(c) > ret:
                ret = int(c)
        
        return ret
