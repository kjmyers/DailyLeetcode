class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = [0] * n
        half = n//2
        for i in range(half):
            ret[i] = i+1
            ret[i+half] = (-i)-1
        
        return ret
