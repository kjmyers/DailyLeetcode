class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])
        
        mins = []
        for row in range(m):
            minVal = 10**5
            minInd = 0
            for col in range(n):
                if matrix[row][col] < minVal:
                    minVal = matrix[row][col]
                    minInd = col
            mins.append((row,minInd))
        
        ret = []
        for col in range(n):
            maxVal = 1
            maxInd = 0
            for row in range(m):
                if matrix[row][col] > maxVal:
                    maxVal = matrix[row][col]
                    maxInd = row
            if (maxInd, col) in mins:
                ret.append(matrix[maxInd][col])
        

        return ret
            
