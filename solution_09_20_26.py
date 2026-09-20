class Solution:
    def reverseDegree(self, s: str) -> int:
        ret = 0
        for i,l in enumerate(s):
            ret += (26 - (ord(l)-97)) * (i+1)
        
        return ret
