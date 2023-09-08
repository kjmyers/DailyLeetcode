class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ret = [[1]]

        for i in range(1,numRows):
            cur = [1] * (i+1)
            for j in range(1,i):
                cur[j] = ret[-1][j-1] + ret[-1][j]
            ret.append(cur)
        
        return ret
