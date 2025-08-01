class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for row in range(1, numRows):
            curRow = [1] * (row+1)
            for i in range(1, row):
                curRow[i] = ret[row-1][i-1] + ret[row-1][i]
            ret.append(curRow)
        
        return ret
