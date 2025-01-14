class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        s = set()
        n = len(A)
        ret = [0] * n

        for i in range(n):
            s.add(A[i])
            s.add(B[i])
            ret[i] = 2*(i+1) - len(s)
        
        return ret
