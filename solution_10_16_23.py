class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ret = [1]

        for i in range(1,rowIndex+1):
            cur = [1] * (i+1)
            for j in range(1,i):
                cur[j] = ret[j-1] + ret[j]
            ret = cur
        
        return ret
